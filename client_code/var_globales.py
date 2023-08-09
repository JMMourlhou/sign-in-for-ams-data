import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server

# Variables globales que j'appelle par 'var_globales.code_app'
code_app1 = "https://2erggvosxp234ktt.anvil.app/EK44RJHJVMRZ7R52DY6NEURF"   # App "AMS Data"  
code_app2 = "https://2erggvosxp234ktt.anvil.app/EK44RJHJVMRZ7R52DY6NEURF" # App "sign-up_for_AMS_Data"
nom_app_pour_mail = "AMS Data"                                          
mon_mail = "jmarc@formation-et-services.fr"
mon_logo = "logo_fs_small.png"
timedelay_url_in_min = 10 #10 minutes delay, after URL (mail-confirm or pw-reset) over 