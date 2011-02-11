from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from blog.models import Post

def index(request):
    latest_post_list = Post.objects.all().order_by('-pub_date')[:5]
    return render_to_response('blog/index.html', {'latest_post_list': latest_post_list, 'active_menu': request.path})


def detail(request, post_id, post_slug):
    p = get_object_or_404(Post, pk=post_id, slug=post_slug)
    return render_to_response('blog/post_detail.html', {'post': p, 'active_menu': '/blog/'})