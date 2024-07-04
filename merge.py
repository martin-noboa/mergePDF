import pymupdf
import sys
from os import listdir, getcwd
from os.path import isfile, join, splitext

# Error codes
# -1 = Fail to read input filename
# -2 = Fail to retrieve filepaths
# -3 = Fail to merge pdfs

def getOutputFilename():
    try:
        output = sys.argv[1] + ".pdf"
        return output
    except:
        return -1

def getFiles():
    try:
        cwd = getcwd()
        files = [f for f in listdir(cwd) if isfile(join(cwd, f)) and splitext(f)[1].lower() == '.pdf']
        if not files:
            return []
        return files
    except:
        return -2
    
def merge(files,finalPDF):
    try:
        output =  pymupdf.open(files[0])
        for file in files[1:]:
            append = pymupdf.open(file)
            output.insert_pdf(append)
        output_path = join(getcwd(), finalPDF)
        output.save(output_path)
        return 0  # Success
    except:
        return -3



def main():
    output = getOutputFilename()
    print(output)
    if output == -1:
        return -1
    files = getFiles()
    if files == -2:
        return -2
    result = merge(files,output)
    if result == -3:
        return -3
    
if __name__ == "__main__":
    main()
