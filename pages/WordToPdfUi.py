import tkinter as tk
from tkinter import filedialog

from converter.img_to_pdf import images_to_pdf
from converter.pdf_to_img import pdf_to_jpeg
from converter.word_to_pdf import word_to_pdf
from utills import remove_before_last_slash, open_folder, delete_all_files_in_folder_with_extension, \
    get_file_paths_with_extension, remove_dimension, delete_all_files_in_folder


class WordToPdfUi(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.button_path = None
        self.button_convert = None
        self.label_path = None
        self.file_path = None
        self.button_open_destination = None
        self.checkbox = None
        self.checkbox_var = None
        label = tk.Label(self)
        label.pack(pady=10, padx=10)

        self.create_widgets()

    def create_widgets(self):
        self.label_path = tk.Label(self, text="файл: ")
        self.label_path.pack(pady=20)

        self.button_path = tk.Button(self, text="Виберіть Word документ", command=self.open_file_dialog)
        self.button_path.pack(pady=10)

        self.button_convert = tk.Button(self, text="Конвертувати", command=self.convert, bg='lightgreen')
        self.button_convert.pack(pady=10)

        self.checkbox_var = tk.IntVar()
        self.checkbox = tk.Checkbutton(self, variable=self.checkbox_var, text="Як зображення")
        self.checkbox.pack(pady=10)

        self.button_open_destination = tk.Button(self, text="Відкрити папку Destination", command=open_folder, bg='lightblue')
        self.button_open_destination.pack(pady=10)

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(
            title="Виберіть Word документ",
            filetypes=[("Word документи", "*.doc"), ("Word документи", "*.docx")]
        )
        if file_path:
            self.file_path = file_path
            self.label_path.config(text=f"Файл: {remove_before_last_slash(file_path)}")

    def convert(self):
        if self.checkbox_var.get():
            self.convert_with_img()
        elif self.file_path and self.file_path != '':
            try:
                self.label_path.config(text=f"Обробка ...")
                word_to_pdf(self.file_path)
                self.label_path.config(text=f"Файл в папці destination")
            except Exception as e:
                self.label_path.config(text=f"Ой! Сталася помилка {e}")

    def convert_with_img(self):
        if self.file_path and self.file_path != '':
            try:
                new_pdf_file_name = remove_dimension(remove_before_last_slash(self.file_path))

                self.label_path.config(text=f"Обробка ...")
                temp_pdf = word_to_pdf(self.file_path, "temp/")

                self.label_path.config(text=f"Обробка зображення ...")
                pdf_to_jpeg("temp/" + temp_pdf, "temp")
                delete_all_files_in_folder_with_extension("temp", ".pdf")

                self.label_path.config(text=f"Обробка в пдф ...")
                jpegs = get_file_paths_with_extension(".\\temp", ".jpg")
                images_to_pdf(jpegs, f".\\destination\\{new_pdf_file_name}.pdf")

                delete_all_files_in_folder(".\\temp")
            except Exception as e:
                self.label_path.config(text=f"Ой! Сталася помилка {e}")

