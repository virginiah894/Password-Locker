# import unittest
# from credentials import Credentials
# import pyperclip
# class TestCredentials(unittest.TestCase):

#     def setUp(self):
#         '''
#         method to run before and after each test 
#         '''
#         self.new_credential = Credentials("vperry","twitter","xyz")
#     def test_proper(self):
#         '''
#         test to show if the object is initialized properly
#         '''
#         self.assertEqual(self.new_credential.username,"vperry")
#         self.assertEqual(self.new_credential.accounts,"twitter")
#         self.assertEqual(self.new_credential.password,"xyz")

#     def tearDown(self):
#         '''
#         cleans up after each test is run.
#         '''
#         Credentials.credentials_list = []
#     def test_saved_credential(self):
#         '''
#         test to show if the credentials are added into the credentials  list
#         '''
#         self.new_credential.saved_credential()
#         self.assertEqual(len(Credentials.credentials_list),1)
#     def test_remove_credential(self):
#         ''' A test for testing if we can delete a credential from  the credential  list'''
#         self.new_credential.saved_credential()
#         test_saved_credential= Credentials("vperry","twitter","xyz")
#         test_saved_credential.saved_credential()
#         self.new_credential.remove_credential()
#         self.assertEqual(len(Credentials.credentials_list),1)

#     def test_get_user_by_username(self):
#         '''
#         testing to find out if we can get the details of user using the username
#         '''
#         self.new_credential.saved_credential()
#         test_saved_credential= Credentials("vperry","twitter","xyz")
#         test_saved_credential.saved_credential()
#         found_cresential  = Credentials.find_by_username("vperry")
#         self.assertEqual(found_cresential.accounts,test_saved_credential.accounts)
#     def test_existing_user(self):
#         '''
#         test to confirm if the user is in the list,if the user does not exist we will get a flase 
#         '''
#         self.new_credential.saved_credential()
#         test_saved_credential= Credentials("vperry","twitter","xyz")
#         test_saved_credential.saved_credential()
#         existing_credental = Credentials.credentials_inlist("vperry")
#         self.assertTrue(existing_credental)
#     def test_show_users(self):
#         '''This test will list all the users'''
#         self.assertEqual(Credentials.list_all(),Credentials.credentials_list)
#     def test_copy_details(self):
#         '''
#         Test to try get all users credentials
#         '''
#         # self.new_credential.saved_credential()
#         # Credentials.copy_details("vperry","twitter","xyz")
#         # self.assertEqual(self.username.accounts .password,pyperclip.paste())





# if __name__=="__main__":
#     unittest.main()
