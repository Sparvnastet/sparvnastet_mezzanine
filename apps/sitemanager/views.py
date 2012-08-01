from django.views.generic.base import TemplateView
from mezzanine.blog.models import BlogPost
from mezzanine.pages.models import Page

__author__ = 'mathias'

class Firstpage(TemplateView):
    """ Just a simple first page, displays recent blog posts
        and PuffText in the right sidebar
    """

    template_name = 'firstpage.html'
    def get_context_data(self, **kwargs):
        context = super(Firstpage, self).get_context_data(**kwargs)
        context['blog_post'] = BlogPost.objects.get(pk=1)
        try:
            context['about'] = Page.objects.get(slug='sparvnastet')
            print context['about']
            print dir(context['about'])
        except Page.DoesNotExist:
            pass
        return context
  