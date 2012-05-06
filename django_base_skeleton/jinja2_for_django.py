from django.template.loader import BaseLoader
from django.template.loaders.app_directories import app_template_dirs
from django.template import TemplateDoesNotExist
from django.core import urlresolvers
from django.conf import settings
import jinja2
import settings
from basic_filters import BASIC_FILTERS

class Template(jinja2.Template):
  def render(self, context):
    # flatten the Django Context into a single dictionary.
    context_dict = {}
    for d in context.dicts:
      context_dict.update(d)
    return super(Template, self).render(context_dict)

class Loader(BaseLoader):
  is_usable = True

  env = jinja2.Environment(loader=jinja2.FileSystemLoader(settings.TEMPLATE_DIRS + app_template_dirs))
  env.template_class = Template

  # These are available to all templates.
  env.globals['url_for'] = urlresolvers.reverse
  env.globals['MEDIA_URL'] = settings.MEDIA_URL
  #env.globals['STATIC_URL'] = settings.STATIC_URL
  env.filters.update(BASIC_FILTERS)

  def load_template(self, template_name, template_dirs=None):
    try:
      template = self.env.get_template(template_name)
    except jinja2.TemplateNotFound:
      raise TemplateDoesNotExist(template_name)
    return template, template.filename
