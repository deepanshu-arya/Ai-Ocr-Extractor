import pandas as pd
import json

def export_excel(data, file_path):
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)

def export_json(data, file_path):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)