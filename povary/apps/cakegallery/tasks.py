# -*- coding: utf-8 -*-
from celery.task import task


@task
def publish_cakeimage(image):
	from cakegallery.models import CakeImage
	try:
		image = CakeImage.objects.get(id=image.id)
		image.published=True
		image.save()
	except CakeImage.DoesNotExist:
		pass