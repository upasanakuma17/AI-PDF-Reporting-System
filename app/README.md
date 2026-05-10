# AI-Powered PDF Reporting System

## Overview

An AI-powered document intelligence system built using Python, OCR, Streamlit, and LLM integration.

This system can:
- Extract text from PDFs
- Read scanned PDFs using OCR
- Generate structured JSON
- Perform AI-based extraction
- Generate automated PDF reports

---

## Features

- PDF Text Extraction
- OCR Processing
- AI-Powered Data Extraction
- JSON Generation
- Automated Report Generation
- Streamlit Dashboard
- Local LLM Integration using Ollama

---

## Tech Stack

- Python
- Streamlit
- PyMuPDF
- Tesseract OCR
- Ollama
- Llama3
- Pandas
- FPDF2

---

## Workflow

PDF Upload  
↓  
Text Extraction  
↓  
OCR Processing  
↓  
JSON Structuring  
↓  
AI Extraction  
↓  
Report Generation

---

## Run Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Ollama

```bash
ollama run llama3
```

### Run Dashboard

```bash
python -m streamlit run app/dashboard.py
```