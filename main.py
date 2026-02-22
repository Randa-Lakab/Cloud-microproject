from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import base64
import fitz  # PyMuPDF
from typing import List

app = FastAPI(title="Cloud Computing Micro Project API")


# Request Models

class EmbedRequest(BaseModel):
    main_pdf: str              # base64
    pdfs_to_embed: List[str]   # list of base64 PDFs


class ExtractRequest(BaseModel):
    pdf: str  # base64

# Endpoint 1: Embed PDFs

@app.post("/create_embedded_pdf")
def create_embedded_pdf(request: EmbedRequest):

    try:
        main_pdf_bytes = base64.b64decode(request.main_pdf)
        main_doc = fitz.open(stream=main_pdf_bytes, filetype="pdf")

        for i, pdf_base64 in enumerate(request.pdfs_to_embed):
            embedded_bytes = base64.b64decode(pdf_base64)
            main_doc.embfile_add(
                f"embedded_{i}.pdf",
                embedded_bytes
            )

        result_bytes = main_doc.write()
        main_doc.close()

        result_base64 = base64.b64encode(result_bytes).decode("utf-8")

        return {"embedded_pdf": result_base64}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint 2: Extract PDFs

@app.post("/extract_embedded_pdf")
def extract_embedded_pdf(request: ExtractRequest):

    try:
        pdf_bytes = base64.b64decode(request.pdf)
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")

        extracted_pdfs = []

        for i in range(doc.embfile_count()):
            info = doc.embfile_info(i)
            embedded_data = doc.embfile_get(i)
            encoded = base64.b64encode(embedded_data).decode("utf-8")

            extracted_pdfs.append({
                "filename": info["filename"],
                "content": encoded
            })

        doc.close()

        return {"extracted_pdfs": extracted_pdfs}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))