# main.py
import tkinter as tk
from handlers.pdf_handler import PDFHandler
from handlers.search_handler import SearchHandler
from ui.ui_handler import PDFViewerUI

# Khởi tạo ứng dụng
root = tk.Tk()
root.title("PDF Viewer")
root.geometry("1200x700")  # Kích thước cửa sổ lớn để dễ quan sát

# Khởi tạo các đối tượng chính
pdf_handler = PDFHandler()
search_handler = SearchHandler(pdf_handler)
ui = PDFViewerUI(root, pdf_handler, search_handler)

# Vòng lặp chính của ứng dụng
root.mainloop()
