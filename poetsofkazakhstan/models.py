from django.db import models
from django.urls import reverse


class Categories(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'
        ordering = ['id']


class Poets(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    year_of_life = models.CharField(max_length=255, db_index=True)
    category_id = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True)
    info_id = models.ForeignKey('Informations', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('poets', kwargs={'poet_id': self.pk})

    class Meta:
        verbose_name = 'Poets'
        verbose_name_plural = 'Poets'


class Poems(models.Model):
    poet_id = models.ForeignKey('Poets', on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=255, db_index=True)
    main = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('poems', kwargs={'poem_id': self.pk})

    class Meta:
        verbose_name = 'Poems'
        verbose_name_plural = 'Poems'


class Informations(models.Model):
    info_id = models.ForeignKey('Poets', on_delete=models.PROTECT, null=True)
    info = models.TextField(blank=True)

    def __str__(self):
        return self.info

    class Meta:
        verbose_name = 'Informations'
        verbose_name_plural = 'Informations'
