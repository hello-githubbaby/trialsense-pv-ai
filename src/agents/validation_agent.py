from .llm_client import call_llm
import json

def validate_adr_report(report) -> dict:
    """
    Validate ADR JSON extracted by the extraction agent.
    Ensures fields, consistency, and valid severity categories.
    """

    prompt = f"""
    You are a pharmacovigilance validation agent.
    Validate and correct this ADR report.

    Ensure:
    - 'reaction', 'drug', 'severity', 'evidence_excerpt' exist
    - severity ∈ {{mild, moderate, severe, unknown}}

    Return VALIDATED JSON only.

    REPORT:
    {report}
    """

    output = call_llm(prompt)

    try:
        return json.loads(output)
    except:
        return {"validation_raw": output}
