from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.comments.moderation import CommentModerator, moderator
from logos.conf import settings
if settings.USE_TAGS:
	from tagging.fields import TagField


class PublicPostManager(models.Manager):
	def get_query_set(self):
		return super(PublicPostManager, self).get_query_set().filter(is_published=True)

class Post(models.Model):
	title = models.CharField(_('title'), max_length=100)
	slug = models.SlugField()
	pub_date = models.DateTimeField(_('date published'))
	body = models.TextField(_('body text'), blank=True)
	allow_comments = models.BooleanField(default=True)
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

	@models.permalink
	def get_absolute_url(self):
		return ('logos_post_detail', (), {
			'year': self.pub_date.year,
			'month': self.pub_date.strftime('%b').lower(),
			'day': self.pub_date.day,
			'slug': self.slug,
		})

class PostModerator(CommentModerator):
	enable_field = 'allow_comments'
	email_notification = True


moderator.register(Post, PostModerator)
