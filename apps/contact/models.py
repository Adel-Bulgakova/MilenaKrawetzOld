# encoding: utf-8

from django.db import models

class Contact(models.Model):
    datetime = models.DateTimeField(u'Дата публикации сообщения', auto_now_add=True)
    author_name = models.CharField(u'Имя автора', max_length = 100)
    email = models.CharField('Email', max_length = 100)
    message = models.CharField(u'Текст сообщения', max_length = 100)

    def __unicode__(self):
        return self.author_name

    class Meta:
        verbose_name = u'Входящее сообщение'
        verbose_name_plural = u'Входящие сообщения'

