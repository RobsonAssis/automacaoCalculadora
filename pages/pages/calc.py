from Pyautomators.desk import Desk
from Pyautomators.mouse_teclado import Teclado
from Pyautomators.mouse_teclado import Mouse
from Pyautomators.Verifica import Valida
import pyautogui
from PIL import Image
import pytesseract
from time import sleep



class Calculadora():
    
    def __init__(self,app):
        self.app = app

    def validacao_tela(self, imagem):
        tentativas = 50
        for tentativas in range(tentativas):
            if(self.app.verifica_tela(imagem, 80, similaridade=50) != None):
                break
            time.sleep(2)
            
    #CP01
    def valida_abertura(self):
        self.app.clica_imagem(r'data\images\menu.png', similar=70)
        self.app.clica_imagem(r'data\images\padrao.png', similar=70)
        self.validacao_tela(imagem=r'data\images\validaPadrao.png')
        self.app.clica_imagem(r'data\images\validaPadrao.png', similar=70)
    
    '''def pega_localizacao():
        x,y,w,h = pyautogui.locateOnScreen(r'teste.png')
        return x,y,w,h
'''

        
    def abrir_cientifica(self):
        self.app.clica_imagem(r'data\images\menu.png', similar=70)
        self.app.clica_imagem(r'data\images\cientifica.png', similar=70)
        self.app.clica_imagem(r'data\images\validaCientifica.png',similar=70)
    
    #CP02
    def valida_cientifica(self):
        self.validacao_tela(imagem=r'data\images\validaCientifica.png')
        self.app.clica_imagem(r'data\images\validaCientifica.png', similar=70)
            

    def calcular(self,operacao,valor1, valor2):
        
        if(valor1 == '1'):
            self.app.clica_imagem(r'data\images\numero1.png', similar=70)
        elif(valor1 == '2'):
            self.app.clica_imagem(r'data\images\numero2.png', similar=70)
        elif(valor1 == '3'):
            self.app.clica_imagem(r'data\images\numero3.png', similar=70)
        elif(valor1 == '4'):
            self.app.clica_imagem(r'data\images\numero4.png', similar=70)
        elif(valor1 == '5'):
            self.app.clica_imagem(r'data\images\numero5.png', similar=70)
        elif(valor1 == '6'):
            self.app.clica_imagem(r'data\images\numero6.png', similar=70)
        elif(valor1 == '7'):
            self.app.clica_imagem(r'data\images\numero7.png', similar=70)
        elif(valor1 == '8'):
            self.app.clica_imagem(r'data\images\numero8.png', similar=70)
        elif(valor1 == '9'):
            self.app.clica_imagem(r'data\images\numero9.png', similar=70)

        if(operacao == 'soma'):
            self.app.clica_imagem(r'data\images\soma.png', similar=70)
        elif(operacao == 'multiplicacao'):
            self.app.clica_imagem(r'data\images\multiplicacao.png', similar=70)
        elif(operacao == 'substracao'):
            self.app.clica_imagem(r'data\images\substracao.png', similar=70)
        elif(operacao == 'divisao'):
            self.app.clica_imagem(r'data\images\divisao.png', similar=70)

        if(valor2 == '1'):
            self.app.clica_imagem(r'data\images\numero1.png', similar=70)
        elif(valor2 == '2'):
            self.app.clica_imagem(r'data\images\numero2.png', similar=70)
        elif(valor2 == '3'):
            self.app.clica_imagem(r'data\images\numero3.png', similar=70)
        elif(valor1 == '4'):
            self.app.clica_imagem(r'data\images\numero4.png', similar=70)
        elif(valor1 == '5'):
            self.app.clica_imagem(r'data\images\numero5.png', similar=70)
        elif(valor1 == '6'):
            self.app.clica_imagem(r'data\images\numero6.png', similar=70)
        elif(valor1 == '7'):
            self.app.clica_imagem(r'data\images\numero7.png', similar=70)
        elif(valor1 == '8'):
            self.app.clica_imagem(r'data\images\numero8.png', similar=70)
        elif(valor1 == '9'):
            self.app.clica_imagem(r'data\images\numero9.png', similar=70)


    def valida_valor(self,):
        self.app.clica_imagem(r'data\images\resultado.png', similar=70)
        res = pyautogui.screenshot(region=(781,180,24,42))
        res.save(r'data\images\res.png')

        '''res = pyautogui.locateOnScreen(r'data\images\teste.png')
        res = pyautogui.screenshot(region=(x,y,w,h))
        res.save(r'data\images\res.png')
        res_texto = pytesseract.image_to_string(r'data\images\res.png')
        print(res_texto)    
    '''
    def menu_padrao(self):
        self.app.clica_imagem(r'data\images\menu.png', similar=70)
        self.app.clica_imagem(r'data\images\padrao.png', similar=70)
        
       
    
  
        

        