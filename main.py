import numpy as np

from modules.read_pdf import read_pdf, deskew, extract_text_from_image




if __name__ == "__main__":
    pdf_path = "Brayan_Alexis Lechón_Resume_10-04-2022-10-46-57.pdf"
    images = read_pdf(pdf_path)

    extracted_text = ""
    for page in images:
        preprocessed_image = deskew(np.array(page))
        text = extract_text_from_image(preprocessed_image)
        extracted_text += text

    print(extracted_text)
