from django.db import models
from django.utils import timezone

class General_info(models.Model):
    address = models.TextField()
    phone_no = models.TextField()
    email = models.EmailField()
    reg_no = models.TextField()
    logo = models.ImageField()

    class Meta:
        verbose_name = 'General Information'

class Slider(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()

    class Meta:
        verbose_name = 'Slider Image'

class About(models.Model):
    who_we_are = models.TextField()
    mission = models.TextField()
    client = models.TextField()
    industry = models.TextField()
    community = models.TextField()
    employee = models.TextField()
    partner = models.TextField()
    vission = models.TextField()

    class Meta:
        verbose_name = 'About Us'

class Team(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField()

    class Meta:
        verbose_name = 'Our Team'


class Project(models.Model):
    caption = models.CharField(max_length=100)
    image = models.ImageField()

    class Meta:
        verbose_name = 'Projects Gallery'

class Services(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()

    class Meta:
        verbose_name = 'Our Services'

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News & Updates'

class Staff(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField()