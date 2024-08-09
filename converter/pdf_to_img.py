import pypdfium2 as pdfium
import os


def pdf_to_jpeg(pdf_path, output_folder=".\\destination"):
    pdf = pdfium.PdfDocument(pdf_path)
    os.makedirs(output_folder, exist_ok=True)

    for i in range(len(pdf)):
        page = pdf[i]

        bitmap = page.render(scale=2)  # Увеличьте значение scale для более высокого разрешения
        pil_image = bitmap.to_pil()
        rgb_image = pil_image.convert("RGB")
        image_path = os.path.join(output_folder, f"page_{i + 1}.jpg")
        rgb_image.save(image_path, "JPEG")

        print(f"Saved: {image_path}")

    pdf.close()



