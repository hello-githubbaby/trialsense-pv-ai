from .llm_client import call_llm
import json

def extract_adr_from_text(text: str) -> dict:
    """
    Extract adverse drug reactions (ADRs) from raw clinical/medical text.
    Uses an LLM for entity detection.
    """

    prompt = f"""
    You are an expert pharmacovigilance assistant.
    Extract Adverse Drug Reactions (ADRs) from the following text.

    Return a JSON array of:
    {{
        "reaction": "",
        "drug": "",
        "severity": "mild | moderate | severe | unknown",
        "evidence_excerpt": ""
    }}

    TEXT:
    {text[:3000]}
    """

    output = call_llm(prompt)

    try:
        return json.loads(output)
    except:
        return {"raw_extraction": output}
