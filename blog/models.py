from datetime import datetime
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=250, help_text='Maximum 250 characters')
    slug = models.SlugField(max_length=250)
    description = models.TextField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/categories/%s/" % self.slug

class Meta:
    ordering = ['title']
    verbose_name_plural = "Categories"

class Post(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(blank=True)
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now)
    slug = models.SlugField(max_length=250)

    def __unicode__(self):
        return self.title

    from django.contrib.auth.models import User
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(default=True)

    STATUS_CHOICES = (
        (1, 'Live'),
        (2, 'Draft'),
        (3, 'Featured')
    )

    status = models.IntegerField(choices=STATUS_CHOICES, default=2)