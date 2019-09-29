"""Tests custom class for appropriate error handling."""
import unittest

import cls_human_error
import cls_human as my_cls


class HumanTestCase(unittest.TestCase):
    def test_real_human(self):
        samus = my_cls.Human('Samus', 'Aran')
        samus.introduction()
        self.assertEqual(samus.last_name, 'Aran')
        self.assertIsNotNone(samus.first_name)

    def test_is_samus(self):
        with self.assertRaises(cls_human_error.HumanError):
            my_cls.Human('Joe', 'Blow')


if __name__ == '__main__':
    unittest.main()