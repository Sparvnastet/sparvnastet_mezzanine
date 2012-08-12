from apps.sitemanager.models import PuffText, LinkRoll
from django.template.defaulttags import register

@register.simple_tag(takes_context=True)
def pufftext(context):

    context.update(
        {'puff_texts' : PuffText.objects.filter(published=True)})
    return ''

@register.simple_tag(takes_context=True)
def linkroll(context):
    context.update(
        {'link_roll' : LinkRoll.objects.filter(published=True).order_by('order')})
    return ''

