import asyncio
import sys
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def _sync_scrape(url: str):
    """
    Synchronous scraping logic using Playwright. 
    This entirely avoids the Uvicorn Windows Event Loop bugs because 
    it is run in a separate Isolated Thread!
    """
    print(f"Starting scrape for: {url}")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto(url, wait_until="networkidle", timeout=30000)
            html_content = page.content()
            browser.close()
            
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Extract Title
            title = soup.title.string if soup.title else "No Title Found"
            
            # Extract Meta Description
            meta_desc = "No Description Found"
            meta_tag = soup.find("meta", attrs={"name": "description"}) or soup.find("meta", attrs={"property": "og:description"})
            if meta_tag:
                meta_desc = meta_tag.get("content", "No Description Found")
            
            # Extract Headings (H1 - H6)
            headings = {}
            for i in range(1, 7):
                tag = f"h{i}"
                headings[tag] = [h.get_text(strip=True) for h in soup.find_all(tag)]
            
            # Extract Images and check for Alt text
            images = []
            for img in soup.find_all("img"):
                src = img.get("src")
                alt = img.get("alt")
                if src:
                    images.append({
                        "src": src,
                        "alt": alt if alt else None 
                    })
            
            # Extract Paragraphs (first 10 to keep it manageable)
            paragraphs = [p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)][:10]

            return {
                "url": url,
                "title": title,
                "meta_description": meta_desc,
                "headings": headings,
                "images": images,
                "paragraphs": paragraphs,
                "status": "success"
            }

        except Exception as e:
            try:
                browser.close()
            except:
                pass
            return {
                "url": url,
                "status": "error",
                "message": str(e)
            }


async def scrape_website(url: str):
    """
    Takes the synchronous scraper and runs it in the background thread pool
    so it doesn't block the FastAPI server or trigger Windows asyncio process errors.
    """
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, _sync_scrape, url)


if __name__ == "__main__":
    test_url = "https://webscraper.io/test-sites/e-commerce/allinone"
    data = asyncio.run(scrape_website(test_url))
    import json
    print(json.dumps(data, indent=2))
