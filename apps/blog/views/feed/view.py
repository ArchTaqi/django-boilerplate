from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed
from apps.blog.models import Comment, Post


class LatestEntriesFeed(Feed):
    title = "%s blog entries" % (Site.objects.get_current())
    description = "The latest blog entries"
    link = "/siteposts/"

    def items(self):
        return Post.objects.order_by('-post_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.bodytext
