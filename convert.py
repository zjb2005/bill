import fitz  # import the bindings
import glob

#
#
class Convert:
    pdf_address = None  # save pdf files
    image_address = None  # save image files
    list1: list = []

    def __init__(self, pdfAddr, imageAddr):
        self.pdf_address = pdfAddr
        self.image_address = imageAddr

    def convert_PdftoImage(self):
        path = self.pdf_address + '\\*.pdf'
        # print(path)
        files = glob.glob(path)
        i = 0
        for file in files:
            print(file)
            list2 = []
            list2.append(file)
            doc = fitz.open(file)  # open document
            for page in doc:  # iterate through the pages
                pix = page.get_pixmap()  # render page to an image
                i += 1
                imgFileName = f'{self.image_address}\\{i}.png'
                list2.append(imgFileName)
                # print(imgFileName)
                pix.save(imgFileName)  # store image as a PNG
            self.list1.append(list2)


    def getConvert(self):
        return self.list1


def main():
    pdf_addr = 'D:\\pythonPro\\bill\\pdfaddr'
    save_addr = 'D:\\pythonPro\\bill\\saveaddr'
    conv = Convert(pdf_addr, save_addr)
    conv.convert_PdftoImage()
    a = conv.getConvert()
    print(a)

if __name__ == "__main__":
    main()
