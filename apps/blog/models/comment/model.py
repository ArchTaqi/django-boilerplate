from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from apps.blog.signals import save_comment
from apps.blog.models import Post


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        related_name='comments',
        verbose_name="post",
        on_delete=models.CASCADE
    )
    body_text = models.TextField(
        max_length=512,
        verbose_name="message",
        db_column='body_text'
    )
    post_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="post date",
        db_column='post_date'
    )
    ip_address = models.GenericIPAddressField(
        default='0.0.0.0',
        verbose_name="ip address",
        db_column='ip_address'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        verbose_name="user",
        related_name='comment_user',
        on_delete=models.SET_NULL,
        db_column='post_date',
    )
    user_name = models.CharField(
        max_length=50,
        default='anonymous',
        verbose_name="user name",
        db_column='user_name'
    )
    user_email = models.EmailField(
        blank=True,
        verbose_name="user email"
    )

    def __str__(self):
        return self.bodytext

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        ordering = ['post_date']


post_save.connect(save_comment, sender=Comment)