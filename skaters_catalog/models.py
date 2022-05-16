from django.db import models
from django.urls import reverse
import uuid


# Create your models here.

class skater(models.Model):
    name_skater = models.CharField(max_length=100, blank=False)
    patronymic_skater = models.CharField(max_length=100, blank=False)
    surname_skater = models.CharField(max_length=100, blank=False)
    sex_skater = models.CharField(max_length=100, blank=False)
    date_of_birth_skater = models.CharField(max_length=100, blank=False)
    biography_skater = models.TextField(max_length=10000, null=True)
    characteristic_skater = models.TextField(max_length=10000, null=True)
    achievements = models.TextField(max_length=10000, null=True)
    photo_skater = models.TextField(max_length=1000, null=True)


    class Meta:
        ordering = ['name_skater', 'surname_skater']

    def get_absolute_url_skater(self):
        return reverse('skaters-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}, {1}'.format(self.name_skater, self.surname_skater)


class trainer(models.Model):
    name_trainer = models.CharField(max_length=100, blank=False)
    patronymic_trainer = models.CharField(max_length=100, blank=False)
    surname_trainer = models.CharField(max_length=100, blank=False)

    sex = (
        ('ж', 'женский'),
        ('м', 'мужской'),
    )

    sex_trainer = models.CharField(
        max_length=1,
        choices=sex,
        blank=False,
        null=True
    )
    date_of_birth_trainer = models.TextField(max_length=100, blank=False)
    biography_trainer = models.TextField(max_length=10000, null=True)
    career_trainer = models.TextField(max_length=10000, null=True)
    school = models.TextField(max_length=1000, null=True)
    photo_trainer = models.TextField(max_length=1000, null=True)

    class Meta:
        ordering = ['name_trainer', 'surname_trainer']

    def get_absolute_url_trainer(self):
        return reverse('trainers-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}, {1}'.format(self.name_trainer, self.surname_trainer)


class element(models.Model):
    name_element = models.CharField(max_length=200, blank=False)
    description_element = models.TextField(max_length=10000, null=True)
    price = models.TextField(max_length=1000, null=True)
    history = models.TextField(max_length=10000, null=True)
    video_element = models.TextField(max_length=1000, null=True)

    class Meta:
        ordering = ['name_element']

    def get_absolute_url_element(self):
        return reverse('elements-detail', args=[str(self.id)])

    def __str__(self):
        return self.name_element


class skater_element(models.Model):
    skater_id = models.ManyToManyField(skater)
    element_id = models.ManyToManyField(element)
    description = models.TextField(max_length=10000, null=True)
    video = models.TextField(max_length=1000, null=True)
    date = models.TextField(max_length=100, blank=False)
    competition = models.TextField(max_length=10000, blank=False)

    def get_absolute_url_skater_element(self):
        return reverse('skater_element-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.skater.name_skater} {self.skater.surname_skater} {self.element.name_element}'


class skater_trainer(models.Model):
    skater_id = models.ManyToManyField(skater)
    trainer_id = models.ManyToManyField(trainer)
    dates_together = models.TextField(max_length=1000, null=True)

    def get_absolute_url_skater_trainer(self):
        return reverse('skater_trainer-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.skater.name_skater} {self.skater.surname_skater} {self.trainer.name_trainer} {self.trainer.surname_skater}'
