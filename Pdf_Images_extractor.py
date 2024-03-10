# install this library first
# pip install PyMuPDF

import fitz  # PyMuPDF

def extract_images_from_pdf(pdf_path, image_folder):
    # Open the PDF
    pdf_document = fitz.open(pdf_path)
    
    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        
        # Get the images on the page
        image_list = page.get_images(full=True)
        
        # Iterate through each image on the page
        for img_index, img_info in enumerate(image_list):
            # Get the XREF of the image
            xref = img_info[0]
            
            # Extract the image
            base_image = pdf_document.extract_image(xref)
            
            # Get the image extension
            image_ext = base_image["ext"]
            
            # Save the image to the output folder
            image_path = f"{image_folder}/page{page_num+1}_image{img_index}.{image_ext}"
            with open(image_path, "wb") as image_file:
                image_file.write(base_image["image"])
                
    # Close the PDF
    pdf_document.close()

# Example usage
pdf_file_path = "PDF_Files/test.pdf"
output_image_folder = "extracted_images"
extract_images_from_pdf(pdf_file_path, output_image_folder)
