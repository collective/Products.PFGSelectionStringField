import unittest


class TestSelectionStringWidget(unittest.TestCase):

    def createSelectionStringWidget(self):
        from Products.PFGSelectionStringField.content.field import SelectionStringWidget
        return SelectionStringWidget()

    def test_instance(self):
        widget = self.createSelectionStringWidget()
        from Products.PFGSelectionStringField.content.field import SelectionStringWidget
        self.assertTrue(isinstance(widget, SelectionStringWidget))
        from Products.Archetypes.public import SelectionWidget
        self.assertTrue(issubclass(SelectionStringWidget, SelectionWidget))

    def test__properties(self):
        widget = self.createSelectionStringWidget()
        self.assertEqual(
            widget._properties['macro'],
            "selection_string")
