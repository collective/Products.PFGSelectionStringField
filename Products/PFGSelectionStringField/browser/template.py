from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class PFGSelectionStringFieldView(BrowserView):

    template = ViewPageTemplateFile('templates/selection_string.pt')

    def __call__(self):
        return self.template()
