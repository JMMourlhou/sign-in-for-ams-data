import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# accès à une var globale précise (en donnant son nom coté client)
@anvil.server.callable
def get_var_value(variable_name):
    # 'variable' nom de la variable globale ds table 'global_variables')
    # 'value' contenu de ma variable globale.
    row = app_tables.global_variables.get(name=variable_name)
    if row:
        # Return the value associated with the variable name
        return row['value']
    else:
        # Handle the case where the variable does not exist
        return None


# Pour avoir en mémoire toutes les variables (si je veux les afficher par ex) PAS ENCORE UTILISé
@anvil.server.callable
def get_variable_names():
    return [row['name'] for row in app_tables.global_variables.search()]


"""
# pour mettre à jour éventuellement les variables par programme
@anvil.server.callable
def set_variable_value(variable_name, value):
    row = app_tables.global_variables.get(name=variable_name)
    if row:
        # If the variable already exists, update its value
        row['value'] = value
    else:
        # If the variable does not exist, add a new row to the table
        app_tables.global_variables.add_row(name=variable_name, value=value)

    return value
"""