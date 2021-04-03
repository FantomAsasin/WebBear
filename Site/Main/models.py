from django.db import models

class Person(models.Model):
    name = models.CharField("Имя", max_length=100)
    role = models.CharField("Роль", max_length=100)
    img = models.ImageField("Изображение", upload_to="media/Avatar/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Персонаж"
        verbose_name_plural = "Персонажи"