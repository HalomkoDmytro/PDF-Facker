from tkinter import filedialog
import tkinter as tk

from converter.img_to_pdf import images_to_pdf
from utills import remove_before_last_slash, remove_dimension, open_folder


class ImgToPDFUi(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.button_convert = None
        self.button_path = None
        self.label_path = None
        self.button = None
        self.button_open_destination = None
        self.label2 = None
        self.images_to_pdf = []

        label = tk.Label(self, text="Конвертувати зображення в ПДФ файл")
        label.pack(pady=10, padx=10)
        self.create_widgets()

    def create_widgets(self):
        self.label_path = tk.Label(self)
        self.label_path.pack(pady=20)

        self.button_path = tk.Button(self, text="Виберіть зображення", command=self.select_files)
        self.button_path.pack(pady=10)

        self.button_convert = tk.Button(self, text="Конвертувати", command=self.convert, bg='lightgreen')
        self.button_convert.pack(pady=10)

        self.button_open_destination = tk.Button(self, text="Відкрити папку Destination", command=open_folder, bg='lightblue')
        self.button_open_destination.pack(pady=10)

    def select_files(self):
        file_paths = filedialog.askopenfilenames(title="Зображення", filetypes=[("*.png", "*.jpg"), ("*.jpg", "*.jpeg")])
        if file_paths:
            self.images_to_pdf = []
            for file_path in file_paths:
                print(file_path)
                self.images_to_pdf.append(file_path)

    def convert(self):
        try:
            if len(self.images_to_pdf) > 0:
                file_name = remove_dimension(remove_before_last_slash(self.images_to_pdf[0]))
                self.label_path.config(text=f"Обробка ...")
                images_to_pdf(self.images_to_pdf, f"destination\\{file_name}.pdf")
                self.label_path.config(text=f"Файл в папці destination")
        except Exception:
            self.label_path.config(text=f"Ой! Сталася помилка")
