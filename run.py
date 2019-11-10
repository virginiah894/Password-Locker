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


def main():

  Print (" Welcome Passord Locker.")

  print("Please Write your name")
      new_name = input()
      print("{new_name}. What do you want to do?")
      print("\n")
      print ("Use this codes: \n CUA-create user account\ AC-Add your credentials\q-leave the application")
      user_code = input().upper().strip()
      if user_code=='q':
            break
      elif user_code=="CUA":
        print("New Contact")
                            print("New User Details)

                            print ("Please enter your first name ....")
                              nameA = input()

                            print("Please enter your last name ...")
                            nameB = input()

                            print("Please enter your Phone number ...")
                            Pnumber = input()

                            print("Plase Enter your email address ...")
                            Pemail = input()
                            saving_users(create_account_user(nameA,nameB,Pnumber,Pemail))
                            '''
                            This creates and saves user details
                            '''
                            print ("Here are your account Details" {nameA}){nameB}{Pnumber}{Pemail})
                            print("\n")


      elif user_code =="AC":
                            print('To signup, enter your credentials :')
                      
                            print("Enter your preferred Username ").strip()
                            usernameA =input()
                            print("Enter your referrence account  eg facebook,twitter").strip()
                            accountsA = input()
                            print("Enter your preferred Password ").strip()
                            passwordA = input()
                            saving_credentials(create_account_credentials(usernameA,accountsA,passwordA))
                            '''
                            function that takes the user input on credentials and saves the credentials
                            '''
                            existing_credential_list(saving_credentials(usernameA,accountsA,passwordA))
                            '''
                            Function to confirm if the Credentials are in the list
                            '''
                            if existing_credential_list == (usernameA,accountsA,passwordA)
                                    print("Dear {usernameA}.Select the options below to continue")
                            While True:
                                    print(f "Hi {usernameA}.Select an option")
                                    print('')
                                    print("Here are the codes:SC-show credentials\ GC -get generated password\CP-Create your password\q ")
                                    access_code =input("Enter your response").lower()
                                    print("-"*60)
                                    if access_code=="q":
                                      print("Goodbye")
                                          break
                                    elif access_code=="SC":
                                      print(" ")
                                    if existing_credential_list == existing_credential_list:
                                      print({"usernameA}.{accountsA},{passwordA}")
                                      else:
                                        print(" Credentials do not match")
                                    if access_code ="GC":
                                      print(" Your Password will be autogenerated")
                                      password = "xyzabc"
                                      print("{password}")

                            
                                    elif access_code="CP":
                                      print("Enter your preffered password here")
                                      new_password =input().lower 
                                      print ("Your password is {new_password}")
                                    




                                      


  
        
  
