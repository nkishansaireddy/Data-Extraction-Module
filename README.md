# OCR Data Extraction Module

**Ministry of New and Renewable Energy OCR Data Extraction Module**

This project is a Flask-based OCR (Optical Character Recognition) tool designed to extract text from images and PDF files. It features a modern, responsive UI built with Bootstrap, allowing users to upload multiple files, view extracted text in real time, and easily copy, download, or print the results.

## Features

- **Multiple File Uploads:** Supports images (PNG, JPG, JPEG) and PDF files.
- **Real-Time OCR:** Extracts text from uploaded files using Tesseract OCR.
- **User-Friendly Interface:** Modern UI with a full pink-themed Home Page and a full blue-themed Data Extraction Page.
- **Navigation:** Clear navigation with Home, About Us, Contact Us, and Data Extraction Tool pages.
- **Export Options:** Copy extracted text to clipboard, download as a text file (or PDF if extended), and print.
- **Responsive Design:** Works on both desktop and mobile devices.

## Project Structure

```
ocr_data_extraction/
├── app.py                  # Flask backend for handling routes and OCR extraction
├── requirements.txt        # List of required Python packages
├── templates/
│   ├── index.html          # Home Page (pink-themed)
│   ├── extract.html        # Data Extraction Page (blue-themed)
│   ├── about.html          # About Us Page
│   └── contact.html        # Contact Us Page
├── static/
│   ├── css/
│   │   └── styles.css      # Custom CSS for styling the pages
│   └── js/
│       └── script.js       # JavaScript for client-side interactivity (copy, download, etc.)
└── uploads/                # Directory to store uploaded files temporarily
```
