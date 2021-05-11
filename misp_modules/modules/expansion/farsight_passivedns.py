import urllib3
from pymisp import PyMISP, MISPEvent, MISPObject
import logging
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logging.basicConfig(filename = "/home/ubuntu/qwert.txt", filemode = 'a', format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt = '%Y-%m-%d %H:%M:%S')
log = logging.getLogger('Testtt')
log.setLevel(logging.DEBUG)
log.debug("......DEBUG.......")


misp_url = 'https://18.116.32.112'
misp_key = 'uU7TIbeQlAquNHkMfcZyFAkZHoY3hi0mexahbzcR'
misp_verifycert = False


misp = PyMISP(misp_url, misp_key, misp_verifycert)
log.debug("......DEBUG123.......")

misp_evt = MISPEvent()
misp_evt.distribution = 4  # sharing group
misp_evt.published = False
misp_evt.sharing_group_id = 1  # depends on your instance
misp_evt.info = 'pycharm tTest'
response = misp.add_event(misp_evt, pythonify=True)

misp_evt = response

misp_obj = MISPObject(name='blog', strict=True)  # standard template
misp_obj.add_attribute('post', value='some l33t text')
response = misp.add_object(misp_evt.id, misp_obj, pythonify=True)

misp_obj = response
