from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 500)
    author = models.CharField(max_length = 30)
    datetime = models.DateTimeField('Date of publication')
    published = models.CharField(max_length = 5)
    content = models.TextField(max_length = 100000)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id