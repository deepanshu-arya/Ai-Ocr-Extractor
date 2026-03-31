import requests

def parse_with_ai(text):
    prompt = f"""
    Extract structured data from this receipt:
    {text}

    Return JSON:
    vendor, total, date, items
    """

    # You can replace with OpenAI API later
    response = {
        "vendor": "AI Shop",
        "total": "250",
        "date": "2026-03-30",
        "items": ["milk", "bread"]
    }

    return response