from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from django_comments.moderation import CommentModerator, moderator

from logos.conf import settings
if settings.USE_TAGS:
    from slugify import slugify
    from taggit.managers import TaggableManager
    from taggit.models import Tag, TaggedItem


if settings.USE_TAGS:
    class PostTag(Tag):
        class Meta:
            proxy = True

        def slugify(self, tag, i=None):
            slug = slugify(tag)
            if i is not None:
                slug += "_%d" % i
            return slug


    class TaggedPost(TaggedItem):
        class Meta:
            proxy = True

        @classmethod
        def tag_model(self):
            return PostTag


class PublicPostManager(models.Manager):
    def get_query_set(self):
        return super(PublicPostManager, self).get_query_set().filter(is_published=True)


class BasePost(models.Model):
    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField()
    pub_date = models.DateTimeField(_('date published'))
    body = models.TextField(_('body text'), blank=True)
    is_published = models.BooleanField(_('it is published'), default=True,
        help_text=_('Determines if it will be displayed at the website.'))

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title


class Post(BasePost):
    allow_comments = models.BooleanField(default=True)
    is_pinned = models.BooleanField(_('is it pinned?'), default=False,
        help_text=_('Determines if it will remain on top even if newer posts are made.'))
    if settings.USE_TAGS:
        tags = TaggableManager(through=TaggedPost, blank=True)

    objects = models.Manager()
    published = PublicPostManager()

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        app_label = 'logos'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('logos_post_detail', kwargs={
            'year': self.pub_date.year,
            'month': self.pub_date.strftime('%b').lower(),
            'day': self.pub_date.day,
            'slug': self.slug,
        })


class PostModerator(CommentModerator):
    enable_field = 'allow_comments'
    email_notification = True


moderator.register(Post, PostModerator)
