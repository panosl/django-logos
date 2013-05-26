from django.conf.urls.defaults import *
from django.views.generic import dates
from django.contrib.sitemaps import GenericSitemap
from logos.models import Post
from logos.conf import settings
if settings.USE_TAGS:
    from taggit.views import tagged_object_list
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

urlpatterns = patterns('',
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[0-9A-Za-z-]+)/$',
        dates.DateDetailView.as_view(model=Post, date_field='pub_date'),
        name='logos_post_detail'),
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$',
        dates.MonthArchiveView.as_view(model=Post, date_field='pub_date'),
        name='logos_month_archive'),
    url(r'^(?P<year>\d{4})/$',
        dates.YearArchiveView.as_view(model=Post, date_field='pub_date'),
        name='logos_year_archive'),
    url(r'^/?$',
        dates.ArchiveIndexView.as_view(model=Post, date_field='pub_date'),
        name='logos_archive'),
)

urlpatterns += patterns('',
    url(r'^feeds/(?P<url>.*)/$',
        'django.contrib.syndication.views.Feed',
        {'feed_dict': feeds},
        name='logos_feeds'),
)

if settings.USE_TAGS:
    urlpatterns += patterns('',
        url(r'^tag/(?P<slug>[^/]+)/$',
            tagged_object_list,
            #dict(queryset_or_model=Post, paginate_by=settings.TAGS_PAGINATE_BY, allow_empty=True,
            dict(queryset=Post.objects.all(), paginate_by=settings.TAGS_PAGINATE_BY, allow_empty=True,
                template_object_name='post'),
            name='logos_tag_detail'),
    )
