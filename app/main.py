from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
import uvicorn

from app.scraper import scrape_website
from app.seo_tool import analyze_seo
from app.content_tool import analyze_content
from app.accessibility_tool import analyze_accessibility
from app.agent import generate_audit_report
from app.database import engine, get_db
from app.models import Base, AuditRecord
from sqlalchemy.orm import Session
from fastapi import Depends

# Create the database tables if they don't exist
Base.metadata.create_all(bind=engine)

# Initialize the FastAPI app
app = FastAPI(
    title="AI Website Auditor Agent",
    description="An API to audit websites using AI agents.",
    version="1.0.0"
)

# Phase 1: Health Check Endpoint
@app.get("/health")
async def health_check():
    """
    A simple endpoint to verify the server is running.
    Returns a status message.
    """
    return {"status": "ok", "message": "AI Website Auditor server is running."}

# Phase 5: The main Audit Endpoint
class AuditRequest(BaseModel):
    url: str

@app.post("/audit")
async def perform_audit(request: AuditRequest, db: Session = Depends(get_db)):
    """
    Endpoint that takes a URL, scrapes it, analyzes it using tools, 
    and generates an AI summary report. Results are saved to PostgreSQL.
    """
    url = request.url
    if not url.startswith("http"):
        # Tell the user they made a mistake if they forgot http://
        raise HTTPException(status_code=400, detail="URL must start with http:// or https://")
        
    # Step 1: Scrape the website (using Playwright + BeautifulSoup)
    scraped_data = await scrape_website(url)
    if scraped_data.get("status") == "error":
        raise HTTPException(status_code=500, detail=f"Failed to scrape website: {scraped_data.get('message')}")
        
    # Step 2: Run the Hardcoded Tools on the data
    seo_results = analyze_seo(scraped_data)
    content_results = analyze_content(scraped_data)
    accessibility_results = analyze_accessibility(scraped_data)
    
    # Step 3: Run the AI Agent to get the executive summary
    ai_summary = generate_audit_report(scraped_data, seo_results, content_results, accessibility_results)
    
    # Step 4: Save the result to the Database
    db_audit = AuditRecord(
        url=url,
        seo_score=seo_results.get("score"),
        content_score=content_results.get("score"),
        accessibility_score=accessibility_results.get("score"),
        ai_summary=ai_summary,
        detailed_data={
            "seo": seo_results,
            "content": content_results,
            "accessibility": accessibility_results
        }
    )
    db.add(db_audit)
    db.commit()
    db.refresh(db_audit)
    
    # Step 5: Return the final JSON payload
    return {
        "id": db_audit.id,
        "url": url,
        "ai_summary": ai_summary,
        "scores": {
            "seo": seo_results.get("score"),
            "content": content_results.get("score"),
            "accessibility": accessibility_results.get("score")
        },
        "created_at": db_audit.created_at
    }

# Phase 8: WebSocket Endpoint for Real-Time Streaming
@app.websocket("/ws/audit")
async def websocket_audit(websocket: WebSocket, db: Session = Depends(get_db)):
    """
    WebSocket endpoint that streams progress messages back to the user
    in real-time as the audit is executing.
    """
    await websocket.accept()
    
    try:
        # Wait for the client to send a URL
        data = await websocket.receive_text()
        url = data.strip()
        
        if not url.startswith("http"):
            await websocket.send_json({"error": "URL must start with http:// or https://"})
            await websocket.close()
            return
            
        # Step 1: Scraping
        await websocket.send_json({"log": "🕷️ Expanding web scraper... connecting to URL..."})
        scraped_data = await scrape_website(url)
        if scraped_data.get("status") == "error":
            await websocket.send_json({"error": f"Failed to scrape: {scraped_data.get('message')}"})
            await websocket.close()
            return
            
        # Step 2: Tools Check
        await websocket.send_json({"log": "🔍 Scraping successful! Now analyzing SEO, Content, and Accessibility..."})
        seo_results = analyze_seo(scraped_data)
        content_results = analyze_content(scraped_data)
        accessibility_results = analyze_accessibility(scraped_data)
        
        # Step 3: AI Reasoning
        await websocket.send_json({"log": "🧠 Tool analysis complete! Asking the AI Agent to generate recommendations..."})
        ai_summary = generate_audit_report(scraped_data, seo_results, content_results, accessibility_results)
        
        # Step 4: Storage
        await websocket.send_json({"log": "🗄️ Saving results to database..."})
        db_audit = AuditRecord(
            url=url,
            seo_score=seo_results.get("score"),
            content_score=content_results.get("score"),
            accessibility_score=accessibility_results.get("score"),
            ai_summary=ai_summary,
            detailed_data={
                "seo": seo_results,
                "content": content_results,
                "accessibility": accessibility_results
            }
        )
        db.add(db_audit)
        db.commit()
        db.refresh(db_audit)
        
        # Final Step: Send the complete report
        await websocket.send_json({
            "log": "✅ Audit Complete!",
            "result": {
                "id": db_audit.id,
                "url": url,
                "ai_summary": ai_summary,
                "scores": {
                    "seo": seo_results.get("score"),
                    "content": content_results.get("score"),
                    "accessibility": accessibility_results.get("score")
                }
            }
        })
        
        # Close the connection nicely
        await websocket.close()
        
    except WebSocketDisconnect:
        print("Client disconnected before audit finished.")
    except Exception as e:
        await websocket.send_json({"error": f"An unexpected error occurred: {str(e)}"})
        await websocket.close()

# To run the server during development:
if __name__ == "__main__":
    print("Starting server... Press Ctrl+C to stop.")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
