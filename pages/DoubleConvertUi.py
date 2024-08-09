from tkinter import filedialog
import tkinter as tk

from converter.img_to_pdf import images_to_pdf
from converter.pdf_to_img import pdf_to_jpeg
from utills import remove_before_last_slash, remove_dimension, get_file_paths_with_extension, \
    delete_all_files_in_folder, open_folder


class DoubleConvertUi(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.file_path = None
        self.button_convert = None
        self.button_path = None
        self.label_path = None
        self.button_open_destination = None
        label = tk.Label(self,
                          text="Щоб текст в документі не розпізнавався як ТЕКСТ конвертувати "
                               "\nпдф в картинку, а потім назад в пдф.")
        label.pack(pady=10, padx=10)

        self.create_widgets()

    def create_widgets(self):
        self.label_path = tk.Label(self, text="файл: ")
        self.label_path.pack(pady=20)

        self.button_path = tk.Button(self, text="Виберіть Pdf документ", command=self.open_file_dialog)
        self.button_path.pack(pady=10)

        self.button_convert = tk.Button(self, text="Конвертувати", command=self.convert, bg='lightgreen')
        self.button_convert.pack(pady=10)

        self.button_open_destination = tk.Button(self, text="Відкрити папку Destination", command=open_folder, bg='lightblue')
        self.button_open_destination.pack(pady=10)

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(
            title="Виберіть Pdf документ",
            filetypes=[("Pdf документи", "*.pdf")]
        )
        if file_path:
            self.file_path = file_path
            self.label_path.config(text=f"Файл: {remove_before_last_slash(file_path)}")

    def convert(self):
        if self.file_path and self.file_path != '':
            try:
                self.label_path.config(text=f"Конвертація в картинку ...")
                pdf_to_jpeg(self.file_path, "./temp")

                self.label_path.config(text=f"Конвертація в пдф ...")
                new_pdf_file_name = remove_dimension(remove_before_last_slash(self.file_path))
                jpegs = get_file_paths_with_extension(".\\temp", ".jpg")
                images_to_pdf(jpegs, f".\\destination\\{new_pdf_file_name}.pdf")

                delete_all_files_in_folder(".\\temp")

                self.label_path.config(text=f"Файл в папці destination")
            except Exception:
                self.label_path.config(text=f"Ой! Сталася помилка")

