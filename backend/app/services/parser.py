import re

def parse_receipt(text):
    total = re.findall(r'\d+\.\d{2}', text)
    date = re.findall(r'\d{2}/\d{2}/\d{4}', text)

    return {
        "vendor": text.split("\n")[0],
        "total": total[-1] if total else "0",
        "date": date[0] if date else "N/A"
    }