# encoding: utf-8

from django.db import models

class Portfolio(models.Model):
    title = models.CharField(u'Заголовок', max_length = 500)
    description = models.CharField(u'Описание', max_length = 2000)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/portfolio/%i/" % self.id

    class Meta:
        verbose_name = u'Портфолио'
        verbose_name_plural = u'Портфолио'

class Portfolio_image (models.Model):
    portfolio = models.ForeignKey('Portfolio')
    image = models.ImageField(u'Изображение', upload_to = 'portfolio/', height_field = None, width_field = None)

    def __unicode__(self):
        return self.image.name

    class Meta:
        verbose_name = u'Портфолио'
        verbose_name_plural = u'Портфолио'


