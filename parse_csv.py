import csv

def parse_csv_file(csv_file_path):
    jobs = []
    with open(csv_file_path, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            job = {}
            for k, v in row.items():
                try:
                    key = k.strip() if k else k
                    value = v.strip() if v else v
                    job[key] = value
                except AttributeError as e:
                    print(f"Error processing row {row}: {e}")
                    job[key] = v
            print(f"Processed job: {job}")  # Debug print
            jobs.append(job)
    return jobs

csv_file_path = 'jobs.csv'  # Update this with your actual CSV file path
parsed_jobs = parse_csv_file(csv_file_path)
print(parsed_jobs)