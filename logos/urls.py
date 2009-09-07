from django.conf.urls.defaults import *
from tagging.views import tagged_object_list
from logos.models import Post
from logos.feeds import LatestPosts, TagFeed

blog_dict = {
	'queryset': Post.published.all(),
	'date_field': 'pub_date',
	'allow_future': True,
}

feeds = {
	'latest': LatestPosts,
	'tag': TagFeed,
}

urlpatterns = patterns('django.views.generic.date_based',
	url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[0-9A-Za-z-]+)/$',
		'object_detail',
		dict(blog_dict, slug_field='slug')),
	url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$',
		'archive_month',
		blog_dict),
	url(r'^(?P<year>\d{4})/$',
		'archive_year',
		blog_dict,
		name='logos_year_archive'),
	url(r'^/?$',
		'archive_index',
		dict(blog_dict, allow_empty=True),
		name='logos-archive'),
)

urlpatterns += patterns('',
	url(r'^feeds/(?P<url>.*)/$',
		'django.contrib.syndication.views.feed',
		{'feed_dict': feeds}),
	url(r'^tag/(?P<tag>[^/]+)/$',
		tagged_object_list,
		dict(queryset_or_model=Post, paginate_by=10, allow_empty=True,
			template_object_name='post'),
		name='widget_tag_detail'),
)
