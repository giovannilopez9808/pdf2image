# import module
from pdf2image import convert_from_path
from sys import argv
# Store Pdf with convert_from_path function
filename = argv[2]
filename_image = filename.replace(
    ".pdf", ".jpg"
)
document = convert_from_path(
    filename
)
document = document[-1]
document.save(
    filename_image,
    "JPEG",
)
