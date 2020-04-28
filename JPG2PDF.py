import img2pdf
import sys
import os

imagelist = []                                                 # Contains the list of all images to be converted to PDF.

# --------------- USER INPUT -------------------- #
if len(sys.argv) != 3:
    print(sys.argv)
    print('Usage: python jpg2pdf.py <input-folder> <pdf-output-path>')
    exit(1)

folder = sys.argv[1]
pdf_dest = sys.argv[2]

# ------------- ADD ALL THE IMAGES IN A LIST ------------- #

for dirpath, dirnames, filenames in os.walk(folder):
    for filename in [f for f in filenames if f.endswith(".jpg")]:
        path = os.path.join(dirpath, filename)
        imagelist.append(path)

imagelist.sort()

print("\nFound " + str(len(imagelist)) + " image files. Converting to PDF....\n")

with open(pdf_dest, "wb") as f:
    f.write(img2pdf.convert(imagelist))

print("PDF generated successfully!\nOutputted to: ", pdf_dest) # TODO print output location.