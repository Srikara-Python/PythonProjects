import PyPDF2
from datetime import datetime



def get_time():
    # datetime object containing current date and time
    now = datetime.now()
    
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
    
    return dt_string

def count_pages(p):
    try:
        with open(p,'rb') as mypdf:
            reader = PyPDF2.PdfFileReader(mypdf)
            return reader.numPages
    except IOError:
        return "File Not Found"

def get_page(file_name, page):
    try:
        with open(file_name, 'rb') as mypdf:
            reader = PyPDF2.PdfFileReader(mypdf)
            return reader.getPage(page)
    except IOError:
        return "File Not Found"

def rotate_page(file_name, rotation):
    try:
        with open(file_name, 'rb') as mypdf:
            reader = PyPDF2.PdfFileReader(mypdf)
            writer = PyPDF2.PdfFileWriter()

            # Rotate every page
            for pagenum in range(reader.numPages):
                page = reader.getPage(pagenum)
                page.rotateClockwise(rotation)
                writer.addPage(page)
            
            pdf_out = open(f'output/rotated-file.pdf', 'wb')
            with open(f'output/rotated-file.pdf', 'wb') as out_file:
                writer.write(pdf_out)

            return "File Rotated"
    except IOError:
        return "File Not Found"

def merge_files(pdf_list):
    try:
        merger = PyPDF2.PdfFileMerger()
        
        for pdf in pdf_list:
            conc = "pdfs/"+pdf
            merger.append(conc)
        
        merger.write("output/merged.pdf")
        return "Files Merged"
    except IOError:
        return "File Not Found"

def water_mark(file_name, wtr):
    try:
        template  = PyPDF2.PdfFileReader(open(file_name,'rb'))
        watermark = PyPDF2.PdfFileReader(open(wtr,'rb'))
        output    = PyPDF2.PdfFileWriter()

        for p in range(template.getNumPages()):
            page = template.getPage(p)
            page.mergePage(watermark.getPage(0))
            output.addPage(page)

        # write file
        with open(f'output/watermarked-{get_time()}.pdf', 'wb') as file:
            output.write(file)

        return "File Water Marked"

    except IOError:
        return "File Not Found"

def pdf_to_word(p):
    try:
        pass
    except IOError:
        return "File Not Found"



file_name = 'pdfs/dummy.pdf'
file_list = ['first.pdf','second.pdf','dummy.pdf']
wtr = 'pdfs/wtr.pdf'
# print(count_pages(file_name))

# print(get_page(file_name,2))

# print(rotate_page(file_name,180))

# print(merge_files(file_list))

print(water_mark(file_name, wtr))