from django.conf.urls.defaults import *
from django.contrib.sitemaps import GenericSitemap
from logos.models import Post
from logos.conf import settings
if settings.USE_TAGS:
	from tagging.views import tagged_object_list
	from logos.feeds import LatestPosts, TagFeed
	feeds = {
		'latest': LatestPosts,
		'tag': TagFeed,
	}
else:
	from logos.feeds import LatestPosts
	feeds = {
		'latest': LatestPosts,
	}


blog_dict = {
	'queryset': Post.published.all(),
	'date_field': 'pub_date',
	'allow_future': True,
}

sitemap = {
	'blog': GenericSitemap(blog_dict, priority=0.6),
}

urlpatterns = patterns('django.views.generic.date_based',
	url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[0-9A-Za-z-]+)/$',
		'object_detail',
		dict(blog_dict, slug_field='slug'),
		name='logos_post_detail'),
	url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$',
		'archive_month',
		blog_dict),
	url(r'^(?P<year>\d{4})/$',
		'archive_year',
		blog_dict,
		name='logos_year_archive'),
	url(r'^/?$',
		'archive_index',
		dict(blog_dict, num_latest=settings.NUM_LATEST, allow_empty=True),
		name='logos-archive'),
)

urlpatterns += patterns('',
	url(r'^feeds/(?P<url>.*)/$',
		'django.contrib.syndication.views.feed',
		{'feed_dict': feeds}),
)

if settings.USE_TAGS:
	urlpatterns += patterns('',
		url(r'^tag/(?P<tag>[^/]+)/$',
			tagged_object_list,
			dict(queryset_or_model=Post, paginate_by=settings.TAG_PAGINATE_BY, allow_empty=True,
				template_object_name='post'),
			name='widget_tag_detail'),
	)
