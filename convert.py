import markdown
from weasyprint import HTML, CSS

# Configuration
input_file = "README.md"
output_file = "README.pdf"

def convert_md_to_pdf(md_file, pdf_file):
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
    except FileNotFoundError:
        print(f"Error: Could not find {md_file}")
        return

    # Convert Markdown to HTML
    html_body = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])

    # HTML Structure
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        {html_body}
    </body>
    </html>
    """

    # --- CSS FIX IS HERE ---
    # I added 'white-space: pre-wrap' and 'word-wrap: break-word' to the 'pre' tag.
    custom_css = CSS(string='''
        @page {
            size: A4;
            margin: 2cm;
        }
        body {
            font-family: Arial, sans-serif;
            font-size: 11pt;
            line-height: 1.6;
            color: #333;
        }
        h1, h2, h3 {
            color: #2c3e50;
            margin-top: 20px;
        }
        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 20px auto;
            border: 1px solid #ddd;
        }
        /* CODE BLOCK FIX */
        pre {
            background-color: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            border: 1px solid #e1e1e1;
            
            /* These 2 lines force text to wrap inside the border */
            white-space: pre-wrap; 
            word-wrap: break-word;
        }
        code {
            font-family: Consolas, "Courier New", monospace;
            font-size: 10pt;
            color: #d63384; /* Highlights code text slightly */
        }
        /* Table Styles */
        table {
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 20px;
            font-size: 10pt;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
            font-weight: bold;
        }
    ''')

    print("Generating PDF...")
    HTML(string=html_content, base_url='.').write_pdf(pdf_file, stylesheets=[custom_css])
    print(f"Success! Fixed PDF saved as {pdf_file}")

if __name__ == "__main__":
    convert_md_to_pdf(input_file, output_file)