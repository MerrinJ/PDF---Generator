import pytest
from fastapi.testclient import TestClient
from app.main import app  

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_create_pdf_success():
    data = {
        "heading": "Test Heading",
        "subheading": "Test Subheading",
        "table": [["Header1", "Header2"], ["Row1Col1", "Row1Col2"]]
    }
    response = client.post("/generate-pdf", json=data)
    assert response.status_code == 200
    json_response = response.json()
    assert "url" in json_response
    assert json_response["url"].startswith("http://127.0.0.1:8000/generated_pdfs/")
    
def test_create_pdf_invalid_data():
    data = {
        "heading": "",
        "subheading": "Test Subheading",
        "table": [["Header1", "Header2"], ["Row1Col1", "Row1Col2"]]
    }
    response = client.post("/generate-pdf", json=data)
    assert response.status_code == 400
    assert "Value error: Heading must be a non-empty string" in response.json()["detail"]



if __name__ == "__main__":
    pytest.main()
