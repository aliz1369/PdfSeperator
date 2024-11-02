from pypdf import PdfReader,PdfWriter

def split_pdf(input_pdf_path, output_pdf_path,start_page,end_page):
   input_pdf = PdfReader(input_pdf_path)
   output_pdf = PdfWriter()

   for i in range(start_page -1 , end_page):
      output_pdf.add_page(input_pdf.pages[i])
   with open(output_pdf_path,"wb") as output_file:
      output_pdf.write(output_file)

   print(f"PDF pages {start_page} to {end_page} saved as {output_pdf_path}")
      

input_pdf_path = input("Enter pdf name:")
output_pdf_path = input("Enter output name:")
start_page = int(input("Enter Start Page:"))  # Example start page
end_page = int(input("Enter End Page:"))     # Example end page

split_pdf(input_pdf_path, output_pdf_path, start_page, end_page)



