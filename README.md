# AI-Powered Lead Qualification & Outreach Automation System

An AI-powered GTM (Go-To-Market) automation system developed using Python, FastAPI, Pandas, Google Gemini API, and n8n. The system automates lead qualification and personalized outreach draft generation to reduce repetitive work in B2B sales processes.

## 1. Project Overview

This project demonstrates how AI and workflow automation can streamline lead qualification and outreach preparation.

The application processes company information from a CSV file, cleans and validates the data, removes duplicate records, and prioritizes potential customers using predefined business criteria. High-priority leads are then processed using Google Gemini to generate company summaries and personalized outreach email drafts.

FastAPI provides the backend endpoints, while n8n orchestrates the workflow through manual and scheduled triggers. Generated emails are saved for human review rather than being sent automatically.

## 2. Key Features

- **Lead Data Processing:** Import company information from CSV, handle missing values, and remove duplicate records.
- **Automated Lead Scoring:** Evaluate potential customers using industry, employee count, and identified automation needs.
- **Lead Prioritization:** Classify companies into High, Medium, and Low priority.
- **AI-Powered Outreach:** Generate company summaries and personalized B2B outreach email drafts using Google Gemini.
- **FastAPI Integration:** Expose endpoints for executing the lead qualification and AI outreach processes.
- **Workflow Automation:** Use n8n to automatically execute the pipeline at scheduled intervals.
- **Duplicate Prevention:** Avoid repeatedly generating outreach drafts for companies that have already been processed.
- **Human Review:** Save generated emails with a Pending Review status before any external communication.

## 3. Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Backend | FastAPI, Uvicorn |
| Data Processing | Pandas |
| AI Integration | Google Gemini API |
| Workflow Automation | n8n |
| Data Storage | CSV |
| Development Tools | Git, GitHub, VS Code |

## 4. System Workflow

The system follows these steps:

1. **Workflow Trigger:** n8n initiates the workflow manually or at a scheduled time.
2. **Lead Processing:** FastAPI triggers the Python pipeline to import, clean, and validate company data.
3. **Lead Qualification:** Companies are scored using predefined business criteria and assigned a priority.
4. **AI Outreach Generation:** High-priority leads are processed using Google Gemini to generate company summaries and personalized outreach drafts.
5. **Duplicate Prevention:** Previously processed companies are skipped to avoid generating duplicate drafts.
6. **Result Storage:** Qualified leads and generated outreach drafts are saved in CSV files for review.

## 5. Lead Scoring Criteria

The system uses a rule-based scoring mechanism.

| Criteria | Points |
|---|---:|
| Software, Technology, or SaaS industry | 40 |
| Company with 20–200 employees | 30 |
| Identified automation need in the input data | 30 |
| **Maximum score** | **100** |

Companies are classified as follows:

- **High Priority:** 70–100 points
- **Medium Priority:** 40–69 points
- **Low Priority:** 0–39 points

These criteria are illustrative and can be adjusted to match a company's Ideal Customer Profile (ICP).

## 6. Project Structure

- `app/main.py` — FastAPI application and API endpoints
- `app/pipeline.py` — Lead cleaning, qualification, and scoring
- `app/outreach.py` — Gemini integration and outreach generation
- `data/leads.csv` — Input company data
- `outputs/qualified_leads.csv` — Processed and prioritized leads
- `outputs/outreach_drafts.csv` — AI-generated outreach drafts
- `.env.example` — Sample environment configuration
- `requirements.txt` — Python dependencies

The `outputs` directory is generated during execution and excluded from Git.

## 7. Installation and Setup

**Prerequisites:** Python, Node.js and npm, and a Google Gemini API key.

**Step 1: Clone the repository**

Clone this repository from GitHub and open the project folder in VS Code.

**Step 2: Create and activate a virtual environment**

On Windows, execute the following commands in the project terminal:

- `py -m venv .myenv`
- `.\.myenv\Scripts\Activate.ps1`

**Step 3: Install Python dependencies**

Run `python -m pip install -r requirements.txt`.

**Step 4: Configure environment variables**

Copy `.env.example` to a new file named `.env`. Add your Gemini API key and configure the model you have access to.

Never commit your actual API key to the repository.

## 8. Running the Application

**Run the lead qualification pipeline**

Execute `python -m app.pipeline` to process the sample company data and generate the qualified leads CSV.

**Start FastAPI**

Run `python -m uvicorn app.main:app --reload`.

Access the interactive API documentation at `http://127.0.0.1:8000/docs`.

The application provides these endpoints:

| Endpoint | Method | Purpose |
|---|---|---|
| `/` | GET | Application information |
| `/health` | GET | API health check |
| `/process-leads` | POST | Execute lead qualification |
| `/generate-drafts` | POST | Generate AI outreach drafts |

Execute `/process-leads` before `/generate-drafts`.

**Start n8n**

In a separate terminal, run `npx.cmd n8n`.

Open `http://localhost:5678` and configure or import the AI GTM Lead Automation workflow.

Connect the Manual Trigger and Schedule Trigger to the first HTTP Request node. Configure two consecutive POST requests:

- `http://127.0.0.1:8000/process-leads`
- `http://127.0.0.1:8000/generate-drafts`

Publish the workflow to enable scheduled execution.

Since this application runs locally, both FastAPI and n8n must be running for scheduled automation to complete.

## 9. Testing and Results

The initial prototype was tested using fictional company data.

The lead qualification pipeline processed four unique companies and assigned scores and priorities based on predefined criteria. The Gemini integration successfully generated a company summary and a personalized outreach email for a high-priority lead.

The n8n workflow was also tested through manual and scheduled execution, with successful API responses from both the lead-processing and outreach-generation endpoints.

Generated email drafts are saved with a Pending Review status.

## 10. Current Limitations

- The current prototype uses supplied CSV records rather than automatically discovering companies.
- Lead scores are based on predefined business rules rather than a trained machine learning model.
- Gemini generates content using the supplied company information; the application does not independently verify business details.
- The application does not automatically send emails or manage customer relationships through an external CRM.
- Scheduled execution depends on the local computer, FastAPI server, and n8n being available.

## 11. Future Enhancements

- Integrate HubSpot CRM to manage lead information and sales pipelines.
- Connect lead enrichment APIs to retrieve additional business information.
- Develop a dashboard for viewing qualified leads and reviewing outreach drafts.
- Add campaign analytics and performance monitoring.
- Deploy the application and automation workflow to a cloud environment.

## 12. Responsible Use

The project uses fictional data for initial testing. When working with real companies, business information should be obtained from appropriate sources and verified before being used in outreach.

All AI-generated emails require human review. The system is intended to support responsible sales automation, not to send unsolicited messages automatically.