
from pathlib import Path
import pandas as pd

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "data" / "leads.csv"
OUTPUT_FILE = BASE_DIR / "outputs" / "qualified_leads.csv"


def score_lead(row):
    score = 0

    if row["industry"].lower() in ["software", "technology", "saas"]:
        score += 40

    if pd.notna(row["employees"]) and 20 <= row["employees"] <= 200:
        score += 30

    if row["automation_need"].lower() == "yes":
        score += 30

    return score


def get_priority(score):
    if score >= 70:
        return "High"
    elif score >= 40:
        return "Medium"
    return "Low"


def process_leads():
    # Load and validate the dataset
    df = pd.read_csv(INPUT_FILE)

    required_columns = [
        "company", "website", "industry",
        "employees", "automation_need"
    ]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing column: {column}")

    # Clean the records
    df["company"] = df["company"].fillna("").str.strip()
    df["website"] = df["website"].fillna("").str.strip().str.lower()
    df["industry"] = df["industry"].fillna("").str.strip()
    df["automation_need"] = df["automation_need"].fillna("").str.strip()

    df = df[(df["company"] != "") & (df["website"] != "")]
    df = df.drop_duplicates(subset=["website"]).copy()
    df["employees"] = pd.to_numeric(df["employees"], errors="coerce")

    # Qualify the leads
    df["lead_score"] = df.apply(score_lead, axis=1)
    df["priority"] = df["lead_score"].apply(get_priority)

    df = df.sort_values("lead_score", ascending=False)

    # Save the processed results
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)

    return df


if __name__ == "__main__":
    results = process_leads()

    print(results[["company", "lead_score", "priority"]].to_string(index=False))
    print(f"\nResults saved to: {OUTPUT_FILE}")
