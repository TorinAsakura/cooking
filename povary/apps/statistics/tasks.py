# -*- coding: utf-8 -*-
import logging

from celery.task import task
from django.contrib.contenttypes.models import ContentType

from statistics.models import TrackingType, Tracking


logger = logging.getLogger("povary.%s" % __name__)


@task
def track_event(data):
	model = data['model']
	object_id = data['object_id']
	message = data.get("message")
	tracking_type_title = data['tracking_type']
	try:
		instance = model.objects.get(id=object_id)
	except model.DoesNotExist:
		logger.debug('Instance for model "%s" with ID "%s" not found!' % (model, object_id))
		return False
	tracking_type, created = TrackingType.objects.get_or_create(title=tracking_type_title)
	tracking = Tracking.objects.create(
		tracking_type=tracking_type,
		content_object=instance,
		message=message
	)
	logger.debug('Tracking for model "%s" with ID "%s" added!' % (model, object_id))
	return True
