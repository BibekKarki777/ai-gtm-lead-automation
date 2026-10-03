
from fastapi import FastAPI, HTTPException
from app.pipeline import process_leads
from app.outreach import generate_drafts
from google.genai import errors


app = FastAPI(
    title="AI GTM Lead Automation",
    description="AI-powered lead qualification and outreach system"
)


@app.get("/")
def home():
    return {"message": "AI GTM Automation API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/process-leads")
def run_lead_pipeline():
    try:
        df = process_leads()

        leads = [
            {
                "company": row.company,
                "lead_score": int(row.lead_score),
                "priority": row.priority
            }
            for row in df.itertuples()
        ]

        return {
            "message": "Leads processed successfully",
            "total_leads": len(leads),
            "qualified_leads": leads
        }

    except FileNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="The leads.csv file was not found."
        )

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@app.post("/generate-drafts")
def create_outreach_drafts():
    try:
        drafts = generate_drafts()

        return {
            "message": "AI drafts generated successfully",
            "total_drafts": len(drafts),
            "drafts": drafts
        }

    except FileNotFoundError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except errors.APIError:
        raise HTTPException(
            status_code=502,
            detail="Gemini API request failed. Check your model and API limits."
        )
