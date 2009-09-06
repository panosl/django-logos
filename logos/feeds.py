from django.contrib.syndication.feeds import Feed
from django.contrib.sites.models import Site
from logos.models import Post


class LatestPosts(Feed):
	title = Site.objects.get(pk=1).name
	link = '/blog/'
	description = ''

	def items(self):
		return Post.published.all()[:5]
