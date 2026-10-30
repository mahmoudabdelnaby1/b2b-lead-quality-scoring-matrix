#!/usr/bin/env python3
import argparse
import csv
import json
import sys
from pathlib import Path

def score_b2b_leads(csv_path, rules_path, out_csv):
    with open(rules_path, "r", encoding="utf-8") as f:
        rules = json.load(f)

    scored_rows = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames + ["fit_score", "lead_tier"]
        for r in reader:
            score = 0
            # Country weighting
            country = r.get("country", "").upper()
            score += rules.get("country_weights", {}).get(country, 10)
            # Company Size
            size = r.get("company_size", "")
            score += rules.get("size_weights", {}).get(size, 10)
            # Seniority
            title = r.get("job_title", "").lower()
            if any(k in title for k in ["cfo", "ceo", "founder", "head", "director", "مدير"]):
                score += 35
            else:
                score += 15

            tier = "SQL (Sales Qualified)" if score >= 75 else ("MQL (Marketing Qualified)" if score >= 50 else "DISQUALIFIED")
            r["fit_score"] = score
            r["lead_tier"] = tier
            scored_rows.append(r)

    Path(out_csv).parent.mkdir(parents=True, exist_ok=True)
    with open(out_csv, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(scored_rows)
    return len(scored_rows)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--csv", required=True)
    p.add_argument("--rules", default="config/scoring_rules.json")
    p.add_argument("--out", default="reports/scored_leads.csv")
    args = p.parse_args()

    c = score_b2b_leads(args.csv, args.rules, args.out)
    print(f"Scored {c} inbound B2B leads -> {args.out}")

if __name__ == "__main__":
    main()
