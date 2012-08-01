from django.views.generic.base import TemplateView
from mezzanine.blog.models import BlogPost
from mezzanine.pages.models import Page

__author__ = 'mathias'

class Firstpage(TemplateView):
    """ Just a simple first page, displays recent blog posts
        and PuffText in the right sidebar
    """
    template_name = 'firstpage.html'
