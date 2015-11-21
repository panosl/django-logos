from django.views.generic import DetailView, ListView
from django.shortcuts import render_to_response

from taggit.models import Tag

from logos.models import Post
from logos.conf import settings


def index(request):
    latest_post_list = Post.objects.all().order_by('-pub_date')[:5]
    return render_to_response('blog.html', {'latest_post_list': latest_post_list})


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
