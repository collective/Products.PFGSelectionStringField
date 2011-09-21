from AccessControl import ClassSecurityInfo
from Products.ATContentTypes.content.base import registerATCT
from Products.Archetypes.public import DisplayList
from Products.Archetypes.public import LinesField
from Products.Archetypes.public import LinesWidget
from Products.Archetypes.public import Schema
from Products.Archetypes.public import SelectionWidget
from Products.Archetypes.public import StringField
from Products.CMFCore.permissions import View
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode
from Products.PFGSelectionStringField.config import PROJECTNAME
from Products.PFGSelectionStringField.interfaces import IPFGSelectionStringField
from Products.PloneFormGen.content.fields import FGSelectionField
from Products.PloneFormGen.content.fieldsBase import BaseFieldSchemaStringDefault
from Products.PloneFormGen.content.fieldsBase import finalizeFieldSchema
from Products.PloneFormGen.content.fieldsBase import vocabularyOverrideField
from Products.PloneFormGen.content.fieldsBase import vocabularyField
from zope.interface import implements

import cgi


class StringVocabularyField(StringField):
    """
    Parent for fields that have vocabularies.
    Overrides Vocabulary so that we can get the value from the instance
    """

    security  = ClassSecurityInfo()

    security.declarePublic('Vocabulary')
    def Vocabulary(self, content_instance=None):
        """
        Returns a DisplayList.
        """
        # if there's a TALES override, return it as a DisplayList,
        # otherwise, build the DisplayList from fgVocabulary

        fieldContainer = content_instance.findFieldObjectByName(self.__name__)

        vl = fieldContainer.getFgTVocabulary()
        if vl is not None:
            return DisplayList(data=vl)

        res = []
        for line in fieldContainer.fgVocabulary:
            lsplit = line.split('|')
            if len(lsplit) == 3:
                item = (lsplit[0],(lsplit[1], lsplit[2]))
            elif len(lsplit) == 2:
                item = (lsplit[0],(lsplit[1], None))
            else:
                item = (lsplit[0],(lsplit[0], None))
            res.append(item)
        return res


class SelectionStringWidget(SelectionWidget):
    _properties = SelectionWidget._properties.copy()
    _properties.update({
        'macro' : "selection_string",
        })

    # security = ClassSecurityInfo()


class PFGSelectionStringField(FGSelectionField):
    """Selection String Field"""

    # schema = FGSelectionField.schema.copy()

    schema = BaseFieldSchemaStringDefault.copy() + Schema((
        vocabularyField,
        vocabularyOverrideField,
        StringField('fgFormat',
            searchable=0,
            required=0,
            default='flex',
            enforceVocabulary=1,
            vocabulary='formatVocabDL',
            widget=SelectionWidget(
                label='Presentation Widget',
                i18n_domain = "ploneformgen",
                label_msgid = "label_fgformat_text",
                description_msgid = "help_fgformat_text",
                ),
        ),
    ))

    finalizeFieldSchema(schema, folderish=True, moveDiscussion=False)

    portal_type = 'PFGSelectionStringField'
    implements(IPFGSelectionStringField)

    def __init__(self, oid, **kwargs):
        """ initialize class """

        FGSelectionField.__init__(self, oid, **kwargs)

        # set a preconfigured field as an instance attribute
        self.fgField = StringVocabularyField('fg_selection_field',
            searchable=0,
            required=0,
            widget=SelectionStringWidget(),
            vocabulary = '_get_selection_vocab',
            enforceVocabulary=1,
            write_permission = View,
            )

    def htmlValue(self, REQUEST):
        """ Return value instead of key """
        utils = getToolByName(self, 'plone_utils')
        charset = utils.getSiteEncoding()
        value = REQUEST.form.get(self.__name__, '')
        vu = value.decode(charset)
        vocabulary = self.fgField.Vocabulary(self)
        item = dict(vocabulary).get(vu)

        if self.fgFormat == 'radio' or (self.fgFormat == 'flex' and len(vocabulary) <= 4):
            name = '%s_%s' %(self.__name__, vu)
        else:
            name = '%s_SELECT' %self.__name__
        desc = REQUEST.form.get(name, None)
        if item is None:
            return vu
        elif desc is None:
            return safe_unicode(cgi.escape(item[0].encode(charset)))
        else:
            return u'%s<br />%s' %(safe_unicode(cgi.escape(item[0].encode(charset))), safe_unicode(cgi.escape(desc.decode(charset))))


registerATCT(PFGSelectionStringField, PROJECTNAME)
