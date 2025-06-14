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
    
    
    # Any code you write here will run when the form opens.
    self.focus_email()
      
  def focus_name(self, **kws):
     """Focus on the name box."""
     self.name_box.focus()
      
  def focus_email(self, **kws):
     """Focus on the name box."""
     self.email_box.focus()

  def focus_password(self, **kws):
    """Focus on the password box."""
    self.password_box.focus()

  def focus_password_repeat(self, **kws):
    """Focus on the password repeat box."""
    self.password_repeat_box.focus()

  def close_alert(self, **kws):
    """Close any alert we might be in with False value."""
    self.raise_event('x-close-alert', value=False)

  def password_box_focus(self, **event_args):
      """This method is called when the TextBox gets focus"""
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
      if "@" not in self.email_box.text:
          alert("Entrez un mail valide !")
          return

     




