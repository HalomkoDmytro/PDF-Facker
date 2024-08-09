import logging
import sys
import tkinter as tk
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
from tkinter import ttk

from LoggerWriter import LoggerWriter
from pages.DoubleConvertUi import DoubleConvertUi
from pages.ImgToPDFUi import ImgToPDFUi
from pages.MergePdfUi import MergePdfUi
from pages.PdfToImgUi import PdfToImgUI
from pages.WordToPdfUi import WordToPdfUi

# Create Logger if doesn't exist
Path("log").mkdir(parents=True, exist_ok=True)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler = TimedRotatingFileHandler('log/error.log', when="midnight", interval=1, encoding='utf8')
handler.suffix = "%Y-%m-%d"
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logging.ERROR)
logger.addHandler(handler)
sys.stdout = LoggerWriter(logging.debug)
sys.stderr = LoggerWriter(logging.warning)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.notebook = None
        self.page_three = None
        self.page_pdf_to_img = None
        self.page_two_frame = None
        self.img_to_pdf = None
        self.home_frame = None
        self.title("PDF facker")
        self.geometry("500x400")

        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self, style='TNotebook')
        self.notebook.pack(fill='both', expand=True)

        self.home_frame = WordToPdfUi(self.notebook)
        self.img_to_pdf = ImgToPDFUi(self.notebook)
        self.page_two_frame = DoubleConvertUi(self.notebook)
        self.page_three = MergePdfUi(self.notebook)
        self.page_pdf_to_img = PdfToImgUI(self.notebook)

        self.notebook.add(self.home_frame, text='WORD в PDF')
        self.notebook.add(self.img_to_pdf, text='Зображення в ПДФ')
        self.notebook.add(self.page_two_frame, text='Подвійна конвертація')
        self.notebook.add(self.page_three, text='Зєднати ПДФ')
        self.notebook.add(self.page_pdf_to_img, text='PDF в jpeg')


if __name__ == "__main__":
    app = App()
    app.mainloop()
