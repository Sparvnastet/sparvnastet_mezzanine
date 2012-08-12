from django.db import models
from django.utils.translation import ugettext as _
from mezzanine.core.fields import FileBrowseField
from south.modelsinspector import add_introspection_rules


# Add rules to South for migrating non-default Django fields
# See http://south.readthedocs.org/en/latest/customfields.html#extending-introspection
add_introspection_rules([], ["^filebrowser_safe\.fields\.FileBrowseField"])

class PuffText(models.Model):
    """ Shorter text blocks to appear in the sidebar """

    title = models.CharField(max_length=255, verbose_name=_('title'))
    image = FileBrowseField("Image", directory="images/", max_length=255,
        extensions=['.jpg', '.png', '.gif'],
        blank=True, null=True)
    content = models.TextField(verbose_name=_('content'), blank=True, null=True)
    published = models.BooleanField(default=True, verbose_name=_('published'))

    def __unicode__(self):
        return u'%s' % self.title


class LinkRoll(models.Model):
    """ URL's to other sites """
    url = models.URLField(verbose_name=_('url'))
    name = models.CharField(verbose_name=_('name'), max_length=255, blank=True, null=True)
    description = models.CharField(verbose_name=_('descrption'), max_length=255, blank=True, null=True)
    order = models.IntegerField(default=1)
    published = models.BooleanField(verbose_name=_('published'), default=True)

    def __unicode__(self):
        if self.name:
            return u'%s' % self.name
        return u'%s' % self.url

    class Meta:
        verbose_name = 'link'
        verbose_name_plural = 'links'

