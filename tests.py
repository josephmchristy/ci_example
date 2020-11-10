import unittest
import task

class TestCase(unittest.TestCase):

  def test01(self):
    expected = "Hello World"
    self.assertEqual(task.my_func(), expected)
    
  def test02(self):
    expected = "Goodbye World"
    self.assertNotEqual(task.my_func(), expected)


if __name__ == '__main__':
  unittest.main()
