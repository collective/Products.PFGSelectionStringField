try:
    from Zope2.App import zcml
except ImportError:
    from Products.Five import zcml
from Products.Five import fiveconfigure
from Testing import ZopeTestCase as ztc
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

@onsetup
def setup_pfg_selection_string_field():

    fiveconfigure.debug_mode = True

    import Products.PloneFormGen
    zcml.load_config('configure.zcml', Products.PloneFormGen)
    import Products.PFGSelectionStringField
    zcml.load_config('configure.zcml', Products.PFGSelectionStringField)

    fiveconfigure.debug_mode = False

    ztc.installProduct('PFGSelectionStringField')
ztc.installProduct('PloneFormGen')
#ztc.installProduct('PFGSelectionStringField')

setup_pfg_selection_string_field()
ptc.setupPloneSite(products=['PloneFormGen', 'PFGSelectionStringField'])
class PFGSelectionStringFieldTestCase(ptc.PloneTestCase):
    """We use this base class for all the tests in this package.
    If necessary, we can put common utility or setup code in here.
    """

class PFGSelectionStringFieldFunctionalTestCase(ptc.FunctionalTestCase):
    """Test case class used for functional (doc-)tests
    """
