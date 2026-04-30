# Job-Match
A command-line tool that uses the Claude API to score job descriptions against your resume — surfacing matched skills, gaps, and role-specific talking points to help you apply smarter. Built during my own internship search as a CS student.

## What it does
Paste a job description or point to a .txt file and job-match will:
- Score your fit from 0–100 based on skill and experience overlap
- List matched skills so you know what to lead with
- Identify missing skills so you know what to address or learn
- Generate talking points tailored to that specific role
- Save your history so you can review past matches anytime

## Demo
``` bash
$ python main.py match -f job_description.txt
```
```
Frontend Engineering Intern at Machina Labs
Fit Score: 72/100

Matched Skills:
  ✓ React Native
  ✓ Node.js
  ✓ AWS (S3, Rekognition)
  ✓ API integration
  ...

Missing Skills:
  ✗ Three.js / WebGL
  ...

Talking Points:
  → Project 1 demonstrates real-time data visualization directly relevant to their dashboards
  → Project 2 shows full-stack development with Stripe, Firebase, and AWS integrations
  ...

Strong React and full-stack foundation, but would benefit from adding Three.js skills.
```

## Tech stack
- Python — core CLI logic
- Anthropic Claude API — resume-to-job description analysis and scoring
- trafilatura — extracts text from job posting URLs
- rich — formatted terminal output
- python-dotenv — environment variable management

## Setup
1. Clone the repo
```bash
git clone https://github.com/yourusername/job-match.git
cd job-match
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Add your Anthropic API key
Create a .env file in the project root to contain the key:
```ANTHROPIC_API_KEY=sk-ant-...```
Get an API key at console.anthropic.com.
4. Add your resume
Edit resume.py and replace the RESUME constant with your own resume content as plain text. Example template below:
```python
RESUME = """
John Doe
Computer Science Student at State University
Bachelor of Science in Computer Science: August 2020 to May 2024
Coursework: ...

Projects:
1. Project 1 (React Native, Expo, Node.js, MongoDB, Firebase): ...
2. Project 2 (Python, Claude API): ...
...

Skills:
...
"""
```

## Usage
Match against a .txt file
```bash
python main.py match -f job_description.txt
```
Match against a URL
```bash
python main.py match https://jobs.lever.co/somecompany/some-role
```
Match against inline text
```bash
python main.py match "We are looking for a React Native engineer..."
```
View match history
``` bash
python main.py history
```
View a specific past match
``` bash
python main.py view 3
```

## Project structure
job-match/
├── main.py          # CLI entry point and arg parsing
├── matcher.py       # Claude API call and response parsing
├── history.py       # Read/write match history to JSON
├── fetcher.py       # URL fetching with trafilatura
├── resume.py        # Your resume as a plain text constant
├── history.json     # Auto-generated on first run
├── .env             # API key (not committed)
└── requirements.txt

### Author
Erik Mendoza — mendoza.erik2903@gmail.com