import fitz  # PyMuPDF để mở và xử lý file PDF

# handlers/search_handler.py
class SearchHandler:
    def __init__(self, pdf_handler):
        self.pdf_handler = pdf_handler

    def search_and_highlight(self, keywords):
        """Tìm kiếm và highlight từ khóa trong bản sao của tài liệu PDF."""
        found_keywords = {}
        # Tạo bản sao của tài liệu gốc để thực hiện highlight
        doc_copy = fitz.open(self.pdf_handler.pdf_path)  # Tạo bản sao của file PDF gốc

        for keyword in keywords:
            keyword_cleaned = keyword.strip()  # Loại bỏ khoảng trắng thừa
            if not keyword_cleaned:
                continue
            found_keywords[keyword_cleaned] = []
            for page_num in range(len(doc_copy)):
                page = doc_copy.load_page(page_num)
                text_instances = page.search_for(keyword_cleaned)
                if text_instances:
                    # Thêm highlight cho từng từ khóa tìm thấy
                    for inst in text_instances:
                        page.add_highlight_annot(inst)
                    found_keywords[keyword_cleaned].append(page_num)
        
        # Trả về bản sao đã highlight thay vì tài liệu gốc
        return found_keywords, doc_copy  # Trả về cả kết quả tìm kiếm và bản sao của tài liệu
