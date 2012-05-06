from django.utils.safestring import mark_safe
from django.utils import simplejson

def create_token(val):
	return "<div style='display:none'><input type='hidden' name='csrfmiddlewaretoken' value='%s' /></div>" %(val,);

def url(view_name, *args, **kwargs):
  from django.core.urlresolvers import reverse, NoReverseMatch
  try:
    return reverse(view_name, args=args, kwargs=kwargs)
  except NoReverseMatch:
    try:
      project_name = settings.SETTINGS_MODULE.split('.')[0]
      return reverse(project_name + '.' + view_name,
                     args=args, kwargs=kwargs)
    except NoReverseMatch:
      return ''

BASIC_FILTERS = {
  "create_token" : create_token,
  "url" : url,
}
