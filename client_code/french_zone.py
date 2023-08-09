import anvil.server

# Pour le calcul de l'heure en France
from datetime import datetime
from pytz import timezone

def time_french_zone():
    now_utc = datetime.now(timezone('UTC'))
    date_time = now_utc.astimezone(timezone('Europe/Paris')) # initialisation of the date & time of writing
    return date_time
