def analyze_seo(scraped_data: dict) -> dict:
    """
    Analyzes the SEO health of the scraped website data using hardcoded rules.
    Returns a score out of 100, a list of issues found, and specific suggestions.
    """
    score = 100
    issues = []
    suggestions = []

    # 1. Title Analysis
    title = scraped_data.get("title", "")
    if title == "No Title Found" or not title:
        score -= 20
        issues.append("Missing Title Tag")
        suggestions.append("Add a descriptive <title> tag to your HTML <head>.")
    elif len(title) < 10:
        score -= 5
        issues.append("Title Tag is too short")
        suggestions.append("Expand the title tag to be more descriptive (aim for 50-60 characters).")
    elif len(title) > 60:
        score -= 5
        issues.append("Title Tag is too long")
        suggestions.append("Keep the title tag under 60 characters so it doesn't get cut off in search engines.")

    # 2. Meta Description Analysis
    meta_desc = scraped_data.get("meta_description", "")
    if meta_desc == "No Description Found" or not meta_desc:
        score -= 20
        issues.append("Missing Meta Description")
        suggestions.append("Add a <meta name=\"description\" content=\"...\"> tag to improve click-through rates.")
    elif len(meta_desc) < 50:
        score -= 5
        issues.append("Meta Description is too short")
        suggestions.append("Expand the meta description to better describe the page (aim for 150-160 characters).")
    elif len(meta_desc) > 160:
        score -= 5
        issues.append("Meta Description is too long")
        suggestions.append("Keep the meta description under 160 characters for optimal display in search results.")

    # 3. Headings Analysis
    headings = scraped_data.get("headings", {})
    h1_tags = headings.get("h1", [])
    
    if len(h1_tags) == 0:
        score -= 15
        issues.append("Missing H1 Heading")
        suggestions.append("Every page should have exactly one <h1> tag indicating the main topic.")
    elif len(h1_tags) > 1:
        score -= 5
        issues.append("Multiple H1 Headings")
        suggestions.append("Consider using only one <h1> tag per page to maintain clear structure.")

    # Ensure score doesn't go below 0
    score = max(0, score)

    return {
        "tool_name": "SEO Analyzer",
        "score": score,
        "issues": issues,
        "suggestions": suggestions
    }

# Quick test logic
if __name__ == "__main__":
    test_data = {
        "title": "Short",
        "meta_description": "No Description Found",
        "headings": {"h1": []}
    }
    import json
    print(json.dumps(analyze_seo(test_data), indent=2))
