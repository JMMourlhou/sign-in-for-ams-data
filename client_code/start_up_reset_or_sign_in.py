import anvil.server
from anvil.google.drive import app_files
from anvil import *   # to load the alert 
from anvil import open_form
from .Form1 import Form1

""" This is the startup module.
x représente le nb d'appel du module
Il permet de tester si APP mère est appelé par une URL en cas de sign in ou pw reset 
je l'incrémente à l'ouverture de home_form
"""
def start_sign_in(h={}):
    alert(h,title="start signin")
    open_form('Form1',h)  
