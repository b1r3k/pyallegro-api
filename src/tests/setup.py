import unittest

from pyallegroapi import SOAPClient

import config

class SanboxedTestCase(unittest.TestCase):
    def setUp(self):
        sandbox_wsdl = 'https://webapi.allegro.pl.webapisandbox.pl/service.php?wsdl'
        self.api = SOAPClient(sandbox_wsdl)
        self.login = config.ALLEGRO_LOGIN
        self.password = config.ALLEGRO_PASSWORD
        self.apikey = config.ALLEGRO_APIKEY