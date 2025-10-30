# User Guide for Externa-Kontroller

This guide explains the complete 5-step workflow for using the Externa-Kontroller repository. It includes installation instructions, directory structure explanation, tips for handling large FASTQ files and confidential PDFs, and an example workflow.

## 1. Receive Assignment
Use `1_receive_assignment.py` to receive your assignment. This script fetches the necessary data and prepares it for the next steps.

## 2. Complete Lab Work
Run `2_complete_lab_work.py` to perform the lab work required for your assignment. Ensure that all necessary inputs are in place before executing this script.

## 3. Chemist Assessment
After completing the lab work, use `3_chemist_assessment.py` to assess the results. This step is crucial for ensuring the quality of the lab work.

## 4. Staff Review
Next, run `4_staff_review.py` to conduct a staff review of the assessment results. This step involves collaboration with your team to finalize the findings.

## 5. Generate Reports
Finally, use `5_generate_reports.py` to generate the necessary reports based on the assessment and review outcomes.

---

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/aulund/externa-kontroller.git
   cd externa-kontroller
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Directory Structure
The repository is structured as follows:
```
externa-kontroller/
│
├── 1_receive_assignment.py
├── 2_complete_lab_work.py
├── 3_chemist_assessment.py
├── 4_staff_review.py
├── 5_generate_reports.py
├── requirements.txt
└── HOW-TO-USE.md
```

## Tips for Handling Large FASTQ Files
- Use tools like `fastq-dump` or `seqtk` for efficient processing of large FASTQ files.
- Consider splitting large files into smaller chunks for easier handling and analysis.

## Tips for Handling Confidential PDFs
- Ensure that all confidential PDFs are stored in a secure location.
- Use password protection or encryption for sensitive documents.
- Limit access to authorized personnel only.

## Example Workflow
1. Execute the assignment script:
   ```bash
   python 1_receive_assignment.py
   ```
2. Complete the lab work:
   ```bash
   python 2_complete_lab_work.py
   ```
3. Assess the results:
   ```bash
   python 3_chemist_assessment.py
   ```
4. Review with staff:
   ```bash
   python 4_staff_review.py
   ```
5. Generate your reports:
   ```bash
   python 5_generate_reports.py
   ```

Follow these steps to ensure a smooth workflow in the Externa-Kontroller project.