import os
import pdfplumber
import docx
from google import genai

# Set your GENAI API key
API_KEY = "AIzaSyCdt8KI-skUdTXN8oNq7JfMRVD3IeQnQfA"

def extract_text_from_pdf(file_path):
    """Extracts text from a PDF file."""
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

def extract_text_from_docx(file_path):
    """Extracts text from a DOCX file."""
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs]).strip()

def analyze_cv(cv_text):
    """Sends CV text to OpenAI GPT-4.0 for analysis."""
    prompt = f"""
    You are an expert AI recruiter analyzing a candidate's CV in IT, software engineering, data analytics and computer science fields. 

    1. Identify and categorize the candidate's experience into fields (e.g., Software Engineering, Lecturer, Business, Finance).
    2. Suggest the main two areas of the candidate's expertise and the most relevant job roles based on the experience.
    3. Provide recommendations for improving the CV in three bullet points.

    CV Text:
    {cv_text}
    """

    client = genai.Client(api_key=API_KEY)

    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=prompt
    )
    print(response.text)
    return response.text

if __name__ == "__main__":
    file_path = input("Enter CV file path (PDF/DOCX): ").strip()

    if not os.path.exists(file_path):
        print("File not found!")
        exit()

    # Extract text based on file type
    if file_path.endswith(".pdf"):
        cv_text = extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        cv_text = extract_text_from_docx(file_path)
    else:
        print("Unsupported file format!")
        exit()

    print("\nAnalyzing CV with GEMINI...\n\n ", cv_text,"\n\n")
    analysis_result = analyze_cv(cv_text)
    
    print("\n--- CV Analysis Results ---\n")
    print(analysis_result)
