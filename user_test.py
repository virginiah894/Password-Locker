import unittest
from user import User
class TestUser(unittest.TestCase):

    '''
    creating test cases using the TestCase class
    '''
    def setUp(self):
        '''
        method to run before and after each test 
        '''
        self.new_user =User("Vee","Perry","vperry","0712345678","vperry@ms.com","xyz")
    def tearDown(self):
        '''
        cleans up after each test is run.
        '''
        User.user_list = []
    def test_proper(self):
        '''
        test to show if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Vee")
        self.assertEqual(self.new_user.last_name,"Perry")
        self.assertEqual(self.new_user.username,"vperry")
        self.assertEqual(self.new_user.number,"0712345678")
        self.assertEqual(self.new_user.email,"vperry@ms.com")
        self.assertEqual(self.new_user.password,"xyz")
    def test_saved_user(self):
        '''
        test to show if the user`s details are added into the user list
        '''
        self.new_user.saved_user()
        self.assertEqual(len(User.user_list),1)
    def test_more_user_saved(self):
        '''
        Testing if the application can have more users in our user_list
        '''
        self.new_user.saved_user()
        test_saved_user= User("tst","tstba","terry","0712389078","test@yahoo.com.com","test")
        test_saved_user.saved_user()
        self.assertEqual(len(User.user_list),2)
    def test_remove_user(self):
        ''' A test for testing if we can delete a user from  the user list'''
        self.new_user.saved_user()
        test_saved_user= User("tst","tstba","terry","0712389078","test@yahoo.com.com","test")
        test_saved_user.saved_user()
        self.new_user.remove_user()
        self.assertEqual(len(User.user_list),1)
    def test_get_user_by_username(self):
        '''
        testing to find out if we can get the details of user using the username
        '''
        self.new_user.saved_user()
        test_saved_user= User("tst","tstba","terry","0712389078","test@yahoo.com.com","test")
        test_saved_user.saved_user()
        found_user  = User.find_by_username("terry")
        self.assertEqual(found_user.email,test_saved_user.email)

if __name__=="__main__":
    unittest.main()
  