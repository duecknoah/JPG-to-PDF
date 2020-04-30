import img2pdf
import sys
import os
import re

imagelist = []                                                 # Contains the list of all images to be converted to PDF.

# --------------- USER INPUT -------------------- #
if len(sys.argv) != 3:
    print(sys.argv)
    print('Usage: python jpg2pdf.py <input-folder> <pdf-output-path>')
    exit(1)

folder = sys.argv[1]
pdf_dest = sys.argv[2]

# Ascii to integer, attempts to convert the string to an int, else returns string
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    Snippet from stackoverflow
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

# ------------- ADD ALL THE IMAGES IN A LIST ------------- #

for dirpath, dirnames, filenames in os.walk(folder):
    for filename in [f for f in filenames if f.endswith(".jpg")]:
        path = os.path.join(dirpath, filename)
        imagelist.append(path)

imagelist.sort(key=natural_keys)

print("\nFound " + str(len(imagelist)) + " image files. Converting to PDF....\n")

with open(pdf_dest, "wb") as f:
    f.write(img2pdf.convert(imagelist))

print("PDF generated successfully!\nOutputted to: ", pdf_dest) # TODO print output location.