import csv
import os

# Prompt for input
program_name = input('Program Name: ')
year = input('Year: ')
review_date = input('Review Date: ')
meeting_leader = input('Meeting Leader: ')
attendees = input('Attendees (comma-separated): ')
decision = input('Decision (OK/Ej OK/Villkorligt OK): ')
group_comments = input('Group Comments: ')
learnings_improvements = input('Learnings and Improvements: ')
follow_up_required = input('Follow-up Required (y/n): ')
next_actions = input('Next Actions: ')
formal_approval_by = input('Formal Approval By: ')
approval_signature_id = input('Approval Signature/ID: ')

# Create directory if it doesn't exist
output_dir = f'programs/{program_name}/{year}/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define CSV file path
csv_file_path = os.path.join(output_dir, '4_review.csv')

# Write data to CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Review Date', 'Program Name', 'Year', 'Meeting Leader', 'Attendees', 'Decision', 'Group Comments', 'Learnings and Improvements', 'Follow-up Required', 'Next Actions', 'Formal Approval By', 'Approval Signature/ID'])
    writer.writerow([review_date, program_name, year, meeting_leader, attendees, decision, group_comments, learnings_improvements, follow_up_required, next_actions, formal_approval_by, approval_signature_id])

# Confirm status
print('Komplett - Redo för rapportering')
