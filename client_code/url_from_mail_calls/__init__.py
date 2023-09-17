from ._anvil_designer import url_from_mail_callsTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import url_from_mail

""" Je ne peux pas appeler directement un module de cette appli d'1 autre appli (AMS data par ex),
Donc je crée cette form et l'appelle de l'extérieur pour:
    - Toutes les réponses des liens envoyés par mail qui viennent d'être clickés :
          mails de confirmation (après un nouveau user)
          password reset (oublié)
          
"""


class url_from_mail_calls(url_from_mail_callsTemplate):
    def __init__(self, h, num_stage=0, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        url_from_mail.confirm_or_pwreset(h, num_stage=0)