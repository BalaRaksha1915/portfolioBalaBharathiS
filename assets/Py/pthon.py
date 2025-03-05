import qrcode
from PIL import Image

# Define the QR Code
qr = qrcode.QRCode(
    version=5,  # Adjust size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for embedding an image
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data("http://www.myportfoliobalabharathi.in/")
qr.make(fit=True)

# Create the QR code image
qr_img = qr.make_image(fill="black", back_color="white").convert("RGB")

# Path to the logo image (Make sure the path is correct)
logo_path = r"C:\Users\balab\OneDrive\Desktop\portfollio\portfolioBalaBharathiS\assets\Py\Blogo.jpeg"  # Change to your logo file path

try:
    # Open the logo image
    logo = Image.open(logo_path)

    # Resize the logo to fit inside the QR code
    logo_size = min(qr_img.size) // 5  # Logo size relative to QR code
    logo = logo.resize((logo_size, logo_size))

    # Calculate position to place the logo in the center
    pos = ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2)

    # Paste the logo onto the QR code
    qr_img.paste(logo, pos)
except FileNotFoundError:
    print(f"Error: Logo file not found at {logo_path}. Generating QR code without logo.")

# Show and save the QR code
qr_img.show()
qr_img.save("portfolio_qr_with_logo.png")
