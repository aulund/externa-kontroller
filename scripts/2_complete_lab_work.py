import os
import shutil
import pandas as pd

def main():
    # Gather input from the user
    assignment = input("Select existing assignment: ")
    analysis_start_date = input("Analysis start date (YYYY-MM-DD): ")
    analysis_end_date = input("Analysis end date (YYYY-MM-DD): ")
    method_protocol = input("Method/Protocol: ")
    instrument_used = input("Instrument Used: ")
    fastq_directory = input("FASTQ files directory: ")
    sanger_directory = input("Sanger AB1 files directory: ")
    references_directory = input("Reference sequences directory: ")
    sequencing_quality = input("Sequencing quality: ")
    coverage = input("Coverage: ")
    pass_rate = input("Pass rate: ")
    lab_notes = input("Lab notes: ")

    # Create directories if they don't exist
    os.makedirs('raw-data/fastq/', exist_ok=True)
    os.makedirs('raw-data/sanger/', exist_ok=True)
    os.makedirs('references/', exist_ok=True)

    # Copy data files to the respective directories
    for file_name in os.listdir(fastq_directory):
        shutil.copy(os.path.join(fastq_directory, file_name), 'raw-data/fastq/')
    
    for file_name in os.listdir(sanger_directory):
        shutil.copy(os.path.join(sanger_directory, file_name), 'raw-data/sanger/')

    for file_name in os.listdir(references_directory):
        shutil.copy(os.path.join(references_directory, file_name), 'references/')

    # Create the CSV file
    data = {
        'Assignment': [assignment],
        'Analysis Start Date': [analysis_start_date],
        'Analysis End Date': [analysis_end_date],
        'Method/Protocol': [method_protocol],
        'Instrument Used': [instrument_used],
        'Sequencing Quality': [sequencing_quality],
        'Coverage': [coverage],
        'Pass Rate': [pass_rate],
        'Lab Notes': [lab_notes]
    }
    
    df = pd.DataFrame(data)
    df.to_csv('2_lab_work.csv', index=False)

    # Display confirmation
    print("Lab work complete - Waiting for assessment")
    print("File sizes:")
    print(f"FASTQ files copied: {sum(os.path.getsize(os.path.join('raw-data/fastq/', f)) for f in os.listdir('raw-data/fastq/') if os.path.isfile(os.path.join('raw-data/fastq/', f)))} bytes")
    print(f"Sanger files copied: {sum(os.path.getsize(os.path.join('raw-data/sanger/', f)) for f in os.listdir('raw-data/sanger/') if os.path.isfile(os.path.join('raw-data/sanger/', f)))} bytes")
    print(f"Reference files copied: {sum(os.path.getsize(os.path.join('references/', f)) for f in os.listdir('references/') if os.path.isfile(os.path.join('references/', f)))} bytes")

if __name__ == "__main__":
    main()