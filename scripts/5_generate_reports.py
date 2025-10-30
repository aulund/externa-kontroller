import os
import pandas as pd

def scan_directories(base_path):
    reports = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.csv'):
                reports.append(os.path.join(root, file))
    return reports

def generate_reports(csv_files):
    readme_content = "# Generated Reports\n\n"
    accreditation_report_content = "| File | Statistics |\n|------|------------|\n"

    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        summary = df.describe()  # Basic statistics
        readme_content += f"## {os.path.basename(csv_file)}\n\n"
        readme_content += str(summary) + "\n\n"
        
        accreditation_report_content += f"| {os.path.basename(csv_file)} | {summary.to_dict()} |\n"

    return readme_content, accreditation_report_content

def main():
    base_path = 'path/to/program/directories'  # Update with actual path
    csv_files = scan_directories(base_path)
    readme_content, accreditation_report_content = generate_reports(csv_files)

    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)

    with open("ACCREDITATION_REPORT.md", "w") as accreditation_file:
        accreditation_file.write(accreditation_report_content)

if __name__ == "__main__":
    main()