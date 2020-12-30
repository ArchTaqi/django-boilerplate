# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, absolute_import
from django.db import models

# Create your models here.
# Third Party Stuff

from django.contrib.auth import get_user_model
User = get_user_model()


class TimeAuditModel(models.Model):
    """To track when the record was created and last modified
    """
    created_at = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Last Modified", auto_now=True,)

    class Meta:
        abstract = True


class UserAuditModel(models.Model):
    """ To track who created and last modified the record
    """
    created_by = models.ForeignKey(User, related_name='created_%(class)s_set',
                                   null=True, blank=True, verbose_name="Created By")
    updated_by = models.ForeignKey(User, related_name='updated_%(class)s_set',
                                    null=True, blank=True, verbose_name="Modified By")

    class Meta:
        abstract = True

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = (request.user, None)
        else:
            obj.created_by = (request.user, None)
        obj.save()


class AuditModel(TimeAuditModel, UserAuditModel):

    class Meta:
        abstract = True




class AbstractEmail(models.Model):
    """
    This is a record of all emails sent to a customer.
    Normally, we only record order-related emails.
    """
    user = models.ForeignKey(User, related_name='emails', verbose_name="User")
    subject = models.TextField(verbose_name='Subject', max_length=255)
    body_text = models.TextField(verbose_name="Body Text")
    body_html = models.TextField(verbose_name="Body HTML", blank=True)
    date_sent = models.DateTimeField(verbose_name="Date Sent", auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return _(u"Email to %(user)s with subject '%(subject)s'") % {
            'user': self.user.get_username(), 'subject': self.subject}


@python_2_unicode_compatible
class AbstractNotification(models.Model):
    recipient = models.ForeignKey(User,
                                  related_name='notifications', db_index=True)

    # Not all notifications will have a sender.
    sender = models.ForeignKey(User, null=True)

    # HTML is allowed in this field as it can contain links
    subject = models.CharField(max_length=255)
    body = models.TextField()

    # Some projects may want to categorise their notifications.  You may want
    # to use this field to show a different icons next to the notification.
    category = models.CharField(max_length=255, blank=True)

    INBOX, ARCHIVE = 'Inbox', 'Archive'
    choices = (
        (INBOX, _('Inbox')),
        (ARCHIVE, _('Archive')))
    location = models.CharField(max_length=32, choices=choices,
                                default=INBOX)

    date_sent = models.DateTimeField(auto_now_add=True)
    date_read = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True
        app_label = 'customer'
        ordering = ('-date_sent',)
        verbose_name = _('Notification')
        verbose_name_plural = _('Notifications')

    def __str__(self):
        return self.subject

    def archive(self):
        self.location = self.ARCHIVE
        self.save()
    archive.alters_data = True

    @property
    def is_read(self):
        return self.date_read is not None