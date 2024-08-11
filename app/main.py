from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator
from fastapi.responses import JSONResponse
from typing import List, Union
import logging

# Import the generate_pdf function from pdf_service
from app.pdf import generate_pdf, SAVE_DIR

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define the base URL of your server
BASE_URL = "http://127.0.0.1:8000"

# Define Pydantic model for input data
class TableData(BaseModel):
    heading: str 
    subheading: str 
    table: List[List[Union[str, int]]] 

    @field_validator('table')
    def check_table_data(cls, table):
        if not table or not all(isinstance(row, list) for row in table):
            raise ValueError("Table must be a list of lists")
        if not all(isinstance(cell, (str, int)) for row in table for cell in row):
            raise ValueError("All cells in the table must be strings or integers")
        return table

@app.get("/")
async def root():
    logging.info("Root endpoint accessed")
    return {"message": "Hello, World!"}

@app.post("/generate-pdf")
async def create_pdf(data: TableData):
    logging.info("Received request for PDF generation")

    try:
        pdf_url = generate_pdf(data.heading, data.subheading, data.table, BASE_URL)
        logging.info(f"PDF URL: {pdf_url}")
        return JSONResponse(content={"url": pdf_url})
    
    except ValueError as ve:
        logging.error(f"Value error: {ve}")
        raise HTTPException(status_code=400, detail=f"Value error: {ve}")
    except Exception as e:
        logging.error(f"Error generating PDF: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Serve the generated PDFs
from fastapi.staticfiles import StaticFiles
app.mount("/generated_pdfs", StaticFiles(directory=SAVE_DIR), name="generated_pdfs")
