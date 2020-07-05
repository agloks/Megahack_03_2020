# Import QRCode from pyqrcode 
import pyqrcode 
import png 
from pyqrcode import QRCode 
  
# ONG FUNDAÇÃO EUFRATEN 
s = "https://pagseguro.uol.com.br/checkout/nc/nl/donation/sender-identification.jhtml?t=725314841dea815b847ba2e316fe09be4aedaf0325ff6d0fa064075d74f7a31b&e=true#rmcl"
  
# Generate QR code 
url = pyqrcode.create(s, error='H') 
  
url.svg("imgs/qrcode_test_eufraten.svg") 
url.png('imgs/qrcode_test_eufraten.png')