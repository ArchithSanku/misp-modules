#!/usr/bin/env python3

import sys
import logging
import urllib3
# import urllib3pip
from pymisp import PyMISP, MISPEvent, MISPObject
# from keys import misp_url, misp_key, misp_verifycert
misp_url = 'https://18.116.32.112'
misp_key = 'uU7TIbeQlAquNHkMfcZyFAkZHoY3hi0mexahbzcR'
misp_verifycert = False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


logging.basicConfig(filename = "/home/ubuntu/xyz.txt", filemode = 'a', format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt = '%Y-%m-%d %H:%M:%S')
log = logging.getLogger('xyz')
log.setLevel(logging.DEBUG)
log.debug("Ready!!")


misp = PyMISP(misp_url, misp_key, misp_verifycert)
if not misp:
    print('PyMISP() failed\n', file=sys.stderr)
    sys.exit(1)

misp_evt = MISPEvent()
misp_evt.distribution = 4  # sharing group
misp_evt.published = False
misp_evt.sharing_group_id = 1  # depends on your instance
misp_evt.info = 'Test event with an object'
response = misp.add_event(misp_evt, pythonify=True)
if isinstance(response, dict) and 'errors' in response:
    print('add_event failed: {}'.format(response['errors']), file=sys.stderr)
    sys.exit(2)
# success
misp_evt = response
print('created evt with ID {}'.format(misp_evt.id))

misp_obj = MISPObject(name='blog', strict=True)  # standard template
misp_obj.add_attribute('post', value='some l33t text')
response = misp.add_object(misp_evt.id, misp_obj, pythonify=True)
if isinstance(response, dict) and 'errors' in response:
    print('add_object failed: {}'.format(response['errors']), file=sys.stderr)
    sys.exit(2)
# success
misp_obj = response
print('created and added obj with ID {}'.format(misp_obj['id']))
