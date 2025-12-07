
---

# ✅ **FILE 5: `src/main.py`**
```python
import os
from src.utils.pdf_reader import extract_text_from_pdf
from src.agents.extraction_agent import extract_adr_from_text
from src.agents.validation_agent import validate_adr_report
from src.rag.vectorstore import SimpleVectorStore

SAMPLE_TEXT = """
Patient reported dizziness and nausea after taking DrugX. Another patient
experienced severe rash and swelling suspected to be due to DrugY. Mild
headache in a small cohort was also reported with DrugX.
"""

def run_pipeline_from_text(text: str):
    print("=== Running ADR Extraction ===")
    extraction = extract_adr_from_text(text)
    print("Extraction Result:\n", extraction)

    print("\n=== Running ADR Validation ===")
    validation = validate_adr_report(extraction)
    print("Validation Result:\n", validation)

    print("\n=== Indexing Input Text in Vector Store ===")
    store = SimpleVectorStore()

    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    store.add_texts(chunks)

    print("\nVector Search Example (query='severe rash'):")
    print(store.search("severe rash", k=2))


if __name__ == "__main__":
    pdf_path = os.path.join("data", "sample.pdf")

    if os.path.exists(pdf_path):
        content = extract_text_from_pdf(pdf_path)
    else:
        content = SAMPLE_TEXT

    run_pipeline_from_text(content)
