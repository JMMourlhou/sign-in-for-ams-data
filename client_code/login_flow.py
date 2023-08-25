from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from LoginDialog import LoginDialog
from SignupDialog import SignupDialog
from ForgottenPasswordDialog import ForgottenPasswordDialog
from PasswordResetDialog import PasswordResetDialog
from . import return_to_mother_app


def login_with_form(allow_cancel=True):
  """Log in by popping up the custom LoginDialog"""
  d = LoginDialog()
    
  BUTTONS = []
  BUTTONS = [("Se connecter", "login", "primary")]
  if allow_cancel:
    BUTTONS += [("Annuler", None)]
  
  while anvil.users.get_user() is None:
    choice = alert(d, title="", dismissible=allow_cancel, buttons=BUTTONS)
    print("choice:", choice)
    if choice == 'login':
        if d.email_box.text == "":
            alert("Rentrez le mail !")
            return
        
        mel = d.email_box.text
        mel = mel.lower()
        d.email_box.text = mel
        
        try:
            user=anvil.users.login_with_email(d.email_box.text, d.password_box.text, remember=True)
            user=anvil.server.call("force_log",user)
            return_to_mother_app.calling_mother_app(2)
        except anvil.users.EmailNotConfirmed:
            alert("Votre mail n'est pas confirmé, Vérifiez le mail que nous vs avions envoyé !")
            if anvil.server.call('_send_email_confirm_link', d.email_box.text):
                alert(f"Un nouvel email de confirmation a été envoyé à {d.email_box.text}.")
            break
        except anvil.users.AuthenticationFailed as e:
            alert(f"Email ou mot de passe erroné, Ré-entrez les !")
            self.raise_event('x-close-alert', value='login')  
            break
            
        
        
            
    elif choice == 'reset_password':
      fp = ForgottenPasswordDialog(d.email_box.text)
      
      if alert(fp, title='Mot de passe oublié', buttons=[("Le réinitialiser", True, "primary"), ("Annuler", False)]):
        #fp.email_box.text = fp.email_box.text.lower()
        if anvil.server.call('_send_password_reset', fp.email_box.text):
          alert(f"Un mail de réinitilisation du mot de passe a été envoyé à {fp.email_box.text}.")
          return_to_mother_app.calling_mother_app()
          #break  # I come out from the loop
        else:
          alert("Cet utilisateur n'existe pas dans nos fichiers.")
        
    elif choice == 'confirm_email':
      if anvil.server.call('_send_email_confirm_link', d.email_box.text):
        alert(f"Un nouvel email de confirmation a été envoyé à {d.email_box.text}.")
      else:
        alert(f"'{d.email_box.text}' n'est pas un utilisateur dont le mail n'est pas encore confirmé.")
      d.confirm_lnk.visible = False
    
    elif choice is None:  #cancel
      break # je sors de la boucle while
      
        
def signup_with_form(num_stage):
  d = SignupDialog()

  while True:
    if not alert(d, title="Création de votre compte", buttons=[("S'enregistrer", True, 'primary'), ("Annuler", False)]):
      return
        
    if d.password_box.text == "":
      d.signup_err_lbl.text = "Le mot de passe n'est pas rentré !"
      return
    if d.password_box.text != d.password_repeat_box.text:
      d.signup_err_lbl.text = "Les mots de passe sont différents! Recommencez."
      d.signup_err_lbl.visible = True
      continue

    if d.email_box.text == "":
      d.signup_err_lbl.text = "Le mail n'est pas rentré !"
      return
    if d.name_box.text == "":
      d.signup_err_lbl.text = "Le nom n'est pas rentré !"
      return 
        
    err = anvil.server.call('do_signup', d.email_box.text, d.name_box.text, d.password_box.text, num_stage)
    if err is not None:
      alert(err)  
    else:
        if anvil.server.call("_send_email_confirm_link", d.email_box.text):
            alert(f"Nous vous avons envoyé un mail de confirmation\n à l'adresse: {d.email_box.text}.\n\nVérifiez votre mail, et cliquez sur le lien.")
    break

    
def do_email_reset(h):
  """Check whether the user has arrived from a password reset, and pop up any necessary dialogs."""
    
  #alert(" fonction do_email_reset(h)  activée!")  
     
  """  situation: Pw reset """  
  if h['a']=='pwreset':
    if not anvil.server.call('_is_password_key_correct', h['email'], h['api']):
        alert("Ceci n'est pas un lien valide pour le lien de réinitialisation")
        return
    #user who changes his pw exists and 2apis identicals, asking him the new pw in dialog 
    while True:
        pwr = PasswordResetDialog()    
        if not alert(pwr, title="Reinitialisez le mot de passe", buttons=[("Changer Mot de passe", True, 'primary'), ("Annuler", False)]):
            return
        if pwr.pw_box.text != pwr.pw_repeat_box.text:
            alert("Les Mots de Passe sont différents, recommencez.")
        else:
            break

    if anvil.server.call('_perform_password_reset', h['email'], h['api'], pwr.pw_box.text):
        alert("Votre mot de passe a été reinitialisé. Connectez-vous maintenant.")
    else:
        alert("Ceci n'est pas un mot de passe valide pour le lien de réinitialisation")
          
     