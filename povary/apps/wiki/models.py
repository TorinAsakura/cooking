# -*- coding: utf-8 -*-
import os

from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse

from uuslug import uuslug as slugify


class CategoryBase(models.Model):
	title = models.CharField("Заголовок", max_length=255)
	slug = models.SlugField("URL", unique=True)
	description = models.TextField("Описание", blank=True, null=True)
	published = models.BooleanField()

	class Meta:
		abstract = True

	def __unicode__(self):
		return self.title


class WikiCategory(CategoryBase):
	pass

	class Meta:
		verbose_name = "Категоиря"
		verbose_name_plural = "Категории"


class WikiSubCategory(CategoryBase):
	category = models.ForeignKey(WikiCategory, verbose_name="Категория")

	class Meta:
		verbose_name = "Подкатегория"
		verbose_name_plural = "Подкатегории"


class WikiSubSubCategory(CategoryBase):
	subcategory = models.ForeignKey(WikiSubCategory, verbose_name="Подкатегория")

	class Meta:
		verbose_name = "Подподкатегория"
		verbose_name_plural = "Подподкатегории"

def wikipage_uploadto(instance, filename):
	from utils import timestampbased_filename
	path = os.path.join(
		"wiki",
		"user_%s" % (instance.author.id),
		timestampbased_filename(filename)
	)
	return path

class WikiPage(models.Model):
	title = models.CharField("Заголовок", max_length=255)
	slug = models.SlugField("URL", unique=True)
	image = models.ImageField("Изображение", upload_to=wikipage_uploadto, blank=True, null=True)
	body = models.TextField("Текст")
	warnings = models.TextField("Предупреждения", blank=True, null=True)
	prooflinks = models.TextField("Ссылки на первоисточники", blank=True, null=True)
	published = models.BooleanField("Опубликовано", default=False)
	verified = models.BooleanField("Утверждено", default=False)
	category = models.ForeignKey(WikiCategory, verbose_name="Категория")
	subcategory = models.ForeignKey(WikiSubCategory, verbose_name="Подкатегория")
	subsubcategory = models.ForeignKey(WikiSubSubCategory, verbose_name="Подподкатегория")
	author = models.ForeignKey(User, verbose_name="Автор", related_name="authors_wikipages",
		blank=True, null=True)
	ip_addr = models.CharField("IP", max_length=255, blank=True, null=True)
	redactors = models.ManyToManyField(User, verbose_name="Список редакторов",
		related_name="redactors_wikipages")
	created = models.DateTimeField("Время создания", auto_now_add=True)
	updated = models.DateTimeField("Время обновления", auto_now=True)

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title, instance=self)
		super(WikiPage, self).save(*args, **kwargs)

	def get_versions(self):
		return WikiPageVersion.objects.filter(page=self).order_by("revision")

	def get_contenttype_id(self):
		return ContentType.objects.get_for_model(WikiPage).id

	def get_absolute_url(self):
		return reverse("wikipage_details", args=(self.slug, ))

	class Meta:
		verbose_name = "Страница энциклопедии"
		verbose_name_plural = "Энциклопедия"


WAITING = '0'
ACCEPTED = '1'
REJECTED = '2'

VERSION_STATUS = (
	(WAITING, 'Ожидает'),
	(ACCEPTED, 'Принято'),
	(REJECTED, 'Отклонено'),
)


class WikiPageVersion(models.Model):
	revision = models.PositiveIntegerField("№ версии", editable=False)
	page = models.ForeignKey(WikiPage, verbose_name="Страница", related_name="revisions")
	old_title = models.CharField("Старый заголовок", max_length=255, blank=True, null=True)
	new_title = models.CharField("Новый заголовок", max_length=255)
	old_slug = models.SlugField("URL", blank=True, null=True)
	new_slug = models.SlugField("URL")
	old_image = models.ImageField("Старое изображение",  upload_to=wikipage_uploadto, blank=True, null=True)
	new_image = models.ImageField("Новое изображение",  upload_to=wikipage_uploadto, blank=True, null=True)
	old_body = models.TextField("Старый текст", blank=True, null=True)
	new_body = models.TextField("Новый текст")
	old_warnings = models.TextField("Старые предупреждения", blank=True, null=True)
	new_warnings = models.TextField("Новые предупреждения", blank=True, null=True)
	old_prooflinks = models.TextField("Старые ссылки на первоисточники", blank=True, null=True)
	new_prooflinks = models.TextField("Новые ссылки на первоисточники", blank=True, null=True)
	reason = models.TextField("Описание изменений", blank=True, null=True)
	author = models.ForeignKey(User, verbose_name="Пользователь", blank=True, null=True)
	status = models.CharField("Статус", max_length=255, choices=VERSION_STATUS, default=WAITING)
	changed = models.DateTimeField("Время изменений", auto_now_add=True)
	ip_addr = models.CharField("IP", max_length=255, blank=True, null=True)


	def __unicode__(self):
		return self.page.title

	def save(self, *args, **kwargs):
		# Auto handling of revision num
		revision_list = WikiPageVersion.objects.filter(page=self.page).order_by('-revision')
		if not self.revision:
			if revision_list:
				self.revision = revision_list[0].revision + 1
			else:
				self.revision = 1
		super(WikiPageVersion, self).save(*args, **kwargs)

	def get_prev_revision(self):
		try:
			prev_version = WikiPageVersion.objects.get(
				page=self.page,
				revision=self.revision-1
			)
			return prev_version
		except WikiPageVersion.DoesNotExist:
			return None

	def get_next_revision(self):
		try:
			prev_version = WikiPageVersion.objects.get(
				page=self.page,
				revision=self.revision+1
			)
			return prev_version
		except WikiPageVersion.DoesNotExist:
			return None

	def get_discussions(self):
		discussion_list = WikiDiscussion.objects.filter(version=self).order_by("-changed")
		return discussion_list

	@staticmethod
	def init_version(wikipage):
		version = WikiPageVersion.objects.create(
			page = wikipage,
			old_title = "",
			old_slug = "",
			old_image = "",
			old_body = "",
			old_warnings = "",
			old_prooflinks = "",
			new_title = wikipage.title,
			new_slug = wikipage.slug,
			new_image = wikipage.image,
			new_body = wikipage.body,
			new_warnings = wikipage.warnings,
			new_prooflinks = wikipage.prooflinks,
			author = wikipage.author,
			ip_addr = wikipage.ip_addr
		)
		return version

	class Meta:
		verbose_name = "Версия страницы"
		verbose_name_plural = "Версии энциклопедии"


class WikiDiscussion(models.Model):
	version = models.ForeignKey(WikiPageVersion, verbose_name="Версия", related_name="discussions")
	text = models.TextField("Коментировать")
	author = models.ForeignKey(User, verbose_name="Автор", related_name="wiki_discussions",
		blank=True, null=True
	)
	pub_date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.text[:50]



@receiver(post_save, sender=WikiPageVersion)
def version_status_check(sender, instance, **kwargs):
	version_list = WikiPageVersion.objects.filter(page=instance.page).order_by('-revision')
	if instance.status == ACCEPTED:
		version_list.filter(~Q(status=REJECTED), revision__gt=instance.revision).update(status=WAITING)
		version_list.filter(~Q(status=REJECTED), revision__lt=instance.revision).update(status=ACCEPTED)
		wikipage = instance.page
		wikipage.title = instance.new_title
		wikipage.slug = instance.new_slug
		wikipage.image = instance.new_image
		wikipage.body = instance.new_body
		wikipage.warnings = instance.new_warnings
		wikipage.prooflinks = instance.new_prooflinks
		wikipage.save()
	elif instance.status == WAITING:
		version_list.filter(~Q(status=REJECTED), revision__gt=instance.revision).update(status=WAITING)
	elif instance.status == REJECTED:
		# Not send email if author is anonymous
		if not instance.author:
			return
		from core.tasks import send_mail
		subject = "Изменения отклонены"
		message = "Ваши изменения к статье %s были отклонены." % instance.old_title
		send_mail(subject, message, "admin@povary.ru", (instance.author.email, ))
