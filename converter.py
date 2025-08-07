import argparse
from weasyprint import HTML

def convert_html_to_pdf(html_file, pdf_file):
    """
    Converts an HTML file to a PDF file.

    :param html_file: Path to the input HTML file.
    :param pdf_file: Path to the output PDF file.
    """
    print(f"Converting {html_file} to {pdf_file}...")
    base_url = '.' # Use current directory for relative paths in HTML
    HTML(filename=html_file, base_url=base_url).write_pdf(pdf_file)
    print("Conversion successful!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert an HTML file to a PDF file.")
    parser.add_argument("html_file", help="Path to the input HTML file.")
    parser.add_argument("pdf_file", help="Path to the output PDF file.")
    args = parser.parse_args()

    convert_html_to_pdf(args.html_file, args.pdf_file)
