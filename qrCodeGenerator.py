import qrcode
import PIL.Image
  
# String which represent the QR code 
url = "https://tr.linkedin.com/in/%C3%B6zg%C3%BCr-bas%C4%B1k-8a71a0222"
  
# Generate QR code 
img = qrcode.make(url)
img.save("qrimg.jpg")  
