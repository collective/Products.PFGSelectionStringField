from Products.Archetypes import atapi
from Products.CMFCore import utils
from Products.CMFCore.permissions import setDefaultRoles
from Products.PFGSelectionStringField.config import ADD_PERMISSIONS
from Products.PFGSelectionStringField.config import PROJECTNAME
from zope.i18nmessageid import MessageFactory


PFGSelectionStringFieldMessageFactory = MessageFactory(PROJECTNAME)

setDefaultRoles(
    "Add PFGSelectionStringField",
    ('Manager', 'Contributor', 'Owner',)
)


def initialize(context):
    """Initializer called when used as a Zope 2 product."""

    content_types, constructors, ftis = atapi.process_types(
        atapi.listTypes(PROJECTNAME),
        PROJECTNAME
    )

    for atype, constructor in zip(content_types, constructors):
        utils.ContentInit(
        '{0}: {1}'.format(PROJECTNAME, atype.portal_type),
            content_types=(atype,),
            permission=ADD_PERMISSIONS[atype.portal_type],
            extra_constructors=(constructor,),
        ).initialize(context)
