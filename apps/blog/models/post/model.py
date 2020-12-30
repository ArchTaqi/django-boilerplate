# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse


class PostManager(models.Manager):
    def get_posts(self):
        posts = self.all()
        if posts:
            return posts[0]
        return None


class Post(models.Model):
    """Blog wide settings.
     title:title of the Blog.
     tag_line: Tagline/subtitle of the post.
               This two are genearlly displayed on each page's header.
     entries_per_page=Number of entries to display on each page.
     recents: Number of recent entries to display in the sidebar.
     recent_comments: Number of recent comments to display in the sidebar.
    """

    title = models.CharField(
        verbose_name='Title',
        max_length=200,
        unique=True,
        db_column='title'
    )
    slug = models.SlugField()
    tag_line = models.CharField(
        verbose_name='Tag Line',
        max_length=100,
        db_column='tag_line'
    )
    body_text = models.TextField(
        verbose_name='Body',
        max_length=1024,
        db_column='body_text'
    )
    post_date = models.DateTimeField(
        verbose_name='Post Date',
        auto_now_add=True,
        db_column='post_date'
    )
    modified = models.DateTimeField(
        verbose_name='Modified',
        null=True,
        db_column='modified'
    )
    # posted_by = models.ForeignKey(
    #     verbose_name='Posted By',
    #     null=True,
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.SET_NULL,
    #     db_column='posted_by'
    # )
    allow_comments = models.BooleanField(
        verbose_name='allow comments',
        default=True,
        db_column='allow_comments'
    )
    comment_count = models.IntegerField(
        verbose_name='comment count',
        blank=True,
        default=0,
        db_column='comment_count'
    )

    objects = PostManager()

    def __str__(self):
        return '{0}, {1}'.format(self.title, self.tag_line)

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'post'
        db_table = 'tbl_post'
        ordering = ['-post_date']

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug,
            'year': '%04d' % self.post_date.year,
            'month': '%02d' % self.post_date.month,
            'day': '%02d' % self.post_date.day,
        }

        return reverse('blog_detail', kwargs=kwargs)
