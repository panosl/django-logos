from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.dates import DateDetailView
from taggit.models import Tag

from logos.conf import settings
from logos.models import Post


def index(request):
    latest_post_list = Post.objects.all().order_by('-pub_date')[:5]

    return render(request, 'blog.html', {'latest_post_list': latest_post_list})


class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class TagIndexView(TagMixin, ListView):
    model = Post
    paginate_by = settings.TAGS_PAGINATE_BY
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug'))


class PostDetailView(DateDetailView):
    model = Post
    date_field = 'pub_date'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all()
        else:
            return Post.objects.filter(is_published=True)
