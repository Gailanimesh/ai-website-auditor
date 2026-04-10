import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables (API Keys) from the .env file
load_dotenv()

def generate_audit_report(scraped_data: dict, seo_results: dict, content_results: dict, accessibility_results: dict) -> str:
    """
    Takes the hardcoded "Math/Fact" scores from our Phase 3 tools and passes
    them to a LangChain LLM (Groq) to generate a human-readable executive summary.
    """
    # 1. Initialize the AI Model. 
    # It will automatically look for GROQ_API_KEY in your .env file
    try:
        llm = ChatGroq(
            model="llama-3.1-8b-instant", # This is a fast, free, and excellent open-source model available via Groq
            temperature=0.2, # Low temperature means more analytical, less "creative"
        )
    except Exception as e:
        return "Error connecting to AI. Did you remember to put your GROQ_API_KEY in the .env file?"

    # 2. Create the Prompt (The Instructions)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert Website Auditor. Your job is to read technical tool outputs and summarize them into a simple, beginner-friendly report for the website owner. Do not use extremely technical jargon. Keep the summary under 3 paragraphs and be encouraging."),
        ("human", """
        Please analyze this website: {url}
        
        1. SEO Score: {seo_score}/100
        SEO Issues: {seo_issues}
        
        2. Content Score: {content_score}/100
        Content Issues: {content_issues}
        
        3. Accessibility Score: {access_score}/100
        Accessibility Issues: {access_issues}
        
        Provide a concise executive summary of these results. Point out what they did well, and what their biggest priority to fix is. Do not just restate the numbers, give them advice!
        """)
    ])

    # 3. Combine the Prompt and the LLM into a "Chain"
    chain = prompt | llm
    
    # 4. Give the Chain our specific data and run it
    try:
        print("Waiting for AI reasoning...")
        response = chain.invoke({
            "url": scraped_data.get("url", "Unknown URL"),
            "seo_score": seo_results.get("score"),
            "seo_issues": seo_results.get("issues"),
            "content_score": content_results.get("score"),
            "content_issues": content_results.get("issues"),
            "access_score": accessibility_results.get("score"),
            "access_issues": accessibility_results.get("issues"),
        })
        return response.content
    except Exception as e:
         return f"AI Generation Failed: {str(e)}"

# Quick test logic to see if it works!
if __name__ == "__main__":
    test_url_data = {"url": "https://example.com"}
    test_seo = {"score": 80, "issues": ["Needs longer title"]}
    test_content = {"score": 90, "issues": []}
    test_access = {"score": 50, "issues": ["Missing image alt tags"]}
    
    print(generate_audit_report(test_url_data, test_seo, test_content, test_access))
