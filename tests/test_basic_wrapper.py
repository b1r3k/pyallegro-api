import unittest

from setup import SanboxedTestCase

class WrapperTestCase(SanboxedTestCase):

    def test_login(self):
         r = self.api.login(self.login, self.password, self.apikey)
         self.assertTrue(r.userId)

    def test_soap_wrapper(self):
         self.api.login(self.login, self.password, self.apikey)
         cat_listing = self.api.doShowCat(catId=54003)
         self.assertTrue(cat_listing)

