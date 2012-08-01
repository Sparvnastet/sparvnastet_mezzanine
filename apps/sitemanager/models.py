from django.db import models
from django.utils.translation import ugettext as _
from mezzanine.core.fields import FileBrowseField

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
