from ._anvil_designer import SignupDialog_V2Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
#from .. import login_flow
from .. import return_to_mother_app

class SignupDialog_V2(SignupDialog_V2Template):
    def __init__(self, h={}, num_stage=0, **properties):
        # Set Form properties and Data Bindings.
        alert("sign in for ams, SignupDialog_V2")
        alert(h)
        self.init_components(**properties)
        self.name_box.text = ""
        self.email_box.text = ""
        self.password_box.text = ""
        self.password_repeat_box.text = ""
        self.num_stage = num_stage

        # Any code you write here will run when the form opens.
        self.name_box.focus()
        
    def button_validation_click(self, **event_args):
        """This method is called when the button is clicked"""
        # nom vide ?
        if self.name_box.text == "":
            alert("Entrez votre nom svp !")
            return
        # lg du nom >= 2 ? mais pas bloquant
        if len(self.name_box.text) <= 2 :
            r=alert("Votre Nom est-il correct ?",buttons=[("non",False),("oui",True)])
            if not r :   #Non, nom pas correct
                return
        #1ere lettre en majuscules
        nm = self.name_box.text
        nm = nm.capitalize()
        self.name_box.text = nm

        # mail vide ?
        if self.email_box.text == "":
            alert("Entrez votre mail svp !")
            return
        # mail en minuscule    et strip
        mel = self.email_box.text
        mel = mel.lower()
        mel = mel.strip()
        self.email_box.text = mel

        # @ ds mail ?
        if not "@" in self.email_box.text:
            alert("Entrez un mail valide !")
            return

        if self.password_box.text != self.password_repeat_box.text:
            alert("Les mots de passe sont différents !")
            return
        # ------------------------------------------------------------   VALIDATION 
        err = anvil.server.call('do_signup', self.email_box.text, self.name_box.text, self.password_box.text, self.num_stage)
        if err != None:
            alert(err)
            return_to_mother_app.calling_mother_app()
        if anvil.server.call('_send_email_confirm_link', self.email_box.text):
            alert(f"Un email de confirmation vous a été envoyé à {self.email_box.text}.")
        else:
            alert(f"'{d.email_box.text}', cette adresse est déjà confirmée. Connectez-vous !")
            """
            A FAIRE envoi en connection
            """
        return_to_mother_app.calling_mother_app()
            
    def button_retour_click(self, **event_args):
        """This method is called when the button is clicked"""
        return_to_mother_app.calling_mother_app()

    def password_repeat_box_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        self.button_validation_click()



