from tkinter import Menu
from ui.help_handler import show_about, show_guide

def create_menu(root, pdf_viewer_ui):
    """Tạo menu chính cho ứng dụng."""
    menubar = Menu(root)

    # Tạo menu "Công cụ PDF"
    pdf_tools_menu = Menu(menubar, tearoff=0)
    pdf_tools_menu.add_command(label="Highlight PDF", command=pdf_viewer_ui.show_highlight_pdf_interface)
    pdf_tools_menu.add_command(label="Extract Specifications", command=pdf_viewer_ui.show_extract_specifications_interface)
    menubar.add_cascade(label="Công cụ PDF", menu=pdf_tools_menu)

    # Tạo menu "Trợ giúp"
    help_menu = Menu(menubar, tearoff=0)
    help_menu.add_command(label="Giới thiệu về ứng dụng", command=lambda: show_about(root))
    help_menu.add_command(label="Hướng dẫn sử dụng", command=lambda: show_guide(root))
    menubar.add_cascade(label="Trợ giúp", menu=help_menu)

    root.config(menu=menubar)
