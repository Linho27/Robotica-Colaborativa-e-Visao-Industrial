# Importar Image da biblioteca Pillow
from PIL import Image

# Definir var img
img1 = Image.open(r"C:\Users\paulo\Desktop\pasta\print.png")
img2 = Image.open("imagem.jpg")

# Abrir img
img1.show()
img2.show()