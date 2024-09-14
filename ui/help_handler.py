import tkinter as tk
from tkinter import messagebox

def show_about(root):
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

def show_guide(root):
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
    guide_window = tk.Toplevel(root)
    guide_window.title("Hướng dẫn sử dụng")
    guide_window.geometry("800x400")

    guide_text = tk.Text(guide_window, wrap="none", font=("Arial", 12))
    guide_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    x_scroll = tk.Scrollbar(guide_window, orient=tk.HORIZONTAL, command=guide_text.xview)
    x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

    y_scroll = tk.Scrollbar(guide_window, orient=tk.VERTICAL, command=guide_text.yview)
    y_scroll.pack(side=tk.RIGHT, fill=tk.Y)

    guide_text.configure(xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)
    guide_text.insert(tk.END, guide_message)
    guide_text.configure(state="disabled")
