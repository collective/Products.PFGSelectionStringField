import mock
import unittest2 as unittest


class TestStringVocabularyField(unittest.TestCase):

    def createStringVocabularyField(self):
        from Products.PFGSelectionStringField.content.field import StringVocabularyField
        return StringVocabularyField('field')

    def test_instance(self):
        field = self.createStringVocabularyField()
        from Products.PFGSelectionStringField.content.field import StringVocabularyField
        self.assertTrue(isinstance(field, StringVocabularyField))
        from Products.Archetypes.public import StringField
        self.assertTrue(issubclass(StringVocabularyField, StringField))

    @mock.patch('Products.PFGSelectionStringField.content.field.DisplayList')
    def test_Vocabulary(self, DisplayList):
        field = self.createStringVocabularyField()
        content_instance = mock.Mock()
        field.Vocabulary(content_instance)
        self.assertTrue(DisplayList.called)
        content_instance.findFieldObjectByName().getFgTVocabulary.return_value = None
        content_instance.findFieldObjectByName().fgVocabulary = ['aaa', 'aaa|AAA', 'aaa|AAA|BBB']
        field.Vocabulary(content_instance)
        self.assertEqual(
            field.Vocabulary(content_instance),
            [
                ('aaa', ('aaa', None)),
                ('aaa', ('AAA', None)),
                ('aaa', ('AAA', 'BBB'))
            ]
        )
