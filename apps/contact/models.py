from django.db import models

class Contact(models.Model):
    datetime = models.DateTimeField('Date of publication', auto_now_add=True)
    author_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    message = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.author_name

