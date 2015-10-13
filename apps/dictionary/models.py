from django.db import models
import uuid
import os

# Create your models here.

def get_path_instrumentation(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images/instrumentation', filename)

class Instrumentation(models.Model):
	"""Permite dar de alta un conceptp con definición e imagen"""
	name = models.CharField('Nombre', max_length = 200, unique = True)
	definition = models.TextField('Definición')
	image = models.FileField(upload_to = get_path_instrumentation)

	class Meta:
		verbose_name = 'Instrumento'
		verbose_name_plural = 'Instrumentos'

	def __str__(self):
		return self.name

	def imagen(self):
		return '<img src="/media/%s"/>' % self.image
	imagen.allow_tags = True