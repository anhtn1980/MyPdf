# handlers/pdf_handler.py
import fitz  # PyMuPDF
from PIL import Image

class PDFHandler:
    def __init__(self, pdf_path=None):
        self.pdf_path = pdf_path
        self.doc = None
        self.original_doc = None  # Lưu trữ bản gốc của tài liệu PDF
        if pdf_path:
            self.open_pdf(pdf_path)
    
    def open_pdf(self, pdf_path):
        """Mở file PDF và lưu đối tượng doc."""
        self.pdf_path = pdf_path
        self.doc = fitz.open(pdf_path)
        # Lưu bản gốc của tài liệu ngay khi mở để sử dụng khi undo
        self.original_doc = fitz.open(pdf_path)  # Lưu lại bản gốc của file PDF

    def convert_to_images(self):
        """Chuyển các trang PDF thành hình ảnh."""
        images = []
        for page_num in range(len(self.doc)):
            page = self.doc.load_page(page_num)
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            images.append(img)
        return images

    def save_pdf(self, save_path):
        """Lưu file PDF đã highlight hoặc bản gốc sau khi undo."""
        if self.doc:
            self.doc.save(save_path)

    def restore_original(self):
        """Khôi phục tài liệu về trạng thái ban đầu (không có highlight)."""
        if self.original_doc:
            # Đóng tài liệu hiện tại và thay thế bằng bản gốc
            self.doc.close()
            self.doc = fitz.open(self.pdf_path)  # Mở lại bản gốc từ đường dẫn ban đầu
