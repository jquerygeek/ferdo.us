from django.shortcuts import get_object_or_404, render_to_response
from polls.models import Choice, Poll
from blog.models import Post


def home(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    featured_post_list = Post.objects.filter(status=3).order_by('-pub_date')[:1]
    live_post_list = Post.objects.filter(status=1).order_by('-pub_date')[:3]
    return render_to_response('main/home.html', {'latest_poll_list': latest_poll_list, 'featured_post_list': featured_post_list, 'live_post_list': live_post_list})
