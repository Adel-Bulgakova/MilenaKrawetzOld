from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length = 500)
    price = models.FloatField(default = 0)
    about = models.CharField(max_length = 2000)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/portfolio/%i/" % self.id

    class meta:
        verbose_name_plural = "Portfolio"

class Portfolio_image (models.Model):
    portfolio = models.ForeignKey('Portfolio')
    image = models.ImageField(upload_to = 'portfolio/', height_field = None, width_field = None)

    def __unicode__(self):
        return self.image.name


