# Create your views here.
import os

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.core.cache import cache

from polls.models import Poll, Choice

from polls.tasks import MyTask
def foo(request):
  """View to test celery tasks"""
  MyTask.delay(some_arg='foo')
  return HttpResponse('Foo!')
  
#@login_required
#def home(request):
#  return render_to_response('index.html', {})

# Example of using cache
@login_required
def home(request):
  cache_key = 'cache_key'
  cache_time = 180 # time to live in seconds
  result = cache.get(cache_key)
  if not result:
    result = 'Cache empty!'
    cache_string = 'Cache string'
    print 'Key not found'
    cache.set(cache_key, cache_string, cache_time)
  print 'Result: %s' %result
  return render_to_response('index.html', {})

@login_required
def createPoll(request):
  return render_to_response('createPoll.html', {})

@login_required
def showPolls(request):
  polls = Poll.objects.all()
  choices = Choice.objects.all()
  return render_to_response('showPolls.html', {'polls': polls, 'choices': choices})

@login_required
def createChoice(request):
  polls = Poll.objects.all()
  return render_to_response('createChoice.html', {'polls': polls})