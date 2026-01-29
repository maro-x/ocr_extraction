from importnb import Notebook

with Notebook():
    from notebooks.ocr import get_invoice_data




if __name__ == '__main__':
    
    invoice_data = get_invoice_data("C:/Users/DELL/OneDrive/Desktop/FA.jpg")
    invoice_data
