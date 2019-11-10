#!/urs/bin/env python3.6
from user import User,Credentials
def create_account_user(nameA,nameB,Pnumber,Pemail):
  '''
  Function to create a user's account
  '''
  new_user = User (nameA,nameB,Pnumber,Pemail)
  return new_user
def saving_users(user):
    ''' A function for saving  user detils'''
    user.saved_user()
def deleting_user(user):
  '''
  Function that allowes user to delete details
  '''
  user.remove_user()
def create_account_credentials(usernameA,accountsA,passwordA):
  '''
  Function to create a user's  credentials
  '''
  new_credential = Credentials (usernameA,accountsA,passwordA)
  return new_credential
def saving_credentials(credentials):
    ''' A function for saving  credential details'''
    credentials.saved_credential()
def deleting_credentials(credentials):
  '''
  Function that allowes user to delete details
  '''
  credentials.remove_credential()

def  existing_credential_list(credentials):
  '''
  function for checking if the credential is in the list
  '''
  credentials.credentials_inlist()
def  show_all_credentials(credentials):
  '''function that shows a list of all credentials in an account'''
  credentials.list_all()


