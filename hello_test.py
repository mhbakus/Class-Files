import hello
import unittest


class HelloTest(unittest.TestCase):

    def test_can_say_hello_to_mohamed(self):
        self.assertEqual(hello.say_hello('Mohamed', 'Amaka'))

    def test_foo(self):
        self.assertFalse(True)   


if __name__ == '__main__':
    unittest.main()
