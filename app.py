from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

# Path to the CSV file
csv_file_path = 'jobs.csv'  # Update this with your actual CSV file path

def parse_csv_file(csv_file_path):
    jobs = []
    with open(csv_file_path, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            job = {}
            for k, v in row.items():
                key = k.strip() if k else k
                value = v.strip() if v else v
                job[key] = value
            jobs.append(job)
    return jobs

@app.route('/')
def index():
    jobs = parse_csv_file(csv_file_path)
    return render_template('index.html', jobs=jobs)

@app.route('/edit/<int:job_id>', methods=['GET', 'POST'])
def edit(job_id):
    jobs = parse_csv_file(csv_file_path)
    job = jobs[job_id]

    if request.method == 'POST':
        job['Name'] = request.form['name']
        job['Company'] = request.form['company']
        job['Requirements'] = request.form['requirements']
        job['Job Fit Summary'] = request.form['job_fit_summary']
        job['Overall Assesment'] = request.form['overall_assessment']
        job['Scorecard'] = request.form['scorecard']
        job['Full Job Post'] = request.form['full_job_post']
        
        # Save updated job details to CSV file
        with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as csv_file:
            fieldnames = jobs[0].keys()
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(jobs)
        
        return redirect(url_for('index'))

    return render_template('edit.html', job=job, job_id=job_id)

@app.route('/job/<int:job_id>')
def job(job_id):
    jobs = parse_csv_file(csv_file_path)
    job = jobs[job_id]
    return render_template('job.html', job=job)

if __name__ == '__main__':
    app.run(debug=True)