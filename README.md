# website_ada_convert_pdf

Convert Website PDFs to text files.  I am developing this for our school district website, but other may find this helpful for managing their own website.

Install poppler
https://github.com/oschwartz10612/poppler-windows/releases/

Add to system path

## Step 1: Install the Tesseract Engine

If you haven't already installed the actual software (not just the Python library):

Download the installer from a reputable source like https://github.com/UB-Mannheim/tesseract/wiki.

Run the .exe installer.

Note the installation path. By default, it is usually:
C:\Program Files\Tesseract-OCR\tesseract.exe

Step 2: Add to System PATH (Recommended)

Search Windows for "Edit the system environment variables".

Click Environment Variables.

Under System Variables, find Path, click Edit, then New.

Paste the folder path: C:\Program Files\Tesseract-OCR

Click OK on all windows and restart your IDE (VS Code, PyCharm, etc.).

Step 3: The "Quick Fix" (Code-based)

If you don't want to mess with system settings or the PATH isn't updating, you can point to the .exe directly in your Python script.

import pytesseract
from PIL import Image

# 1. Point to the specific location of the tesseract executable
# Change this path if you installed Tesseract somewhere else
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 2. Now run your OCR logic
try:
    text = pytesseract.image_to_string(Image.open('your_image.png'))
    print(text)
except Exception as e:
    print(f"Error: {e}")


Troubleshooting

Permission Error: Ensure you are running your terminal/IDE as Administrator if you installed Tesseract in a protected folder.

Language Data: If you are scanning non-English text, ensure you checked the "Additional script/language data" boxes during the Tesseract installation.

## Run On Windows powershell

```!
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
..\venv\Scripts\activate
```
