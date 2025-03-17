from flask import Flask, render_template, request, jsonify, send_file
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os
from fpdf import FPDF

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Set Tesseract OCR path (Change if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/extract", methods=["POST"])
def extract_text():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    extracted_text = ""
    
    try:
        if file.filename.lower().endswith((".png", ".jpg", ".jpeg")):
            image = Image.open(filepath)
            extracted_text = pytesseract.image_to_string(image)
        elif file.filename.lower().endswith(".pdf"):
            images = convert_from_path(filepath)
            for img in images:
                extracted_text += pytesseract.image_to_string(img) + "\n"
        else:
            return jsonify({"error": "Unsupported file type"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"text": extracted_text})

@app.route("/download-pdf", methods=["POST"])
def download_pdf():
    text = request.form.get("text")
    
    if not text:
        return jsonify({"error": "No text to download"}), 400
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)

    pdf_path = os.path.join(app.config["UPLOAD_FOLDER"], "extracted_text.pdf")
    pdf.output(pdf_path)

    return send_file(pdf_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)