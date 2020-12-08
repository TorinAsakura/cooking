# -*- coding: utf-8 -*-
from django import forms

from gallery.models import GalleryImage


class GalleryImageForm(forms.ModelForm):
	class Meta:
		model = GalleryImage
		fields = ('title', 'image', )