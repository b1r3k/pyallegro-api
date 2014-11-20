import unittest

import mock
from suds import WebFault

from setup import SanboxedTestCase

class ExceptionsTestCase(SanboxedTestCase):

    def test_handling_webfault(self):
        def side_effect(*args, **kwargs):
            fault_obj = mock.MagicMock()
            fault_obj.faultcode = 'ERR_NO_SESSION'
            raise WebFault(fault_obj, None)

        self.api.login(self.login, self.password, self.apikey)

        mocked = mock.MagicMock()
        mocked.doShowCat.side_effect=side_effect
        self.api.service = mocked

        with self.assertRaises(WebFault):
            self.api.doShowCat(catId=54003)

        # Webfault can mean that session has expired therefore we are going to login again
        self.assertTrue(mocked.doLoginEnc.called)
        # and call our method again
        self.assertEqual(mocked.doShowCat.call_count, 2)


if __name__ == '__main__':
    unittest.main()
