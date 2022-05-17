from django.db import models
import sqlite3
from datetime import date, datetime

from django.db.models.fields import CharField, SlugField

connection = sqlite3.connect("db.sqlite3")

crsr = connection.cursor()

class Saint(models.Model):
    """              """
    text = models.CharField(max_length=200)
    summary = models.TextField(default="",blank=True)
    status = models.CharField(max_length=2, default="",blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    birth = models.DateField('birth Y-m-d')
    death = models.DateField('death Y-m-d')
    m_feast = models.CharField(max_length=50)
    d_feast = models.CharField(max_length=2)
    image = models.ImageField()
    cal_Image = models.ImageField()
    thumbnail = models.ImageField()
    credit = models.CharField(max_length=50,blank=True)
    alt = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.text

class Entry(models.Model):

    saint = models.ForeignKey(Saint, on_delete=models.CASCADE)
    text = models.TextField(default="There is nothing listed for this saint.")
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + "..."



class Prayer(models.Model):
    image = models.ImageField()
    prayer = models.ImageField()
    caption = models.CharField(max_length=50,blank=True)
    atl = models.CharField(max_length=50,blank=True)

class Calendar(models.Model):
    month = models.CharField(default=datetime.now(),max_length=50)