import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog, Canvas, messagebox
from PIL import ImageTk
from ui.menu_handler import create_menu
from ui.common_widgets import open_pdf, save_highlighted_pdf, next_page, prev_page
from ui.help_handler import show_about, show_guide  # Import các chức năng từ module help_handler

class PDFViewerUI:
    def __init__(self, root, pdf_handler, search_handler):
        self.root = root
        self.pdf_handler = pdf_handler
        self.search_handler = search_handler
        self.current_page = 0
        self.pdf_images = []
        self.save_folder_path = None  # Thư mục lưu file đã tô màu

        # Đặt tiêu đề cho ứng dụng
        self.root.title("PDF Processing Tool")

        # Tạo menu
        create_menu(self.root, self)

        # Hiển thị màn hình Welcome
        self.show_welcome_screen()

    def show_welcome_screen(self):
        """Hiển thị màn hình Welcome khi khởi động."""
        self.clear_interface()
        self.welcome_frame = tk.Frame(self.root)
        self.welcome_frame.pack(fill=tk.BOTH, expand=True)

        welcome_label = tk.Label(self.welcome_frame, text="Welcome to PDF Processing Tool", font=("Arial", 24))
        welcome_label.pack(expand=True)

    def clear_interface(self):
        """Xóa các widget hiện có trên giao diện trước khi hiển thị mới."""
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Menu):  # Không xóa menu
                continue
            widget.destroy()

    def show_highlight_pdf_interface(self):
        """Hiển thị giao diện cho chức năng Highlight PDF."""
        self.clear_interface()

        # Khung bên trái chứa các điều khiển
        self.left_frame = tk.Frame(self.root)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Nút chọn file PDF
        self.open_button = tk.Button(self.left_frame, text="Chọn file PDF", command=lambda: open_pdf(self.pdf_handler, self.canvas, self.display_pdf_page))
        self.open_button.pack(pady=5)

        # Ô nhập từ khóa
        self.keyword_label = tk.Label(self.left_frame, text="Nhập các từ khóa (mỗi từ khóa trên một dòng):")
        self.keyword_label.pack(pady=5, anchor="center")

        self.keyword_entry = ScrolledText(self.left_frame, height=10)
        self.keyword_entry.pack(pady=5, fill=tk.BOTH, expand=True)

        # Nút tìm kiếm từ khóa
        self.search_button = tk.Button(self.left_frame, text="Tìm kiếm nội dung", command=self.search_keywords, bg="yellow")
        self.search_button.pack(pady=5)

        # Ô hiển thị kết quả tìm kiếm
        self.result_text = ScrolledText(self.left_frame, height=10)
        self.result_text.pack(pady=5, fill=tk.BOTH, expand=True)

        # Nút để thay đổi thư mục lưu file
        self.change_folder_button = tk.Button(self.left_frame, text="Change folder to save", command=self.change_save_folder)
        self.change_folder_button.pack(pady=5)

        # Nút lưu file đã tô màu
        self.save_button = tk.Button(self.left_frame, text="Lưu file đã tô màu", command=lambda: save_highlighted_pdf(self.pdf_handler, self.save_folder_path, self.display_message_with_link))
        self.save_button.pack(pady=5)

        # Nút Undo để hoàn tác highlight
        self.undo_button = tk.Button(self.left_frame, text="Undo Highlight", command=self.undo_highlight)
        self.undo_button.pack(pady=5)

        # Khung bên phải chứa canvas hiển thị PDF
        self.right_frame = tk.Frame(self.root)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Canvas hiển thị trang PDF
        self.canvas = Canvas(self.right_frame, bg="white")
        self.canvas.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        # Các nút chuyển trang
        self.nav_frame = tk.Frame(self.right_frame)
        self.nav_frame.pack(side=tk.BOTTOM, pady=10)

        self.prev_page_button = tk.Button(self.nav_frame, text="Trang trước", command=lambda: prev_page(self.current_page, self.pdf_images, self.display_pdf_page, self.canvas))
        self.prev_page_button.pack(side=tk.LEFT, padx=10)

        self.next_page_button = tk.Button(self.nav_frame, text="Trang sau", command=lambda: next_page(self.current_page, self.pdf_images, self.display_pdf_page, self.canvas))
        self.next_page_button.pack(side=tk.LEFT, padx=10)

    def display_pdf_page(self, page_num, pdf_images=None, canvas=None):
        """Hiển thị trang PDF cụ thể."""
        if pdf_images is None:
            pdf_images = self.pdf_images
        if canvas is None:
            canvas = self.canvas

        if not pdf_images:
            return

        img = pdf_images[page_num]
        img_tk = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor="nw", image=img_tk)
        canvas.image = img_tk  # Giữ tham chiếu đến hình ảnh để tránh bị xóa khỏi bộ nhớ


    def change_save_folder(self):
        """Thay đổi thư mục lưu file."""
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.save_folder_path = folder_selected
            messagebox.showinfo("Thư mục lưu", f"Thư mục lưu đã thay đổi: {self.save_folder_path}")

    def show_extract_specifications_interface(self):
        """Hiển thị giao diện Extract Specifications."""
        self.clear_interface()

        # Khung bên trái hiển thị PDF
        self.left_frame = tk.Frame(self.root)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Canvas hiển thị trang PDF
        self.canvas = Canvas(self.left_frame, bg="white")
        self.canvas.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        # Khung chứa các nút chuyển trang
        self.nav_frame = tk.Frame(self.left_frame)
        self.nav_frame.pack(side=tk.BOTTOM, pady=10)
        self.prev_page_button = tk.Button(self.nav_frame, text="Trang trước", command=lambda: prev_page(self.current_page, self.pdf_images, self.display_pdf_page, self.canvas))
        self.prev_page_button.pack(side=tk.LEFT, padx=10)
        self.next_page_button = tk.Button(self.nav_frame, text="Trang sau", command=lambda: next_page(self.current_page, self.pdf_images, self.display_pdf_page, self.canvas))
        self.next_page_button.pack(side=tk.LEFT, padx=10)

        # Khung bên phải chứa nút và ô kết quả
        self.right_frame = tk.Frame(self.root)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Nút Extract Specifications
        self.extract_button = tk.Button(self.right_frame, text="Extract Specifications", command=self.extract_specifications)
        self.extract_button.pack(pady=10)

        # Ô hiển thị kết quả trích xuất thông số
        self.result_text = ScrolledText(self.right_frame, height=20, width=40)
        self.result_text.pack(pady=10, fill=tk.BOTH, expand=True)

    def extract_specifications(self):
        """Tìm kiếm và trích xuất các thông số kỹ thuật từ file PDF."""
        # Đặt các từ khóa liên quan đến thông số kỹ thuật
        specification_keywords = ["weight", "dimensions", "size", "capacity", "voltage", "current", "power", "length", "width", "height"]
        
        # Xóa kết quả cũ
        self.result_text.delete(1.0, tk.END)

        # Tìm kiếm các thông số kỹ thuật trong PDF
        results, doc_copy = self.search_handler.search_and_highlight(specification_keywords)

        if results:
            # Hiển thị kết quả trong ô kết quả
            for keyword, pages in results.items():
                self.result_text.insert(tk.END, f"{keyword}: {pages}\n")

            # Cập nhật lại hình ảnh PDF với các thông số được highlight
            self.pdf_handler.doc = doc_copy
            self.pdf_images = self.pdf_handler.convert_to_images()
            self.display_pdf_page(self.current_page)
        else:
            self.result_text.insert(tk.END, "Không tìm thấy thông số kỹ thuật.\n")

    def undo_highlight(self):
        """Hoàn tác highlight, khôi phục tài liệu gốc."""
        self.pdf_handler.restore_original()  # Khôi phục lại tài liệu gốc
        self.pdf_images = self.pdf_handler.convert_to_images()  # Cập nhật lại hình ảnh PDF
        self.display_pdf_page(self.current_page)  # Hiển thị lại trang hiện tại
        messagebox.showinfo("Hoàn tác", "Đã khôi phục tài liệu về trạng thái gốc.")

    def search_keywords(self):
        """Lấy từ khóa và tìm kiếm chúng trong bản sao của PDF."""
        # Xóa kết quả tìm kiếm trước đó
        self.result_text.delete(1.0, tk.END)
        
        # Lấy từ khóa từ ô nhập
        keywords = self.keyword_entry.get("1.0", tk.END).strip().splitlines()
        
        # Tìm kiếm và highlight các từ khóa trong bản sao của tài liệu
        results, doc_copy = self.search_handler.search_and_highlight(keywords)
        
        if results:
            self.display_results(results)
            # Cập nhật lại hình ảnh PDF từ bản sao đã highlight
            self.pdf_handler.doc = doc_copy  # Cập nhật bản sao đã highlight vào pdf_handler
            self.pdf_images = self.pdf_handler.convert_to_images()  # Chuyển đổi bản sao đã highlight thành hình ảnh
            self.display_pdf_page(self.current_page)  # Hiển thị lại trang hiện tại
        else:
            messagebox.showinfo("Kết quả tìm kiếm", "Không tìm thấy từ khóa.")

    def display_results(self, results):
        """Hiển thị kết quả tìm kiếm trong ô ScrolledText với màu sắc và liên kết."""
        # Xóa kết quả tìm kiếm trước đó
        self.result_text.delete(1.0, tk.END)

        total_keywords = len(results)
        found_count = sum(len(pages) for pages in results.values())

        # Hiển thị tổng số từ khóa tìm thấy
        self.result_text.insert(tk.END, f"Tìm thấy {found_count}/{total_keywords} từ khóa.\n\n")

        for keyword, pages in results.items():
            color = "blue" if pages else "gray"
            self.result_text.insert(tk.END, f"Từ khóa: {keyword} - ", color)

            if pages:
                for page_num in pages:
                    # Tạo liên kết để nhấp vào trang
                    self.result_text.insert(tk.END, f"Trang {page_num + 1} ", "link")
                self.result_text.insert(tk.END, "\n")
            else:
                self.result_text.insert(tk.END, "Không tìm thấy\n", "gray")

        # Định nghĩa các thẻ màu
        self.result_text.tag_config("blue", foreground="blue")
        self.result_text.tag_config("gray", foreground="gray")
        self.result_text.tag_config("link", foreground="blue", underline=True)

        # Thêm sự kiện nhấp chuột vào thẻ "link"
        self.result_text.tag_bind("link", "<Button-1>", self.on_click_result_link)

    def save_highlighted_pdf(self):
        """Lưu file PDF đã tô màu."""
        if not self.pdf_handler.doc:
            messagebox.showwarning("Lỗi", "Chưa mở file PDF.")
            return

        # Lấy tên file gốc mà không bao gồm đường dẫn
        original_file_name = os.path.basename(self.pdf_handler.pdf_path)
        # Tạo tên file với hậu tố _Highlighted
        file_name_with_suffix = f"{os.path.splitext(original_file_name)[0]}_Highlighted.pdf"

        if self.save_folder_path:
            # Lưu trong thư mục được chọn với tên file đã chỉnh sửa
            save_path = os.path.join(self.save_folder_path, file_name_with_suffix)
        else:
            # Lưu cùng vị trí với file gốc
            save_path = f"{os.path.splitext(self.pdf_handler.pdf_path)[0]}_Highlighted.pdf"

        # Lưu file PDF đã highlight
        self.pdf_handler.save_pdf(save_path)
        self.display_message_with_link(f"File đã được lưu thành công. Nhấn vào đường dẫn dưới để mở file:", save_path)

    def display_message_with_link(self, message, file_path):
        """Hiển thị thông báo với đường dẫn có thể nhấp chuột."""
        # Tạo cửa sổ mới cho thông báo
        msg_window = tk.Toplevel(self.root)
        msg_window.title("Thông báo")

        # Tạo nhãn thông báo
        msg_label = tk.Label(msg_window, text=message)
        msg_label.pack(pady=10)

        # Tạo nhãn có thể nhấp vào để mở file
        link_label = tk.Label(msg_window, text=file_path, fg="blue", cursor="hand2")
        link_label.pack(pady=10)

        # Thêm sự kiện nhấp vào nhãn để mở file PDF
        link_label.bind("<Button-1>", lambda e: open_pdf_in_system_viewer(file_path))

        # Nút để đóng cửa sổ
        close_button = tk.Button(msg_window, text="Đóng", command=msg_window.destroy)
        close_button.pack(pady=5)

    def on_click_result_link(self, event):
        """Xử lý sự kiện nhấp vào liên kết trang trong kết quả tìm kiếm."""
        index = self.result_text.index("@%s,%s" % (event.x, event.y))
        tag_ranges = self.result_text.tag_ranges("link")

        for i in range(0, len(tag_ranges), 2):
            if self.result_text.compare(tag_ranges[i], "<=", index) and self.result_text.compare(tag_ranges[i + 1], ">=", index):
                page_num = int(self.result_text.get(tag_ranges[i], tag_ranges[i + 1]).strip().split(" ")[-1]) - 1
                self.display_pdf_page(page_num)

    def show_about(self):
        """Hiển thị thông tin về ứng dụng."""
        about_message = """
        Phần mềm: Xử lý PDF
        Phiên bản: 1.0
        Phát triển bởi: Anhtn (09/2024)
        Bản quyền thuộc về TNNSI.VN

        v2.8: Đưa ra cảnh báo cho người dùng trong trường hợp lưu file mà chưa Highlight.
        v2.9: Nạp lại PDF gốc khi bôi màu, tạo menu hướng dẫn, giới thiệu.
        V3.1: Bổ sung nút Undo.
        """
        messagebox.showinfo("Giới thiệu về ứng dụng", about_message)

    def show_guide(self):
        """Hiển thị hướng dẫn sử dụng."""
        guide_message = """
        Hướng dẫn sử dụng phần mềm:
        1. Chọn file PDF bằng cách nhấn nút "Chọn file PDF".
        2. Nhập các từ khóa cần tìm (mỗi từ khóa trên một dòng).
        3. Nhấn nút "Tìm kiếm nội dung" để tìm từ khóa trong file PDF.
        4. Kết quả sẽ hiển thị số lượng từ khóa tìm thấy.
        5. Bạn có thể nhấn vào từ khóa để xem vị trí từ khóa đó trong PDF.
        6. Nhấn nút "Lưu file đã tô màu" để lưu file PDF đã tô sáng từ khóa.
        """
        # Tạo cửa sổ mới cho hướng dẫn sử dụng
        guide_window = tk.Toplevel(self.root)
        guide_window.title("Hướng dẫn sử dụng")
        guide_window.geometry("800x400")

        # Thêm text hướng dẫn
        guide_text = tk.Text(guide_window, wrap="none", font=("Arial", 12))
        guide_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        x_scroll = tk.Scrollbar(guide_window, orient=tk.HORIZONTAL, command=guide_text.xview)
        x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

        y_scroll = tk.Scrollbar(guide_window, orient=tk.VERTICAL, command=guide_text.yview)
        y_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        guide_text.configure(xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)

        guide_text.insert(tk.END, guide_message)
        guide_text.configure(state="disabled")

    def compare_pdfs(self):
        """Chức năng Compare PDF (Placeholder)."""
        messagebox.showinfo("Thông báo", "Chức năng Compare PDF chưa được phát triển.")

import os
import platform
import subprocess
from tkinter import messagebox

    def open_pdf_in_system_viewer(file_path):
        """Mở file PDF trong trình đọc mặc định của hệ thống."""
        try:
            if platform.system() == "Windows":
                os.startfile(file_path)  # Windows
            elif platform.system() == "Darwin":
                subprocess.run(["open", file_path])  # macOS
            else:
                subprocess.run(["xdg-open", file_path])  # Linux
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể mở file: {e}")
