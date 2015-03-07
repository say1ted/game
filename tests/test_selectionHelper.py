from unittest import TestCase
from core.helpers import SelectionHelper


class TestSelectionHelper(TestCase):
    def setUp(self):
        list = ['123', '321']
        self.helper = SelectionHelper(list)

    def test_valid(self):
        self.assertTrue(self.helper.valid('2'))
        self.assertFalse(self.helper.valid('5'))

    def test_get_elem(self):
        result = self.helper.get_elem('1')
        self.assertTrue(result == '123')