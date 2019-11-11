import unittest
from user import User,Credentials
import pyperclip
class TestUser(unittest.TestCase):

    '''
    creating test cases using the TestCase class
    '''
    def setUp(self):
        


        '''
        method to run before and after each test 
        '''
        self.new_user =User("Vee","Perry","0712345678","vperry@ms.com")
    def test_proper(self):
        '''
        test to show if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Vee")
        self.assertEqual(self.new_user.last_name,"Perry")
        # self.assertEqual(self.new_user.username,"vperry")
        self.assertEqual(self.new_user.number,"0712345678")
        self.assertEqual(self.new_user.email,"vperry@ms.com")
        # self.assertEqual(self.new_user.password,"xyz")



    def tearDown(self):
        '''
        cleans up after each test is run.
        '''
        User.user_list = []
    def test_saved_user(self):
        '''
        test to show if the user`s details are added into the user list
        '''
        self.new_user.saved_user()
        self.assertEqual(len(User.user_list),1)
    def test_more_users(self):
        '''
        Testing if the application can have more users in our user_list
        '''
        self.new_user.saved_user()
        test_saved_user= User("tst","tstba","0712389078","test@yahoo.com.com")
        test_saved_user.saved_user()
        self.assertEqual(len(User.user_list),2)
    def test_remove_user(self):
        ''' A test for testing if we can delete a user from  the user list'''
        self.new_user.saved_user()
        test_saved_user= User("tst","tstba","0712389078","test@yahoo.com.com")
        test_saved_user.saved_user()
        self.new_user.remove_user()
        self.assertEqual(len(User.user_list),1)

    # def test_get_user_by_name(self):
    #     '''
    #     testing to find out if we can get the details of user using the name
    #     '''
    #     self.new_user.saved_user()
    #     test_saved_user= User("tst","tstba","0712389078","test@yahoo.com.com")
    #     test_saved_user.saved_user()
    #     found_user  = User.find_by_name("tst")
    #     self.assertEqual(found_user.name,test_saved_user.name)

    # # def test_existing_user(self):
    # #     '''
    #     test to confirm if the user is in the list,if the user does not exist we will get a flase 
    #     '''
    #     self.new_user.saved_user()
    #     test_saved_user= User("tst","tstba","terry","0712389078","test@yahoo.com.com","test")
    #     test_saved_user.saved_user()
    #     existing_user = User.user_inlist("terry")
    #     self.assertTrue(existing_user)


# credentials tests
class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''
        method to run before and after each test 
        '''
        self.new_credential = Credentials("vperry","twitter","xyz")
    def test_init(self):
        '''
        test to show if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.username,"vperry")
        self.assertEqual(self.new_credential.accounts,"twitter")
        self.assertEqual(self.new_credential.password,"xyz")

    def tearDown(self):
        '''
        cleans up after each test is run.
        '''
        Credentials.credentials_list = []
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

    def test_existing_credentials(self):
        '''
        test to confirm if the user is in the list,if the user does not exist we will get a false response
        '''
        self.new_credential.saved_credential()
        test_saved_credential= Credentials("vperry","twitter","xyz")
        test_saved_credential.saved_credential()
        existing_credental = Credentials.credentials_inlist("vperry")
        self.assertTrue(existing_credental)
    def test_show_credentials(self):
        '''This test will list all the credentials'''
        self.assertEqual(Credentials.list_all(),Credentials.credentials_list)

    def test_find_credential(self):
        '''
        Tests whether a user can find a credential based on a username
        '''
        test_credential = Credentials("Virginia", "facebook", "virgyperry")
        Credentials.saved_credential(test_credential)

        self.assertEqual(Credentials.find_credential("Virginia").username, test_credential.username)

        
    # def test_copy_details(self):
    #     '''
    #     Test to try get all users credentials
    #     '''
    #     self.new_credential.saved_credential()
    #     Credentials.copy_details("vperry")
    #     self.assertEqual(self.new_credential,pyperclip.paste())


if __name__=="__main__":
    unittest.main()
  