import glob
from pypdf import PdfWriter

files_list = glob.glob("*.pdf")
merger = PdfWriter()

for pdf in files_list:
    merger.append(pdf)

merger.write("output.pdf")
merger.close()
