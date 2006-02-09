#
# PlonePASTestCase
#

# $Id: PlonePASTestCase.py 18188 2006-01-19 20:48:45Z wichert $


from zope.app.tests.placelesssetup import setUp, tearDown
from Products.Five import zcml
import Products.statusmessages

from Testing import ZopeTestCase
from Products.PloneTestCase import PloneTestCase
from Products.PloneTestCase.setup import PLONE25
# Do our placeless setup if needed, this should be handled in PTC itself
# eventually
if PLONE25:
    setUp()
    zcml.load_config('meta.zcml', Products.Five)
    zcml.load_config('configure.zcml', Products.statusmessages)

PloneTestCase.setupPloneSite(products=('PlonePAS',))

from Products.PloneTestCase.PloneTestCase import FunctionalTestCase

# Stub test case just in case we need custom stuff at some point
class PlonePASTestCase(PloneTestCase.PloneTestCase):
    '''TestCase for Plone testing'''