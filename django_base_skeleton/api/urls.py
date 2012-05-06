from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from api.handlers import CalcHandler, PollHandler, ChoiceHandler

class CsrfExemptResource( Resource ):
  def __init__( self, handler, authentication = None ):
    super( CsrfExemptResource, self ).__init__( handler, authentication )
    self.csrf_exempt = getattr( self.handler, 'csrf_exempt', True )

calc_resource = CsrfExemptResource( CalcHandler )
poll_resource = CsrfExemptResource( PollHandler )
choice_resource = CsrfExemptResource( ChoiceHandler )

urlpatterns = patterns( '',
  url( r'^calc/(?P<expression>.*)$', calc_resource ), #even though it says ^calc it takes the path api/calc as this file is included using the ^api/ path
  url( r'^poll/(?P<id>.*)$', poll_resource),
  url( r'^poll/$', poll_resource),
  url( r'^choice/(?P<id>\d*)$', choice_resource),
  url( r'^choice/(?P<id>\d*)/(?P<action>increment)$', choice_resource),
  url( r'^choice/$', choice_resource),
)