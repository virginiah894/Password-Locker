class User:
  '''
  A class blueprint that will intantiate users
  '''
  user_list = []
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