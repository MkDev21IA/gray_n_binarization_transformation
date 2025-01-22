#Esse projeto consiste da criação de duas funções, uma para transformar uma imagem em tons de cinza, e a outra para fazer uma binarização, ou seja,\
#transformar a imagem em preto e branco. Isso sem utilizar biblioteca OpenCV que é a mais comum para esse tipo de tarefa.
#Seria possivel utilizar limiar médio na função de transformar em preto e branco, mas isso é só um detalhe.

#Importação das biblioteca necessária
from PIL import Image

#Função para transformar uma imagem em tons de cinza
def gray_transformation(image):
    image2 = image.copy()
    width, height = image2.size
    for x in range(width):
        for y in range(height):
            r, g, b = image2.getpixel((x, y))
            gray = int(0.3*r + 0.59*g + 0.11*b)
            image2.putpixel((x,y),(gray , gray, gray))
    return image2

#Função para transformar uma imagem em preto e branco
def blackandwhite_transformation(image):
    image3 = image.copy()
    image3 = gray_transformation(image3)
    width, height = image3.size
    for x in range(width):
        for y in range(height):
            if image3.getpixel((x,y))[0] < 128:
                color = 0
            else:
                color = 255
            image3.putpixel((x,y),(color,color,color))
    return image3

#Caminho para a imagem
image_path = 'buzz_lightyear.jpg'

#Abrir a imagem
image = Image.open(image_path)

#Transformando-a em tons de cinza
image2 = gray_transformation(image)

#Transformando-a em preto e branco
image3 = blackandwhite_transformation(image)

image.show()
image2.show()
image3.show()
