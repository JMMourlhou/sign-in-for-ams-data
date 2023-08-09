from anvil import *
import anvil.server
from anvil import open_form
"""
Je constate que je ne peux pas appeler open_form d'une form
mais seulement d'un module !
"""
""" ************************************************************************"""  
""" This part will have to be adapted to any APP callind SIGN UP app """
""" ************************************************************************"""  
def calling_mother_app(x=2):
    import AMS_Data
    from AMS_Data import Module1
    Module1.starting_app(x)  # ds main app 2+1 donc pas de retour ds Sign In
