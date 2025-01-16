from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Diary(models.Model):
    title = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.TextField(verbose_name='Текст', **NULLABLE)
    cd_date = models.DateField(verbose_name='Дата записи')
    image = models.ImageField(upload_to='diary/images/', verbose_name='Картинка', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f"{self.title} {self.description}"
