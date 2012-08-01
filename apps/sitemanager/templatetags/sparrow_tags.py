from apps.sitemanager.models import PuffText
from django.template.defaulttags import register

@register.simple_tag(takes_context=True)
def pufftext(context):

    context.update({'puff_texts' : PuffText.objects.filter(published=True)})
    return ''



