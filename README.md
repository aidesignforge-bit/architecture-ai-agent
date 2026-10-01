# Architecture Layout & Project Data AI Agent — V1

A starter AI-agent dashboard for architecture/project-layout workflows.

## Included
- Project name / builder / location / RERA fields
- Project-data checklist with NOT FOUND status
- Layout / brochure upload UI
- Multiple-layout workflow notes
- Unit conversion: mm, cm, m, inch, feet
- Required output unit: feet + inches
- Canva template/page-size configuration
- 4K/8K export settings
- Verification status: VERIFIED / SOURCE CHECK / NOT FOUND / NEEDS REVIEW
- Architecture-safe rule: never invent unclear dimensions

## Run
1. Install Python 3.10+
2. `pip install -r requirements.txt`
3. `streamlit run app.py`

## Important
This V1 is a local prototype. It does NOT yet log into Canva, automatically browse the web, or perform AI OCR/vision by itself. Those are integration points for V2 after you provide the real templates/API credentials and source requirements.
