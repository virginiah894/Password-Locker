class User:
    # import pyperclip
  
    '''
    A class blueprint that will intantiate users
    '''
    user_list=[]
    
    def __init__(self,first_name,last_name,username,number,email,password):

        '''
        constructor with all class parameters
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.number = number
        self.email = email
        self.password = password
    def saved_user(self):
        User.user_list.append(self)
    
    def remove_user(self):
        '''
        method for removing a user from the user list
        '''
        User.user_list.remove(self)
class Credentials:
    '''
    A class for generating the username and password
    '''
    credentials_list=[]
    '''
    An empty list that will be a blueprint for credentials
    '''
    # User_credentials 
    def __init__(self,username,accounts,password):
        
        '''
        An blueprint for the credentials class
        '''
        self.username = username
        self.accounts = accounts
        self.password = password
    def saved_credential(self):
        Credentials.credentials_list.append(self)
    def remove_credential(self):
        '''
        method for removing a user from the user list
        '''
        Credentials.credentials_list.remove(self)

    

    # @classmethod
    # def find_by_username(cls,username):
    #     '''
    #     method for searching by using the username to return the details
    #     '''
    #     for credentials in cls.credentials_list:
    #         if credentials.username == username:
    #             return username
    @classmethod
    def credentials_inlist(cls,username):
        '''Method for confirming if the username exists.the method'''
        '''
        uses username as argument to return a true or false answer
        '''
        for credentials in cls.credentials_list:
            if credentials.username == username:
                return True
        return False
    @classmethod
    def list_all(cls):
        return cls.credentials_list
    # @classmethod
    # def copy_details(cls,username):
    #     user_details = User.find_by_username(username)
    #     pyperclip.copy(user_details.first_name.last_name.username .number.email.password)
