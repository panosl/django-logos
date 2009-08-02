from django.db import models
from django.utils.translation import gettext_lazy as _
from logos.conf import settings
if settings.USE_TAGS:
	from tagging.fields import TagField


class PublicPostManager(models.Manager):
	def get_query_set(self):
		return super(PublicPostManager, self).get_query_set().filter(is_published=True)

class Post(models.Model):
	title = models.CharField(_('title'), max_length=30)
	slug = models.SlugField()
	pub_date = models.DateTimeField(_('date published'))
	body = models.TextField(_('body text'), blank=True)
	is_published = models.BooleanField(_('it is published'), default=True,
		help_text=_('Determines if it will be displayed at the website.'))
	if settings.USE_TAGS:
		tags = TagField()

	objects = models.Manager()
	published = PublicPostManager()

	class Meta:
		ordering = ('-pub_date',)
		verbose_name = _('post')
		verbose_name_plural = _('posts')

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return '/blog/%s/%s/' % (self.pub_date.strftime('%Y/%b/%d').lower(), self.slug)
