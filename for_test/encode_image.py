import base64

# Đọc tệp ảnh và chuyển thành base64
with open("logo.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

# Tạo chuỗi base64 dưới dạng chuỗi nhiều dòng trong Python
line_length = 76  # Chiều dài mỗi dòng, thường là 76 ký tự
base64_lines = [encoded_string[i:i+line_length] for i in range(0, len(encoded_string), line_length)]

# In chuỗi base64 dưới dạng chuỗi nhiều dòng sử dụng dấu nháy kép
print('image_base64 = (\n    "' + '"\n    "'.join(base64_lines) + '"\n)')
