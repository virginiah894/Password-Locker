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


  
if __name__=="__main__":
    unittest.main()
  