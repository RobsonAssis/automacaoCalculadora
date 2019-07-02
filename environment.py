
"""		Pyautomator Framework de teste 

			Calculadora"""

from Pyautomators.desk import Desk
from Pyautomators.mouse_teclado import Teclado
from Pyautomators.mouse_teclado import Mouse
from Pyautomators.Verifica import Valida
from Pyautomators import Ambiente
from pages.pages.calc import Calculadora
from Pyautomators import *
from time import sleep


def before_all(context):
	context.app = Desk('C:\Windows\System32\calc.exe', Driver_Winium='driver\Winium.Desktop.Driver.exe')
	context.calc = Calculadora(context.app)
	
def before_feature(context,feature):
	pass

def before_scenario(context,scenario):
	pass

def before_step(context,step):
	pass

def after_step(context,step):
	pass

def after_scenario(context,scenario):
	pass

def after_feature(context,feature):
	pass

def after_all(context):
	pass