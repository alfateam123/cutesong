import requests
import unittest
import cutesong as qt

class TestList(unittest.TestCase):
    def setUp(self):
        self.list_response = requests.get("http://openings.moe/api/list.php").json()
        self.filenames_response = requests.get("http://openings.moe/api/list.php?filenames").json()

    def test_list(self):
        self.assertEqual(qt.list(), self.list_response)

    def test_filenames(self):
        self.assertEqual(qt.filenames(), self.filenames_response)
