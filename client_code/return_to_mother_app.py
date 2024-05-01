from anvil import *
import anvil.server
import AMS_Data


"""
Je constate que je ne peux pas appeler open_form d'une form
mais seulement d'un module !
"""
""" ************************************************************************"""  
""" This part will have to be adapted to any APP callind SIGN UP app """
""" ************************************************************************"""  
def calling_mother_app(x=2):
    
    from AMS_Data.Main import Main
    from anvil import open_form    #Main.content_panel.clear()
    open_form('AMS_Data.Main',x)    #x=3 si login normal
    