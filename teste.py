from PIL import Image
import pyautogui
import pytesseract


def pega_localizacao():
    x,y,w,h = pyautogui.locateOnScreen(r'data\images\teste.png')
    return x,y,w,h
    
#print( pytesseract.image_to_string(Image.open(r'data\images\1.png')))# Extraindo o texto da imagem 
'''x,y,w,h = pyautogui.locateOnScreen(r'data\images\teste.png')
print(x,y,w,h)'''