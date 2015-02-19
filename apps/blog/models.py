# encoding: utf-8

from django.db import models

class Post(models.Model):
    title = models.CharField(u'Заголовок', max_length = 500)
    date = models.DateField(u'Дата публикации')
    published = models.BooleanField(u'Опубликовано')
    content = models.TextField(u'Контент', max_length = 100000)
    preview = models.TextField(u'Preview', max_length = 100000)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id

    class Meta:
        verbose_name = u'Пост'
        verbose_name_plural = u'Посты'


class Post_image (models.Model):
    post = models.ForeignKey('Post')
    image_group = models.CharField(u'Группа изображений', max_length = 5)
    image = models.ImageField(u'Изображение', upload_to = 'blog/', height_field = None, width_field = None)

    def __unicode__(self):
        return self.image.name

    class Meta:
        verbose_name = u'Изображение поста'
        verbose_name_plural = u'Изображения постов'