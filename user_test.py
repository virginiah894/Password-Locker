import unittest
from user import User,Credentials

# import pyperclip
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
        test_saved_user= User("tst","tstba","terry","0712389078","test@yahoo.com.com","xyz")
        test_saved_user.saved_user()
        self.assertEqual(len(User.user_list),2)
    def test_remove_user(self):
        ''' A test for testing if we can delete a user from  the user list'''
        self.new_user.saved_user()
        test_saved_user= User("tst","tstba","terry","0712389078","test@yahoo.com.com","test")
        test_saved_user.saved_user()
        self.new_user.remove_user()
        self.assertEqual(len(User.user_list),1)

# credentials tests
class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''
        method to run before and after each test 
        '''
        self.new_credential = Credentials("vperry","twitter","xyz")
    def tearDown(self):
        '''
        cleans up after each test is run.
        '''
        Credentials.credentials_list = []
    def test_proper(self):
        '''
        test to show if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.username,"vperry")
        self.assertEqual(self.new_credential.accounts,"twitter")
        self.assertEqual(self.new_credential.password,"xyz")
    def test_saved_credential(self):
        '''
        test to show if the credentials are added into the credentials  list
        '''
        self.new_credential.saved_credential()
        self.assertEqual(len(Credentials.credentials_list),1)
    def test_remove_credential(self):
        ''' A test for testing if we can delete a credential from  the credential  list'''
        self.new_credential.saved_credential()
        test_saved_credential= Credentials("vperry","twitter","xyz")
        test_saved_credential.saved_credential()
        self.new_credential.remove_credential()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_get_user_by_username(self):
        '''
        testing to find out if we can get the details of user using the username
        '''
        self.new_credential.saved_credential()
        test_saved_credential= Credentials("vperry","twitter","xyz")
        test_saved_credential.saved_credential()
        found_cresential  = Credentials.find_by_username("vperry")
        self.assertEqual(found_cresential.accounts,test_saved_credential.accounts)
    def test_existing_user(self):
        '''
        test to confirm if the user is in the list,if the user does not exist we will get a flase 
        '''
        self.new_credential.saved_credential()
        test_saved_credential= Credentials("vperry","twitter","xyz")
        test_saved_credential.saved_credential()
        existing_credental = Credentials.credentials_inlist("vperry")
        self.assertTrue(existing_credental)
    def test_show_users(self):
        '''This test will list all the users'''
        self.assertEqual(Credentials.list_all(),Credentials.credentials_list)
    def test_copy_details(self):
        '''
        Test to try get all users credentials
        '''
        # self.new_credential.saved_credential()
        # Credentials.copy_details("vperry","twitter","xyz")
        # self.assertEqual(self.username.accounts .password,pyperclip.paste())


if __name__=="__main__":
    unittest.main()
  