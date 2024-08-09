import tkinter as tk
from tkinter import filedialog

from converter.merge_pdf import merge_pdfs
from utills import open_folder


class MergePdfUi(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.to_merge = []
        self.button_path = None
        self.label_path = None
        self.button_convert = None
        self.button_open_destination = None
        self.button_counter = 0
        label = tk.Label(self, text="Обэднати декілька ПДФ файлів")
        label.pack(pady=10, padx=10)

        self.create_widgets()

    def create_widgets(self):
        self.label_path = tk.Label(self)
        self.label_path.pack(pady=20)

        self.button_path = tk.Button(self, text="Виберіть Pdf документ", command=self.select_files)
        self.button_path.pack(pady=10)

        self.button_convert = tk.Button(self, text="Конвертувати", command=self.convert, bg='lightgreen')
        self.button_convert.pack(pady=10)

        self.button_open_destination = tk.Button(self, text="Відкрити папку Destination", command=open_folder, bg='lightblue')
        self.button_open_destination.pack(pady=10)

    def select_files(self):
        file_paths = filedialog.askopenfilenames(title="Выберите файлы", filetypes=[("PDF files", "*.pdf")])
        if file_paths:
            print("Выбранные файлы:")
            self.to_merge = []
            for file_path in file_paths:
                print(file_path)
                self.to_merge.append(file_path)

    def convert(self):
        try:
            if len(self.to_merge) > 1:
                self.label_path.config(text=f"Обробка ...")
                merge_pdfs(self.to_merge, "destination\\Обєданний додаток.pdf")
                self.label_path.config(text=f"Файл в папці destination")
        except Exception:
            self.label_path.config(text=f"Ой! Сталася помилка")
