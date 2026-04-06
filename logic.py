def categorize_task(text: str) -> str:
    text = text.lower()
    if not text.strip():
        return "Invalid"
    if "терміново" in text or "urgent" in text:
        return "High Priority"
    if "баг" in text or "error" in text:
        return "Bug"
    return "Final Main Task"