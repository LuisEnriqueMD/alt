# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class ThermoGenius(models.Model):
	name = models.CharField(max_length=50, default='', unique=True)
	description = models.TextField(max_length=900,default='')
	especification = models.ManyToManyField('Especifications',default='')
	price = models.CharField(max_length=7,default='')
	image = models.ImageField(upload_to='thermo/',default='')
	def __unicode__(self):
		return self.name

class Especifications(models.Model):
	name = models.CharField(max_length=40,default='')
	class Meta:
		ordering = ('name',)
		verbose_name = 'Especificación'
		verbose_name_plural = 'Especificaciones'
	def __unicode__(self):
		return self.name
