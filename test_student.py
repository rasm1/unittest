import unittest
from student import Student

class TestStudent(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print('setUpClass')
        
    @classmethod
    def tearDownClass(cls):
        print("teardownClass")

    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Doe')


    def tearDown(self):
        print('teardown')


    def test_full_name(self):
       print('test_full_name')
       self.assertEqual(self.student.full_name,"John Doe")

    def test_alert_santa(self):
        print('test_email')
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        print('test_alert_santa')
        self.assertEqual(self.student.email, "john.doe@email.com")

if __name__== '__main__':
    unittest.main()

