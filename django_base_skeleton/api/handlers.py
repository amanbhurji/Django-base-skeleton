from piston.handler import BaseHandler
from piston.utils import rc, translate_mime
from polls.models import Poll, Choice
import utils

class CalcHandler( BaseHandler ):
  def read( self, request, expression ): #called for a get request
    return eval( expression )

class PollHandler( BaseHandler ):
  allowed_methods = ('GET', 'POST', 'PUT')
  # if you want to disable a request just remove it from the tuple
  model = Poll
  #fields = ('question', 'pub_date', ) # this determines what fields of the above mentioned model are to be included in the JSON response

  def read( self, request, id=None ): #called for a GET request
    if id:
      try:
        return Poll.objects.get(id=id)
      except Poll.DoesNotExist, e:
        return {}
    else:
      return Poll.objects.all()

  def create( self, request, id=None ): #called for a POST request
    #When making a POST request, data has to be sent with the request, same goes with PUT
    #eg - In jQuery ajax {"a":null} works but {} doesn't
    #print "GOT CREATE (POST) request on /api/poll/"
    if not id: #id should always be None here
      try:
        question = request.POST.get('question')
        pub_date = utils.dateFromString(request.POST.get('pubDate'))
        if question and pub_date:
          poll = Poll()
          poll.question = question
          poll.pub_date = pub_date
          poll.polling_ended = False
          poll.save()
          
          return poll
      except Exception, e:
        resp = rc.BAD_REQUEST
        resp.write("Error creating 'Poll' object")
        return resp

  def update( self, request ): #called for a PUT request
    print "GOT UPDATE (PUT) request on /api/poll/"

class ChoiceHandler( BaseHandler ):
  allowed_methods = ('GET', 'POST', 'PUT')
  model = Choice
  #fields = ('choice', 'votes', ('poll', ('question', 'pub_date', 'polling_ended'))) #fields can also be nested
  
  #customize the return JSON for the poll field to be the id instead of the complete JSON for poll
  @classmethod
  def poll(cls, model):
    if model.poll:
      return model.poll.id
    else:
      return None

  def read( self, request, id=None, action=None ):

    if id:        
      try:
        choice = Choice.objects.get(id=id)
        if request.user and action:
          choice.votes = choice.votes+1
          choice.save()
          
        return choice
      except Choice.DoesNotExist, e:
        return {}
    else:
      return Choice.objects.all()

  def create( self, request, id=None, action=None ):
    if not id: #id should always be None here
      try:
        pollId = request.POST.get('pollId')
        choiceText = request.POST.get('choice')
        try:
          poll = Poll.objects.get(id=pollId)
          if poll and choiceText:
            choice = Choice()
            choice.poll = poll
            choice.choice = choiceText
            choice.save()

            return choice
        except Poll.DoesNotExist, e:
          resp = rc.BAD_REQUEST
          resp.write("Error fetching 'Poll' object")
          return resp
      except Exception, e:
        resp = rc.BAD_REQUEST
        resp.write("Error creating 'Choice' object")
        return resp

  def update( self, request, id=None, action=None ):
    #print "GOT UPDATE (PUT) request on /api/choice/"
    print "action:", action