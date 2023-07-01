import unittest

import utils


class TestUtilsMethods(unittest.TestCase):
    def test_home_page(self):
        uid = 0
        self.assertEqual(utils.get_home_page(
            uid), "https://weibo.com/u/%s" % uid)


if __name__ == '__main__':
    unittest.main()
