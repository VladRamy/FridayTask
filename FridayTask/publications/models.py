from django.db import models



class Publications(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Описание')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/publications/{self.id}'

    class Meta:
        verbose_name='Публикация'
        verbose_name_plural='Публикации'
