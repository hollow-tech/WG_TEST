from django.db import models


class Upload(models.Model):
    title = models.CharField(verbose_name='название', max_length=50)
    file = models.FileField(verbose_name='файл', upload_to='files/')

    def __str__(self):
        return self.title
