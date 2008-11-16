from django.db import models
from django.utils.translation import gettext_lazy as _



class Post(models.Model):
	title = models.CharField(_('title'), max_length=30)
	slug = models.SlugField()
	pub_date = models.DateTimeField(_('date published'))
	body = models.TextField(_('body text'), blank=True)

	class Meta:
		ordering = ('-pub_date',)
		verbose_name = _('post')
		verbose_name_plural = _('posts')

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return '/blog/%s/%s/' % (self.pub_date.strftime('%Y/%b/%d').lower(), self.slug)
