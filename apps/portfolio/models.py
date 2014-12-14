from django.db import models

class Art(models.Model):
    title = models.CharField(max_length = 500)
    image = models.ImageField(upload_to = 'images/', height_field = None, width_field = None)
    price = models.FloatField(default = 0)
    about = models.CharField(max_length = 2000)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/portfolio/%i/" % self.id

    class meta:
        verbose_name_plural = "Portfolio"



