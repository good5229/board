from django.db import models
from django.urls import reverse


class Category(models.Model):
    class Meta:
        verbose_name = u'분류'
        ordering = ['name']

    name = models.CharField(verbose_name=u'이름', max_length=50)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    class Meta:
        verbose_name = u'글'
        ordering = ['created']

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=u'분류', null=True, blank=True)
    title = models.CharField(verbose_name=u'제목', max_length=256)
    content = models.TextField(u'내용', blank=True, default='')
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'생성일')
    photo = models.ImageField(u'이미지', blank=True, null=True, default='', upload_to='media/')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.id})
