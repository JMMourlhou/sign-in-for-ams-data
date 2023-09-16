from ._anvil_designer import LoginDialog_V2Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import login_flow
from .. import return_to_mother_app

class LoginDialog_V2(LoginDialog_V2Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run when the form opens.
        self.email_box.focus()

    def email_box_lost_focus(self, **event_args):
        """This method is called when the TextBox loses focus"""
        pass
        

    def password_box_lost_focus(self, **event_args):
        """This method is called when the TextBox loses focus"""
        pass
        

    def button_retour_click(self, **event_args):
        """This method is called when the button is clicked"""
        return_to_mother_app.calling_mother_app()

    def button_validation_click(self, **event_args):
        """This method is called when the button is clicked"""
        # --------------------------------Tests sur mail
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
            self.email_box.focus()
            return
        # --------------------------------Tests sur mot de passe   
        if self.password_box.text == "":
            alert("Entrez le mot de passe svp !")
            self.password_box.focus()
            return   
        # ------------------------------------------------------------   VALIDATION 
        try:
            user=anvil.users.login_with_email(self.email_box.text, self.password_box.text, remember=True)
            user=anvil.server.call("force_log",user)
            return_to_mother_app.calling_mother_app(2)
        except anvil.users.EmailNotConfirmed:
            alert("Votre mail n'est pas encore confirmé! Vérifiez le mail que nous vs avions envoyé !")
            if anvil.server.call('_send_email_confirm_link', self.email_box.text):
                alert(f"Un nouvel email de confirmation vous a été envoyé à {email_box.text}.")
                return_to_mother_app.calling_mother_app()
        except anvil.users.AuthenticationFailed as e:
            alert(f"Email ou mot de passe erroné, Ré-entrez les !")
            return

    def password_box_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        self.button_validation_click()

    def reset_pw_link_click(self, **event_args):
        """This method is called when the link is clicked"""
        # --------------------------------Tests sur mail
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
            self.email_box.focus()
            return
            
        if anvil.server.call('_send_password_reset', self.email_box.text):
          alert(f"Un mail de réinitilisation du mot de passe vous a été envoyé à {self.email_box.text}.")
          return_to_mother_app.calling_mother_app()



        
        
        

