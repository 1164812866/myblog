from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.models import EmailAddress
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

 
class UserProfile(AbstractUser):
    GENDER_CHOICE = (
        ('male', '男'),
        ('female', '女')
    )
    nick_name = models.CharField(max_length=20, verbose_name='昵称', null=True, blank=True)
    mobile = models.CharField(max_length=11, verbose_name='手机', null=True, blank=True)
    address = models.CharField(max_length=200, verbose_name='地址', null=True, blank=True)
    avatar = ProcessedImageField(upload_to='avatar/%Y/%m/%d',
                                 default='avatar/default.png',
                                 verbose_name='头像',
                                 processors=[ResizeToFill(80, 80)]
                                 )
 
    def email_verified(self):
        if self.is_authenticated:
            result = EmailAddress.objects.filter(email=self.email)
            if len(result):
                return result[0].verified
        else:
            return False

 
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
        ordering = ['-id']
 
    def __str__(self):
        return self.username