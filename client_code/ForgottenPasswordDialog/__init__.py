from ._anvil_designer import ForgottenPasswordDialogTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ForgottenPasswordDialog(ForgottenPasswordDialogTemplate):
  def __init__(self, email=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    if email is not None:
      self.email_box.text = email.lower()

  def close_alert(self, **kws):
    """Close any alert we might be in with True value."""
    self.raise_event('x-close-alert', value=True)
       

  def email_box_lost_focus(self, **event_args):
      """This method is called when the TextBox loses focus"""
      ml = self.email_box.text
      ml = ml.lower()
      self.email_box.text = ml

