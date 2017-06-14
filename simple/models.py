# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class tutorial(models.Model):
	name=models.TextField(max_length=255)
