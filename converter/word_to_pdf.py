
from docx2pdf import convert

from utills import remove_before_last_slash, remove_dimension


def word_to_pdf(file_path, folder="destination/"):
    to = remove_before_last_slash(file_path)
    to = remove_dimension(to)
    convert(file_path, folder + to + ".pdf")
    return to + ".pdf"

