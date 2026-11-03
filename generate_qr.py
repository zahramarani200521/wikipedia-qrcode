import qrcode
import os

# 1. Define folder and file name
folder_name = "generated_qrcodes"
file_name = "wikipedia_qr.png"

# 2. Create full path
full_path = os.path.join(folder_name, file_name)

# 3. Create folder
os.makedirs(folder_name, exist_ok=True)

# 4. Create QR Code
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

# 5. Add website link
qr.add_data('https://www.wikipedia.org/')
qr.make(fit=True)

# 6. Create QR Code image
img = qr.make_image(
    fill_color="black",
    back_color="lightyellow"
)

# 7. Save image
img.save(full_path)

print("QR code saved successfully!")
print("Website: https://www.wikipedia.org/")
print("File:", os.path.abspath(full_path))