from django.db import models


# Create your models here.
class Fcuser(models.Model):
    username = models.CharField(max_length=64, verbose_name='사용자명')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.username

    # fcuser 의 테이블 이름을 직접 설정해주기
    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name = '패스트 캠퍼스 사용자'
        verbose_name_plural = '패스트 캠퍼스 사용자'
