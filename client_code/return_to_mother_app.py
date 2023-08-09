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
    import Fitness_d
    #from Fitness_d.home_form import home_form
    #open_form('Fitness_d.home_form',x)    #x=3 si login normale
    from Fitness_d import Module1
    Module1.starting_app(x)  # ds main app 2+1 donc pas de retour ds Sign In
