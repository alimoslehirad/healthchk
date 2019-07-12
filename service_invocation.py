from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _
from model_utils import Choices

from apps.supervised_request import constants as supervised_request_constants
from apps.users.models import User
from utils.models import BaseModel


class ServiceInvocation(BaseModel):
    STATUS_CHOICES = Choices(*supervised_request_constants.STATUS_TYPES)

    service = models.CharField(max_length=30, db_index=True)
    triggered_by_id = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    triggered_for_type_id = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    triggered_for_id = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, db_index=True)
    retry_count = models.IntegerField(_('retry count'), default=0, db_index=True)
    pending_count = models.IntegerField(_('pending count'), default=0, db_index=True)
    recovery_for = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='recoveries',
                                     verbose_name=_('recovery for'), blank=True, null=True)
    data = JSONField(verbose_name=_('data'), null=True, blank=True)
    duration = models.FloatField(_('duration'), blank=True, null=True, db_index=True)
    is_bulk = models.BooleanField(_('is bulk'), default=False)
    on_delivered_in_recovery = models.CharField(verbose_name=_('delivered in recovery'), max_length=500,
                                                null=True, blank=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = _('service invocation')
        verbose_name_plural = _('service invocations')

    def __str__(self):
        return '%s-invocation' % self.service

    @cached_property
    def triggered_for(self):
        content_type = ContentType.objects.filter(id=self.triggered_for_type_id).first()
        if content_type:
            model = apps.get_model(content_type.app_label, content_type.model)
            return model.objects.filter(id=self.triggered_for_id).first()
        return None

    @cached_property
    def triggered_by(self):
        return User.objects.filter(id=self.triggered_by_id).first()
