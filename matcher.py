import anthropic
import json
from resume import RESUME

SYSTEM_PROMPT = """
You are a job application assistant. Given a resume and a job description,
return a JSON object with exactly these fields:
- company: string
- role: string
- fit_score: integer 0-100
- matched_skills: list of strings
- missing_skills: list of strings
- talking_points: list of strings (what to emphasize in this application)
- summary: one sentence overall assessment

Return only valid JSON. No markdown, no preamble.
"""

def match(job_description: str) -> dict:
    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1000,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": f"Resume:\n{RESUME}\n\nJob Description:\n{job_description}"
            }
        ]
    )
    raw = response.content[0].text.strip()
    raw = raw.removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    return json.loads(raw)