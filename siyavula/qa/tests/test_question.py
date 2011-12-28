import os
import unittest2 as unittest

from plone.uuid.interfaces import IUUID
from zope.component import createObject
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from z3c.relationfield.relation import create_relation
from Products.CMFCore.utils import getToolByName

from rhaptos.compilation.contentreference import CompilationSourceBinder
from rhaptos.compilation.compilation import TableOfContentsHelpers, ICompilation
from rhaptos.compilation.section import ISection 
from rhaptos.compilation.viewlets import NavigationViewlet

from base import PROJECTNAME
from base import INTEGRATION_TESTING

dirname = os.path.dirname(__file__)

class QuestionBaseTestCase(unittest.TestCase):
    """ Basic methods for all other question tests """

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])


class TestQuestion(QuestionBaseTestCase):
    """ Test a question """

    def test_allowed(self):
        pass
