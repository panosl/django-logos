from django.core.exceptions import ObjectDoesNotExist
from django.contrib.syndication.views import Feed, FeedDoesNotExist
from django.contrib.sites.models import Site
from logos.conf import settings
from logos.models import Post
if settings.USE_TAGS:
    from logos.models import PostTag


class LatestPosts(Feed):
    title = Site.objects.get(pk=1).name
    link = '/blog/'
    description = ''

    def items(self):
        return Post.published.all()[:5]


if settings.USE_TAGS:
    class TagFeed(Feed):
        def get_object(self, bits):
            if len(bits) != 1:
                raise ObjectDoesNotExist
            return PostTag.objects.get(slug__exact=bits[0])

        def title(self, obj):
            return '%s feed for "%s" tag' % (Site.objects.get(pk=1).name, obj.name)

        def link(self, obj):
            if not obj:
                raise FeedDoesNotExist
            return '/blog/tag/%s' % (obj.name,)

        def items(self, obj):
            return Post.objects.filter(tags__name__in=[obj.name])
