from Products.CMFCore.utils import getToolByName
from Products.PFGSelectionStringField.tests.base import IntegrationTestCase


class TestSetup(IntegrationTestCase):

    def setUp(self):
        self.portal = self.layer['portal']

    def test_package_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('PFGSelectionStringField'))

    def test_pfg_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('PloneFormGen'))

    def test_factorytool__PFGSelectionStringField(self):
        factory = getToolByName(self.portal, 'portal_factory')
        self.assertTrue(factory.getFactoryTypes()['PFGSelectionStringField'])

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-Products.PFGSelectionStringField:default'), u'1')

    def test_propertiestool__not_searchable(self):
        properties = getToolByName(self.portal, 'portal_properties')
        site_properties = getattr(properties, 'site_properties')
        self.assertIn('PFGSelectionStringField', list(site_properties.getProperty('types_not_searched')))

    def test_propertiestool__use_folder_tabs(self):
        properties = getToolByName(self.portal, 'portal_properties')
        site_properties = getattr(properties, 'site_properties')
        self.assertNotIn('PFGSelectionStringField', site_properties.getProperty('use_folder_tabs'))

    def test_proepertiestool__typesLinkToFolderContentsInFC(self):
        properties = getToolByName(self.portal, 'portal_properties')
        site_properties = getattr(properties, 'site_properties')
        self.assertNotIn('PFGSelectionStringField', site_properties.getProperty('typesLinkToFolderContentsInFC'))

    def test_propertiestool__not_in_navtree(self):
        properties = getToolByName(self.portal, 'portal_properties')
        navtree_properties = getattr(properties, 'navtree_properties')
        self.assertIn('PFGSelectionStringField', list(navtree_properties.getProperty('metaTypesNotToList')))

    def test_rolemap__Add_PFGSelectionStringField__rolesOfPermission(self):
        permission = "Add PFGSelectionStringField"
        roles = [
            item['name'] for item in self.portal.rolesOfPermission(
                permission) if item['selected'] == 'SELECTED']
        roles.sort()
        self.assertEqual(
            roles, ['Editor', 'Manager', 'Site Administrator'])

    def test_rolemap__Add_PFGSelectionStringField__acquiredRolesAreUsedBy(self):
        permission = "Add PFGSelectionStringField"
        self.assertEqual(
            self.portal.acquiredRolesAreUsedBy(permission), '')

    def test_skins__PFGSelectionStringField__SkinPath(self):
        skins = getToolByName(self.portal, 'portal_skins')
        paths = skins.getSkinPaths()[0][1].split(',')
        self.assertEqual(
            paths.index('PFGSelectionStringField'),
            paths.index('PloneFormGen') - 1)

    def test_skins_PFGSelectionStringField__DirPath(self):
        skins = getToolByName(self.portal, 'portal_skins')
        self.assertEqual(
            skins['PFGSelectionStringField'].getDirPath(),
            'Products.PFGSelectionStringField:skins/PFGSelectionStringField')

    def test_skins_PFGSelectionStringField__meta_type(self):
        skins = getToolByName(self.portal, 'portal_skins')
        self.assertEqual(
            skins['PFGSelectionStringField'].meta_type,
            'Filesystem Directory View')

    def test_types__PFGSelectionStringField__metatype(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('PFGSelectionStringField')
        self.assertEqual(ctype.meta_type, 'Factory-based Type Information with dynamic views')

    def test_types__PFGSelectionStringField__title(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('PFGSelectionStringField')
        self.assertEquals(ctype.title, 'Selection String Field')

    def test_types__PFGSelectionStringField__description(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('PFGSelectionStringField')
        self.assertEquals(ctype.description, '')

    def test_types__PFGSelectionStringField__content_meta_type(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('PFGSelectionStringField')
        self.assertEquals(ctype.content_meta_type, 'PFGSelectionStringField')

    def test_types__PFGSelectionStringField__factory(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('PFGSelectionStringField')
        self.assertEquals(ctype.factory, 'addPFGSelectionStringField')

    def test_types__PFGSelectionStringField__immediate_view(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('PFGSelectionStringField')
        self.assertEquals(ctype.immediate_view, 'fg_base_view_p3')

    def test_types__PFGSelectionStringField__global_allow(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('PFGSelectionStringField')
        self.assertFalse(ctype.global_allow)

    def test_types__PFGSelectionStringField__filter_content_types(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('PFGSelectionStringField')
        self.assertFalse(ctype.filter_content_types)

    def test_types__PFGSelectionStringField__allowed_content_types(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('PFGSelectionStringField')
        self.assertEqual(ctype.allowed_content_types, ())

    def test_types__PFGSelectionStringField__default_view(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('PFGSelectionStringField')
        self.assertEqual(ctype.default_view, 'fg_base_view_p3')

    def test_types__PFGSelectionStringField__view_methods(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('PFGSelectionStringField')
        self.assertEqual(ctype.view_methods, ('fg_base_view_p3',))

    def test_types__PFGSelectionStringField__aliases(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('PFGSelectionStringField')
        self.assertEqual(
            ctype.getMethodAliases(), {
                '(Default)': '(dynamic view)',
                'edit': 'atct_edit',
                'sharing': '@@sharing',
                'view': '(selected layout)'
            })

    def test_types__FormFolder__allowed_content_types(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('FormFolder')
        self.assertIn('PFGSelectionStringField', ctype.allowed_content_types)

    def test_workflow(self):
        workflow = getToolByName(self.portal, 'portal_workflow')
        self.assertEquals((), workflow.getChainForPortalType('PFGSelectionStringField'))

    def test_uninstall__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['PFGSelectionStringField'])
        self.assertFalse(installer.isProductInstalled('PFGSelectionStringField'))

    def test_uninstall__types__PFGSelectionStringFielder(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['PFGSelectionStringField'])
        types = getToolByName(self.portal, 'portal_types')
        self.assertIsNone(types.getTypeInfo('PFGSelectionStringField'))
