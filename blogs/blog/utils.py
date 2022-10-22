def get_minimized_text(text, length=30):
    if len(text) <= length:
        return text
    return text[:length] + "..."
