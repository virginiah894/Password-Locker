# import pyperclip
# class Credentials:

#     '''

#     A class for generating the username and password
#     '''
#     credentials_list=[]

#     '''
#     An empty list that will be a blueprint for credentials
#     '''
    
            
#         # User_credentials 
#     def __proper__(self,username,accounts,password):
#         '''
#         An blueprint for the credentials class
#         '''
#         self.username = username
#         self.accounts = accounts
#         self.password = password
        
                
                
#     def saved_credential(self):
#         Credentials.credentials_list.append(self)
#     def remove_credential(self):
#         '''
#         method for removing a user from the user list
#         '''
#         Credentials.credentials_list.remove(self)

            

#     @classmethod
#     def find_by_username(cls,username):
#         '''
#         method for searching by using the username to return the details
#         '''
#         for credentials in cls.credentials_list:
#             if credentials.username == username:
#                 return credentials
#     @classmethod
#     def credentials_inlist(cls,username):
#         '''Method for confirming if the username exists.the method'''
#         '''
#         uses username as argument to return a true or false answer
#         '''
#         for credentials in cls.credentials_list:
#             if credentials.username == username:
#                 return True
#             return False
                
                
#     @classmethod
#     def list_all(cls):
#         return cls.credentials_list
#     # @classmethod
#     # def copy_details(cls,username):
#     #     credentials_details = credentials_details.find_by_username(username)
#     #     pyperclip.copy(credentials_details.first_name.last_name.username .number.email.password)
