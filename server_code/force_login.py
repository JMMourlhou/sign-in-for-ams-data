import anvil.files
from anvil.files import data_files
import anvil.email
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from . import french_zone # importation du module pour le calcul du jour / heure du sign in

@anvil.server.callable
def force_log(user_row):
    user=anvil.users.force_login(user_row,remember=True)
    user["last_login"]=french_zone.time_french_zone()  # Update the login time
    return user