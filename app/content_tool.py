def analyze_content(scraped_data: dict) -> dict:
    """
    Analyzes the content quality of the scraped website data using hardcoded rules.
    Evaluates word counts and basic structural presence.
    Returns a score out of 100, a list of issues found, and specific suggestions.
    """
    score = 100
    issues = []
    suggestions = []

    # Get the paragraphs
    paragraphs = scraped_data.get("paragraphs", [])
    
    # Calculate Word Count
    total_words = 0
    for p in paragraphs:
        # Split paragraph into words based on spaces
        total_words += len(p.split())
        
    if total_words == 0:
        score -= 50
        issues.append("No Body Content Found")
        suggestions.append("Ensure your page has text content in <p> tags.")
    elif total_words < 300:
        score -= 20
        issues.append("Thin Content")
        suggestions.append(f"Your page only has {total_words} words. Search engines generally prefer comprehensive content (300+ words).")

    # Paragraph structure check
    if len(paragraphs) == 1 and total_words > 100:
        score -= 10
        issues.append("Poor Readability Structure")
        suggestions.append("Break up large blocks of text into smaller paragraphs to make it easier to read.")

    # Ensure score doesn't go below 0
    score = max(0, score)

    return {
        "tool_name": "Content Analyzer",
        "score": score,
        "word_count": total_words,
        "issues": issues,
        "suggestions": suggestions
    }

# Quick test logic
if __name__ == "__main__":
    test_data = {
        "paragraphs": ["This is a very short test."]
    }
    import json
    print(json.dumps(analyze_content(test_data), indent=2))
