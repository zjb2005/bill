from qreader import QReader
import cv2
from convert import Convert


class BillQreader:
    __imgLists: list = None
    __billLists: list = []

    def __init__(self, imagelist):
        self.__imgLists = imagelist

    def getBillReader(self):
        for imagList in self.__imgLists:
            print(imagList)
            qreader = QReader()
            qrcode_filename = imagList[1]
            qrcode_image = cv2.imread(qrcode_filename)
            # Get the image that contains the QR code
            image = cv2.cvtColor(qrcode_image, cv2.COLOR_BGR2RGB)
            # Use the detect_and_decode function to get the decoded QR data
            decoded_text = qreader.detect_and_decode(image=image)
            print(decoded_text)
            len1 = len(decoded_text)
            if len1<1:
                continue
            imagList.insert(2, decoded_text)
            self.__billLists.append(imagList)

    def getBillLists(self):
        return self.__billLists


def main():
    pdf_addr = 'D:\\pythonPro\\bill\\pdfaddr'
    save_addr = 'D:\\pythonPro\\bill\\saveaddr'
    ct = Convert(pdf_addr, save_addr)
    ct.convert_PdftoImage()
    ct_list = ct.list1

    sb = BillQreader(ct_list)
    sb.getBillReader()
    a = sb.getBillLists()
    print(a)


if __name__ == "__main__":
    main()
