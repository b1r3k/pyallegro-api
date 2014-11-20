# -*- coding: UTF-8 -*-
import hashlib
import socket
import logging
import time

import suds

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

hdl = logging.StreamHandler()
hdl.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M'))

logger.addHandler(hdl)

WSDL_URL = 'http://webapi.allegro.pl/uploader.php?wsdl'

class SOAPClient(suds.client.Client):

    def __init__(self, wsdl_url=WSDL_URL, cache=None, country_code=1, retry_limit = 10, retry_delay = 5):
        super(SOAPClient, self).__init__(wsdl_url)

        self.set_options(cache=cache)
        self.country_code = country_code
        self._session = None
        self._allegro_username = None
        self._allegro_password = None
        self._allegro_apikey = None
        self._retry_count = 0
        self._retry_limit = retry_limit
        self._retry_delay = retry_delay


    def login(self, username, password, user_apikey):
        """
        Obtain session for given credentials

        :param username:
        :param password:
        :param user_apikey:
        :return:
        """
        sys_status = self.service.doQuerySysStatus(1, self.country_code, user_apikey)
        password_encoded = hashlib.sha256(password).digest().encode('base64')

        response = self.service.doLoginEnc(username,
                                           password_encoded,
                                           self.country_code,
                                           user_apikey,
                                           sys_status.verKey)

        self._session = response.sessionHandlePart
        self._allegro_username = username
        self._allegro_password = password
        self._allegro_apikey = user_apikey
        self._allegro_version_key = sys_status.verKey

        return response


    def __getattribute__(self, name):
        try:
            return super(SOAPClient, self).__getattribute__(name)
        except AttributeError:
            api_method = getattr(self.service, name)
            return self._get_api_method(api_method)


    def _get_api_method(self, method_name):
        """
        A wrapper around suds components. Adds common parameters
        to each call as well as handles session expiration gracefully.
        """
        def _service(*args, **kwargs):
            kwargs['countryCode'] = self.country_code
            kwargs['webapiKey'] = self._allegro_apikey
            kwargs['localVersion'] = self._allegro_version_key
            kwargs['sessionHandle'] = self._session

            try:
                return method_name(*args, **kwargs)

            except suds.WebFault as exc:
                if exc.fault.faultcode in ['ERR_NO_SESSION', 'ERR_SESSION_EXPIRED']:
                    logger.debug('Session expired while in method: %s, args: %s, kwargs: %s' % (method_name, args, kwargs))
                    self.login(self._allegro_username, self._allegro_password, self._allegro_apikey)
                    return method_name(*args, **kwargs)

        return _service