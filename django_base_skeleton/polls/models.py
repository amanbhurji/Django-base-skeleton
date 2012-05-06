from django.db import models

# Create your models here.
class Poll(models.Model):
  question = models.CharField(max_length=200)
  pub_date = models.DateField('date published')
  polling_ended = models.BooleanField() #added to demonstrate South. So, if you want to try south, create the initial db with this commented
  #created = models.DateTimeField(auto_now_add=True) #added to demonstrate South. So, if you want to try south, create the initial db with this commented
  def __unicode__(self):
    return self.question
    
class Choice(models.Model):
  poll = models.ForeignKey(Poll)
  choice = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

  def __unicode__(self):
    return self.poll.question + " - " + self.choice
