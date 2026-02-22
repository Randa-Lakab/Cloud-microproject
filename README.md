# Cloud Computing Micro Project

##  Description
This project is a Web API built with FastAPI for manipulating PDFs in binary format.

It provides two endpoints:

- `create_embedded_pdf` → Embed multiple PDFs inside a main PDF
- `extract_embedded_pdf` → Extract all embedded PDFs from a PDF

Swagger documentation is automatically generated.

---

##  Technologies Used
- Python
- FastAPI
- Uvicorn
- PyMuPDF

---

##  How to Run

###  Install dependencies
```bash
pip install -r requirements.txt
```
### Run the server
```bash
uvicorn main:app --reload
```

### Open Swagger
```bash
http://127.0.0.1:8000/docs
```"# Cloud-microproject" 
