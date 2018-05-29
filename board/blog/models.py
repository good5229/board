from django.conf import settings
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

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.id})



def user_path(instance, filename): #파라미터 instance는 Photo 모델을 의미 filename은 업로드 된 파일의 파일 이름
    from random import choice
    import string # string.ascii_letters : ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr) # 8자리 임의의 문자를 만들어 파일명으로 지정
    extension = filename.split('.')[-1] # 배열로 만들어 마지막 요소를 추출하여 파일확장자로 지정
    # file will be uploaded to MEDIA_ROOT/user_<id>/<random>
    return '%s/%s.%s' % (instance, pid, extension) # 예 : wayhome/abcdefgs.png

class Photo(models.Model):
    image = models.ImageField(upload_to = user_path) # 어디로 업로드 할지 지정
    thumname_image = models.ImageField(blank = True) # 필수입력 해제
    comment = models.CharField(max_length = 255)
    pub_date = models.DateTimeField(auto_now_add = True) # 레코드 생성시 현재 시간으로 자동 생성