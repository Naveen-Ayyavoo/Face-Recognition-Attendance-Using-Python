import os
import pandas as pd

# Define the XLSX input file variable
XLSX_INPUT_FILE = "IT_Attendance_2025-05-19.xlsx"

# Set output folder and file name
OUTPUT_FOLDER = "attendance_reports"
OUTPUT_PDF_FILE = os.path.join(OUTPUT_FOLDER, os.path.splitext(XLSX_INPUT_FILE)[0] + ".pdf")

def excel_to_dataframe(xlsx_filename=XLSX_INPUT_FILE):
    return pd.read_excel(xlsx_filename)

def export_to_pdf(output_filename=OUTPUT_PDF_FILE):
    import pdfkit
    from pdfkit.configuration import Configuration
    # Ensure output folder exists
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)
    df = excel_to_dataframe()
    course = df['Course'].iloc[0] if 'Course' in df.columns else ''
    date = df['Date'].iloc[0] if 'Date' in df.columns else ''
    df = df.drop(columns=[col for col in ['Course', 'Date'] if col in df.columns])
    style = """
    <style>
        body { 
        font-size: 20pt; 
        font-family: Arial, sans-serif; 
        }

        h2 { 
        font-size: 22pt; 
        text-align: center; 
        }

        p { 
        font-size: 18pt; 
        text-align: center; 
        }

        table { 
        border: 1px solid black; 
        border-collapse: collapse; 
        width: 100%; 
        table-layout: auto; 
        }
        
        th, td { 
        border: 1px solid black; 
        padding: 7px; 
        text-align: center; 
        white-space: nowrap; 
        font-size: 16pt; 
        }
    </style>
    """
    heading = f'<h2>Attendance Report</h2><p>Course: {course} &nbsp;&nbsp; Date: {date}</p>'
    html = style + heading + df.to_html(index=False, border=0)
    config = Configuration(wkhtmltopdf=r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    options = {'page-size': 'A4'}
    pdfkit.from_string(html, output_filename, configuration=config, options=options)
    print(f"✅ PDF report saved as {output_filename}")

if __name__ == "__main__":
    export_to_pdf()