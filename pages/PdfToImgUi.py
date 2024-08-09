import tkinter as tk
from tkinter import filedialog

from converter.pdf_to_img import pdf_to_jpeg
from utills import remove_before_last_slash, open_folder


class PdfToImgUI(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.file_path = None
        self.button_convert = None
        self.button_path = None
        self.label_path = None
        self.button_open_destination = None
        label = tk.Label(self, text="Конвертувати PDF в jpeg")
        label.pack(pady=10, padx=10)

        self.create_widgets()

    def create_widgets(self):
        self.label_path = tk.Label(self, text="файл: ")
        self.label_path.pack(pady=20)

        self.button_path = tk.Button(self, text="Виберіть Pdf документ", command=self.open_file_dialog)
        self.button_path.pack(pady=10)

        self.button_convert = tk.Button(self, text="Конвертувати", command=self.convert, bg='lightgreen')
        self.button_convert.pack(pady=10)

        self.button_open_destination = tk.Button(self, text="Відкрити папку Destination", command=open_folder,
                                                 bg='lightblue')
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
                pdf_to_jpeg(self.file_path, "./destination")

                self.label_path.config(text=f"Файл в папці destination")
            except Exception:
                self.label_path.config(text=f"Ой! Сталася помилка")