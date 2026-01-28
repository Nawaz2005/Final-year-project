from datetime import datetime

def save_report(name, wound_type, days):
    with open("patient_reports.txt", "a") as f:
        f.write(f"{datetime.now()} | {name} | {wound_type} | {days} days\n")
