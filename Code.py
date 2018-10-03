import testcode
import unittest
class Testcode(unittest.TestCase):
    def test_verify_correct_user_password(self):
        self.assertEqual(testcode.login('aa','bb'),1)
    def test_verify_correct_user_incorrect_password(self):
        self.assertEqual(testcode.login('aa','bbb'),0)
    def test_verify_incorrect_user_correct_password(self):
        self.assertEqual(testcode.login('aaa','bb'),0)
    def test_verify_incorrect_user_incorrect_password(self):
        self.assertEqual(testcode.login('aaa','bbb'),0)

if __name__ == '__main__':
    unittest.main()
        
