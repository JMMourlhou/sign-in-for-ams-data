from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.users
#import anvil.google
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import login_flow
from .. import return_to_mother_app
from .. import url_from_mail

class Form1(Form1Template):
  def __init__(self, h={}, num_stage=0, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.
    self.num_stage = num_stage  
    self.h=h
    #alert(h)
    if len(h)!=0:  # a URL from a confirm/reset_pw mail/qr code was sent to main app
        url_from_mail.confirm(h, num_stage) 
            
    self.update_login_status()
        
  def update_login_status (self):
    user = anvil.users.get_user()
    if user is None:
      self.login_status_lbl.text = "Vous n'êtes pas connecté."
      self.login_btn.visible = True
      self.logout_btn.visible = False
      #login_flow.login_with_form()
    else:
      self.login_status_lbl.text = "Vous êtes connecté en tant que %s" % user['email']
      self.login_btn.visible = False
      self.logout_btn.visible = True
      #get_open_form().content_panel.clear()
      return_to_mother_app.calling_mother_app(2)
      
        
  def login_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    login_flow.login_with_form()
    self.update_login_status()

  def logout_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    self.update_login_status()

  def signup_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    login_flow.signup_with_form(self.num_stage)

  
    

  


  
    
    




