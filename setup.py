from cx_Freeze import setup, Executable
import numpy
import os

numpy_path = os.path.dirname(numpy.__file__)

build_exe_options = {
    "packages": ["os", "fpdf", "PIL", "tkinter", "pypdfium2", "docx2pdf", "PyPDF2", "numpy"],
    "includes": [],
    "include_files": [(numpy_path, "numpy")]
}

executables = [Executable("main.py", base="Win32GUI")]
# executables = [Executable("main.py", base=None)]

setup(
    name="PDF Facker",
    version="0.1",
    description="Утиліта для конвертації ПДФ",
    options={"build_exe": build_exe_options},
    executables=executables
)

# run in console to start generate exe: python setup.py build
