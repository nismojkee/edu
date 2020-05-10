from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone


class news(models.Model):
	image = models.ImageField(upload_to = 'news/', help_text = 'news image', verbose_name = 'News image:')
	title = models.CharField(max_length = 200, help_text = 'news title', verbose_name = 'News title:')
	text = models.TextField(help_text = 'news text', verbose_name = 'News text:')
	
	FRESH = 'FR'
	POPULAR = 'PO'
	HOT = 'HO'
	YEAR_IN_SCHOOL_CHOICES = [
		(FRESH, 'Fresh news'),
		(POPULAR, 'Popular news'),
		(HOT, 'Hot news'),
	]
	category = models.CharField(
		max_length=2,
		choices=YEAR_IN_SCHOOL_CHOICES,
		default=FRESH,
	)
	
	created = models.DateTimeField(default = timezone.now)

	def publish(self):
		self.save()

	def __str__(self):
		return self.title


class course(models.Model):
	image = models.ImageField(upload_to = 'course/', help_text = 'course image', verbose_name = 'Course image:')
	title = models.CharField(max_length = 200, help_text = 'course title', verbose_name = 'Course name:')
	description = models.TextField(help_text = 'course description', verbose_name = 'Course description:')
	price = models.PositiveIntegerField(help_text = 'course price', verbose_name = 'Course price:')
	category = models.CharField(max_length = 200, help_text = 'course category', verbose_name = 'Course category:')

	def publish(self):
		self.save()

	def __str__(self):
		return self.title


class reviewer(models.Model):
	photo = models.ImageField(upload_to = 'review/', help_text = 'reviewer photo', verbose_name = 'Reviewer photo:')
	name = models.CharField(max_length = 200, help_text = 'reviewer name', verbose_name = 'Reviewer name:')
	email = models.EmailField(max_length = 254, help_text = 'reviewer email', verbose_name = 'Reviewer email:')
	review = models.TextField(help_text = 'reviewer message', verbose_name = 'Reviewer message:')
	stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], help_text = 'reviewer rating', verbose_name = 'Reviewer rating', null = True, blank = True)
	created = models.DateTimeField(default = timezone.now)

	def publish(self):
		self.save()

	def __str__(self):
		return self.name