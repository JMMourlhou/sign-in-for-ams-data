from ._anvil_designer import SignupDialogTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class SignupDialog(SignupDialogTemplate):
  def __init__(self, num_stage=0, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.name_box.text = ""
    self.email_box.text = ""
    self.password_box.text = "" 
    self.password_repeat_box.text = ""
    
    self.image_1.visible = False
    # Any code you write here will run when the form opens.
    self.focus_email()
    
  def focus_email(self, **kws):
     """Focus on the name box."""
     self.name_box.focus()

  def focus_password(self, **kws):
    """Focus on the password box."""
    self.password_box.focus()

  def focus_password_repeat(self, **kws):
    """Focus on the password repeat box."""
    self.password_repeat_box.focus()

  def close_alert(self, **kws):
    """Close any alert we might be in with True value."""
    self.raise_event('x-close-alert', value=True)

  def password_box_focus(self, **event_args):
      """This method is called when the TextBox gets focus"""
      # nom vide ?
      if self.name_box.text == "":
        alert("Entrez votre nom svp !")
        self.close_alert()
        return
      # lg du nom >= 2 ? mais pas bloquant
      if len(self.name_box.text) <= 2 :
        r=alert("Votre Nom est-il correct ?","oui","non")
        result = alert(content="Votre Nom est-il correct ?",
               large=False,
               buttons=[
                 ("Oui", "YES"),
                 ("Non", "NO"),
                 ])
      #1ere lettre en majuscules
      nm = nm.capitalize()
      self.name_box.text = nm
      
      # mail vide ?
      if self.email_box.text == "":
        alert("Entrez votre mail svp !")
        return
      # mail en minuscule    
      mel = self.email_box.text
      mel = mel.lower()
      self.email_box.text = mel
      # @ ds mail ?
      if not "@" in self.email_box.text:
          alert("Entrez un mail valide")
          return

     




