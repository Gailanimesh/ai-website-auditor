def analyze_accessibility(scraped_data: dict) -> dict:
    """
    Analyzes the accessibility of the scraped website data using hardcoded rules.
    Currently focuses on image 'alt' tag presence.
    Returns a score out of 100, a list of issues found, and specific suggestions.
    """
    score = 100
    issues = []
    suggestions = []

    # Analyze images
    images = scraped_data.get("images", [])
    total_images = len(images)
    
    if total_images == 0:
        # No images, no accessibility issues related to images
        return {
            "tool_name": "Accessibility Analyzer",
            "score": score,
            "issues": ["No images found to analyze."],
            "suggestions": []
        }
        
    missing_alt_count = 0
    for img in images:
        # Check if alt exists and is not an empty string
        if img.get("alt") is None or str(img.get("alt")).strip() == "":
            missing_alt_count += 1
            
    if missing_alt_count > 0:
        # Calculate penalty based on percentage of missing alt tags
        penalty = int((missing_alt_count / total_images) * 40) # Max 40 point penalty for images
        score -= penalty
        issues.append(f"{missing_alt_count} out of {total_images} images are missing 'alt' descriptions.")
        suggestions.append("Add descriptive 'alt' text to all images to help visually impaired users and improve SEO.")

    # Ensure score doesn't go below 0
    score = max(0, score)

    return {
        "tool_name": "Accessibility Analyzer",
        "score": score,
        "issues": issues,
        "suggestions": suggestions
    }

# Quick test logic
if __name__ == "__main__":
    test_data = {
        "images": [{"src": "img1.jpg", "alt": None}, {"src": "img2.jpg", "alt": "A cat"}]
    }
    import json
    print(json.dumps(analyze_accessibility(test_data), indent=2))
