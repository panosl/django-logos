from django.contrib.syndication.feeds import Feed
from logos.models import Post


class LatestPosts(Feed):
	title = u'emporikos sullogos'	
	link = '/blog/'
	description = ''

	def items(self):
		return Post.published.all()[:5]
