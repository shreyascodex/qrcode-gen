import qrcode

text = input("Enter text or URL: ")

img = qrcode.make(text)
img.save("QrCode.png")

print("QR code generated successfully!")