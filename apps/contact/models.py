from django.db import models

class Contact(models.Model):
    recd = models.DateTimeField('Date_of_receipt')
    author_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    message = models.TextField(max_length = 1000)
    def __unicode__(self):
        return self.recd