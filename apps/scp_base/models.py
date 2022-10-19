from django.db import models
from django.db.models.query import QuerySet
from typing import Optional, Any
from datetime import datetime


class ScpModelQuerySet(QuerySet):

    def get_deleted(self) -> QuerySet['SCPSafe']:
        return self.filter(datetime_deleted_isnull=False)

    def get_not_deleted(self) -> QuerySet['SCPSafe']:
        return self.filter(
            datetime_deleted__isnull=True
        )

    def get_not_equal_updated(self) -> QuerySet:
        return self.filter(
            datetime_updated=['datetime_created']
        )

    def get_obj(self, p_key: str) -> Optional['SCPSafe']:
        try:
            return self.get(
                id=p_key
            )
        except SCPSafe.DoesNotExist:
            return None


class SCPSafe(models.Model):
    title_object = models.CharField(verbose_name='Название объекта', max_length=100)
    description = models.CharField(verbose_name='Описание', max_length=6000)
    image = models.ImageField(verbose_name='Изображение', upload_to='scp_safe')
    content = models.CharField(verbose_name="Условия содержания", max_length=5000)

    # objects = ScpModelQuerySet().as_manager()

    class Meta:
        ordering = (
            'title_object',
        )
        verbose_name = 'временная модель'
        verbose_name_plural = 'временные модели'

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.full_clean()
        super().save(*args, **kwargs)

    def delete(self) -> None:
        self.datetime_deleted = datetime.now()
        self.save(
            update_field=['datetime_deleted']
        )

    def __str__(self):
        return f'{self.title_object}'
#Целый ____________________

class SCPEuclid(models.Model):
    title_object = models.CharField(verbose_name='Название объекта фонда', max_length=255)
    description = models.CharField(verbose_name='Описание', max_length=6000)
    image = models.ImageField(verbose_name="Изображение", upload_to='scp_euclid/')
    content = models.CharField(verbose_name="Условия содержания", max_length=5000)

    def __str__(self) -> str:
        return f"{self.title_object}"

    class Meta:
        ordering = (
            'id',

        )


class SCPKeter(models.Model):
    title_object = models.CharField(verbose_name='Название объекта фонда', max_length=255)
    description = models.CharField(verbose_name='Описание', max_length=6000)
    image = models.ImageField(verbose_name="Изображение", upload_to='scp_keter')
    content = models.CharField(verbose_name="Условия содержания", max_length=5000)

    def __str__(self) -> str:
        return f"{self.title_object}"

    class Meta:
        ordering = (
            'id',

        )


class SCPThaumiel(models.Model):
    title_object = models.CharField(verbose_name='Название объекта фонда', max_length=255)
    description = models.CharField(verbose_name='Описание', max_length=6000)
    image = models.ImageField(verbose_name="Изображение", upload_to='scp_thaumiel/')
    content = models.CharField(verbose_name="Условия содержания", max_length=5000)

    def __str__(self) -> str:
        return f"{self.title_object}"

    class Meta:
        ordering = (
            'id',

        )


class SCPAllClasses(models.Model):
    scp_safe = models.ForeignKey(SCPSafe, verbose_name='Объект класса Безопасный', on_delete=models.PROTECT)
    scp_euclid = models.ForeignKey(SCPEuclid, verbose_name='Объект класса Евклид', on_delete=models.PROTECT)
    scp_keter = models.ForeignKey(SCPKeter, verbose_name='Объект класса Кетер', on_delete=models.PROTECT)
    scp_thaumiel = models.ForeignKey(SCPThaumiel, verbose_name='Объект класса Таумиель', on_delete=models.PROTECT)
