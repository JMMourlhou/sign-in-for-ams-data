""" Read the URL sent by the mail link, after a new user signed in or PW reset"""
from anvil import *   # to load the alert    

import anvil.users
import anvil.tables as tables
import anvil.server
from . import return_to_mother_app
from . import login_flow

"""In a URL, what travels after # is known as hash.
In an HTTP request that reaches a server (server side)
this data does not travel to the server.
Therefore, on the server side, it is not possible to retrieve it
(web browsers do not send this data in the HTTP request).
However, on the client side it is possible. """  

def confirm(h):   
    if h == None:
        return
    print(f"l'Url est: {h}")
    to_be_confirmed_email=""

    #test1: si h est type dict
    if not isinstance(h, dict):  
        print("URL not a dict type")
        return
    print("type; ", isinstance(h, dict))

    # mail in URL ?
    to_be_confirmed_email=h["email"]
    if to_be_confirmed_email == "" :
        alert("email vide")
        return
    
        
    url_purpose=h["a"]
    """ 'pw reset URL'  """
    
    if url_purpose=='pwreset':
        #alert("pwreset, going to login_flow")
        login_flow.do_email_reset(h)  
        
    """ mail confirmation URL  """
    if url_purpose=='confirm':
        #alert("confirm")
        # Hash password in URL ?
        hpw=h["hpw"]
        if not hpw:
            alert("Hash Password empty")
            return
        
        try:   
            #test3: is the user in the users data table ?
            user=anvil.server.call("search", to_be_confirmed_email, hpw)
            #Displaying the confirm alert 
            msg=user["first_name"]+", votre mail est confirmé, connectez-vous avec votre mail et mot de passe."
        except:
        #if not user:
            alert("Essayez de vous connecter.")
    
    anvil.users.logout()       #logging out the user
    #return_to_mother_app.calling_mother_app()