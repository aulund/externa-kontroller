import os
import csv
from datetime import datetime

# Prompt for user inputs
program_name = input('Program name: ')
year = input('Year: ')
assessment_date = input('Assessment date (YYYY-MM-DD): ')
assessor_name = input('Assessor name: ')
overall_status = input('Overall status (Godkänd/Delvis godkänd/Ej godkänd): ')
overall_score = int(input('Overall score (0-100): '))
samples_tested = int(input('Samples tested: '))
correct_results = int(input('Correct results: '))
incorrect_results = int(input('Incorrect results: '))
findings_minor_count = int(input('Findings minor count: '))
findings_major_count = int(input('Findings major count: '))
results_description = input('Results description: ')
results_pdf_path = input('Results PDF path: ')
findings_pdf_path = input('Findings PDF path (optional): ') or None
technical_comments = input('Technical comments: ')
improvements = input('Improvements: ')
return_date = input('Return date (YYYY-MM-DD): ')
return_method = input('Return method (E-post/Portal/Post): ')

# Create directory if it does not exist
output_dir = f'programs/{program_name}/{year}'
os.makedirs(output_dir, exist_ok=True)

# Create CSV file
csv_file_path = os.path.join(output_dir, '3_assessment.csv')
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Program Name', 'Year', 'Assessment Date', 'Assessor Name', 'Overall Status', 'Overall Score', 'Samples Tested', 'Correct Results', 'Incorrect Results', 'Findings Minor Count', 'Findings Major Count', 'Results Description', 'Results PDF Path', 'Findings PDF Path', 'Technical Comments', 'Improvements', 'Return Date', 'Return Method'])
    writer.writerow([program_name, year, assessment_date, assessor_name, overall_status, overall_score, samples_tested, correct_results, incorrect_results, findings_minor_count, findings_major_count, results_description, results_pdf_path, findings_pdf_path, technical_comments, improvements, return_date, return_method])

# Copy PDF files to pdfs subfolder
pdfs_dir = 'pdfs/'
os.makedirs(pdfs_dir, exist_ok=True)

# Copy results PDF
if os.path.exists(results_pdf_path):
    os.rename(results_pdf_path, os.path.join(pdfs_dir, os.path.basename(results_pdf_path)))
else:
    print(f'Results PDF not found at {results_pdf_path}')

# Copy findings PDF if provided
if findings_pdf_path and os.path.exists(findings_pdf_path):
    os.rename(findings_pdf_path, os.path.join(pdfs_dir, os.path.basename(findings_pdf_path)))
elif findings_pdf_path:
    print(f'Findings PDF not found at {findings_pdf_path}')

# Confirmation message
print('Bedömt - Väntar på personalmöte')
