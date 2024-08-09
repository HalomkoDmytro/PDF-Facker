from fpdf import FPDF
from PIL import Image


def images_to_pdf(image_paths, output_pdf_path="..\\destination\\pdf_from_img.pdf"):
    pdf = FPDF()

    for image_path in image_paths:
        image = Image.open(image_path)

        width, height = image.size

        width_mm = width * 0.264583
        height_mm = height * 0.264583

        pdf.add_page(format=(width_mm, height_mm))
        pdf.image(image_path, 0, 0, width_mm, height_mm)

    pdf.output(output_pdf_path)
