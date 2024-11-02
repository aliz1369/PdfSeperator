from pypdf import PdfReader,PdfWriter

def split_pdf(input_pdf_path, output_pdf_path,start_page,end_page):
   input_pdf = PdfReader(input_pdf_path)
   output_pdf = PdfWriter()

   for i in range(start_page -1 , end_page):
      output_pdf.add_page(input_pdf.pages[i])
   with open(output_pdf_path,"wb") as output_file:
      output_pdf.write(output_file)

   print(f"PDF pages {start_page} to {end_page} saved as {output_pdf_path}")
      
def rotate_pdf(input_pdf_path,output_pdf_path,degree):
   input_pdf = PdfReader(input_pdf_path)
   output_pdf = PdfWriter()
   totalPages = len(input_pdf.pages)

   for i in range(0,totalPages):
      output_pdf.add_page(input_pdf.pages[i])
      output_pdf.pages[i].rotate(degree)

   with open(output_pdf_path,"wb") as output_file:
      output_pdf.write(output_file)
   print(f"PDF rotate with {degree} degree")


print(f"1:To split Pdf")   
print(f"2:To rotate Pdf")   
input_function_selector = int(input("Enter The Function:"))
if input_function_selector == 1:
   input_pdf_path = input("Enter pdf name:")
   output_pdf_path = input("Enter output name:")
   start_page = int(input("Enter Start Page:"))  # Example start page
   end_page = int(input("Enter End Page:"))     # Example end page
   split_pdf(input_pdf_path, output_pdf_path, start_page, end_page,-90)
elif input_function_selector == 2:
   input_pdf_path = input("Enter pdf name:")
   output_pdf_path = input("Enter output name:")
   rotate_degree = int(input("Enter rotate degree:"))
   rotate_pdf(input_pdf_path, output_pdf_path,rotate_degree)



