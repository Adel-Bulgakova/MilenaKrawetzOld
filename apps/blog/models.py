from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 500)
    author = models.CharField(max_length = 30)
    date = models.DateField('Date of publication')
    published = models.CharField(max_length = 5)
    content = models.TextField(max_length = 100000)
    preview = models.TextField(max_length = 100000)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id


class Post_image (models.Model):
    post = models.ForeignKey('Post')
    image_group = models.CharField(max_length = 5)
    image = models.ImageField(upload_to = 'blog/', height_field = None, width_field = None)

    def __unicode__(self):
        return self.image.name