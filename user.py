class User:
  
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
    @classmethod
    def find_by_username(cls,username):
        '''
        method for searching by using the username to return the details
        '''
        for user in cls.user_list:
            if user.username == username:
                return user
    @classmethod
    def user_inlist(cls,username):
        '''Method for confirming if the username exists.the method'''
        '''
        uses username as argument to return a true or false answer
        '''
        for user in cls.user_list:
            if user.username == username:
                return True
        return False
