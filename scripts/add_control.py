import os
import csv
from datetime import datetime

def main():
    # Prompt user for control program information
    program_name = input("Enter the program name: ")
    control_date = input("Enter the control date (YYYY-MM-DD): ")
    next_control_date = input("Enter the next control date (YYYY-MM-DD): ")
    status = input("Enter the status: ")
    inspector = input("Enter the inspector's name: ")
    overall_score = input("Enter the overall score: ")
    findings_minor = input("Enter findings (minor): ")
    findings_major = input("Enter findings (major): ")
    action_items = input("Enter action items: ")
    notes = input("Enter any additional notes: ")

    # Create directory structure
    year = datetime.now().year
    base_dir = f"programs/{program_name}/{year}"
    data_file_path = os.path.join(base_dir, "data.csv")
    pdfs_dir = os.path.join(base_dir, "pdfs")

    # Create directories
    os.makedirs(pdfs_dir, exist_ok=True)

    # Write to CSV file
    with open(data_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Program Name", "Control Date", "Next Control Date", "Status", "Inspector", "Overall Score", "Findings Minor", "Findings Major", "Action Items", "Notes"])
        writer.writerow([program_name, control_date, next_control_date, status, inspector, overall_score, findings_minor, findings_major, action_items, notes])

    print("Control program information saved successfully.")

if __name__ == "__main__":
    main()