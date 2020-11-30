from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Artist(models.Model):
	image = models.ImageField(default='default.jpg', upload_to='artist_pics')
	name = models.CharField(max_length=100)
	birth_date = models.DateField()

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		super(Artist, self).save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)


class Construction(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='construction_pics')
    name = models.CharField(max_length=100)
    history = models.TextField(default="")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    creation_date = models.DateField()
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Construction, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 180 or img.width > 272:
            output_size = (180, 272)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    event_date = models.DateField()
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('museum-event-detail', kwargs={'pk': self.pk})