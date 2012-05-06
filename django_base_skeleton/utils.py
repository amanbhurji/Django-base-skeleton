import datetime
import time

def dateFromString(date):
  if isinstance(date, str) or isinstance(date, unicode):
    try:
      dateStruct_aux = time.strptime(date, "%m/%d/%Y")
      date = datetime.date(dateStruct_aux.tm_year, dateStruct_aux.tm_mon, dateStruct_aux.tm_mday)
    except ValueError, vErr:
      print "dateFromString >> Received exception %s. Forcing date = None" % vErr
      date = None
    return date
  elif isinstance(date, datetime.date) or (date is None):
    return date
  else:
    print "Received a type %s. Only string/unicode or datetime.date allowed" % type(date)