from ._anvil_designer import LoginDialogTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import login_flow

class LoginDialog(LoginDialogTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.image_1.visible = False
    # Any code you write here will run when the form opens.
    self.email_box.focus()
      
  def confirm_lnk_click (self, **event_args):
    """Close any alert we might be in with 'confirm_email' value."""
    self.raise_event('x-close-alert', value='confirm_email')

  def reset_pw_link_click (self, **event_args):
    """Close any alert we might be in with 'reset_password' value."""
    self.raise_event('x-close-alert', value='reset_password')
    
  def focus_password(self, **kws):
     """Focus on the password box."""
     self.password_box.focus()

  def close_alertmel(self, **kws):
     """Close any alert we might be in with 'login' value."""
     self.raise_event('x-close-alert', value='login')

  def form_show(self, **event_args):
      """This method is called when the column panel is shown on the screen"""
      self.email_box.focus()


 

  



  





