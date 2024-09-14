from tkinter import filedialog, Canvas, messagebox
from PIL import ImageTk
import os

def open_pdf(pdf_handler, canvas, display_pdf_page_callback):
    """Mở file PDF và hiển thị hình ảnh các trang."""
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        pdf_handler.open_pdf(pdf_path)
        pdf_images = pdf_handler.convert_to_images()
        
        # Chỉ truyền một tham số cho callback
        display_pdf_page_callback(0)  # Hiển thị trang đầu tiên


def display_pdf_page(page_num, pdf_images, canvas):
    """Hiển thị trang PDF cụ thể."""
    if not pdf_images:
        return
    img = pdf_images[page_num]
    img_tk = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor="nw", image=img_tk)
    canvas.image = img_tk

def next_page(current_page, pdf_images, display_pdf_page, canvas):
    """Chuyển sang trang tiếp theo."""
    if current_page < len(pdf_images) - 1:
        current_page += 1
        display_pdf_page(current_page, pdf_images, canvas)

def prev_page(current_page, pdf_images, display_pdf_page, canvas):
    """Quay lại trang trước."""
    if current_page > 0:
        current_page -= 1
        display_pdf_page(current_page, pdf_images, canvas)

def save_highlighted_pdf(pdf_handler, save_folder_path, display_message_with_link):
    """Lưu file PDF đã tô màu."""
    if not pdf_handler.doc:
        messagebox.showwarning("Lỗi", "Chưa mở file PDF.")
        return

    # Lấy tên file gốc mà không bao gồm đường dẫn
    original_file_name = os.path.basename(pdf_handler.pdf_path)
    # Tạo tên file với hậu tố _Highlighted
    file_name_with_suffix = f"{os.path.splitext(original_file_name)[0]}_Highlighted.pdf"

    if save_folder_path:
        # Lưu trong thư mục được chọn với tên file đã chỉnh sửa
        save_path = os.path.join(save_folder_path, file_name_with_suffix)
    else:
        # Lưu cùng vị trí với file gốc
        save_path = f"{os.path.splitext(pdf_handler.pdf_path)[0]}_Highlighted.pdf"

    # Lưu file PDF đã highlight
    pdf_handler.save_pdf(save_path)
    display_message_with_link(f"File đã được lưu thành công. Nhấn vào đường dẫn dưới để mở file:", save_path)
