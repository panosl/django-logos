from django.conf.urls.defaults import *
from logos.models import Post

blog_dict = {
	'queryset': Post.objects.all(),
	'date_field': 'pub_date',
	'allow_future': True,
}

urlpatterns = patterns('django.views.generic.date_based',
	(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[0-9A-Za-z-]+)/$', 'object_detail', dict(blog_dict, slug_field='slug')),
	(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'archive_month', blog_dict),
	(r'^(?P<year>\d{4})/$', 'archive_year', blog_dict),
	(r'^/?$', 'archive_index', dict(blog_dict, allow_empty=True)),
)

