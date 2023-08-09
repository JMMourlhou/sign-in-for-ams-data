import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server

# Variables globales que j'appelle par 'var_globales.code_app'
code_app1 = "https://R4JRRFM62XCXXE6E.anvil.app/7DMDO4IOGQA2FTMYFDGX6EPV"   # App "Fitness'd"  
code_app2 = "https://EQQMHT4ZPNVIAT2X.anvil.app/4JZ7UGVU2GVJUMBKVNEY3VPL" # App "fr_custom_signup"
nom_app_pour_mail = "Fitness'd, "                                          
mon_mail = "jmarc@formation-et-services.fr"
mon_logo = "logo_fs_small.png"
timedelay_url_in_min = 10 #10 minutes delay, after URL (mail-confirm or pw-reset) over 