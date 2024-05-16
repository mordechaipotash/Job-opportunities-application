### Templates

- `index.html`: Main page that lists all job opportunities.
- `edit.html`: Page to edit job opportunities.
- `job.html`: Page to view detailed job information.

### Scripts

- `app.py`: Main Flask application script.
- `parse_csv.py`: Script to parse the job opportunities CSV file.

### Data

- `jobs.csv`: CSV file containing the job opportunities data.
- `Job_Opportunities_Scorecard.md`: Markdown file with detailed job scorecards.

## Usage

### Viewing Job Opportunities

On the main page (`/`), you can see a list of all job opportunities with brief details. Click on "Mordechai's Fit" to view detailed information about each job.

### Editing Job Opportunities

On the detailed job view page, there is an "Edit" button that takes you to a form where you can update the job details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Flask for providing a simple yet powerful web framework.
- Markdown for easy formatting of documentation.

- ob-opportunities-application/
├── templates/
│   ├── edit.html
│   ├── index.html
│   └── job.html
├── .gitignore
├── Job_Opportunities_Scorecard.md
├── README.md
├── app.py
├── jobs.csv
└── parse_csv.py
