from django.db import models

class Contact(models.Model):
    first_name = models.CharField(
        max_length=255,
        blank=True,
        db_index=True,
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
        db_index=True,
    )
    email = models.EmailField(
        blank=True
    )
    subject_massage = models.CharField(
        max_length=255,
        blank=True,
        db_index=True
    )
    massage = models.TextField(
        blank=True
    )
    def __str__(self):
        return self.subject_massage


class Feedback(models.Model):
    title = models.CharField(
        max_length=255,
        blank=True,
        db_index=True,
    )
    file = models.FileField(
        upload_to='imeges/%Y/%m/%d',
        blank=True
    )
    context = models.TextField(
        blank=True
    )
    name = models.CharField(
        max_length=255,
        blank=True
    )
    created = models.DateTimeField(
        auto_now=True
    )
    update = models.DateTimeField(
        auto_now=True
    )
    is_published = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name

class Project(models.Model):
    Project_name = models.CharField(
        max_length=255,
        blank=True
    )
    kinds = models.CharField(
        max_length=255,
        blank=True,
        db_index=True,
    )
    file = models.FileField(
        upload_to='imeges/%Y/%m/%d',
        blank=True
    )
    context = models.TextField(
        blank=True
    )
    created = models.DateTimeField(
        auto_now=True
    )
    update = models.DateTimeField(
        auto_now=True
    )
    is_published = models.BooleanField(
        default=True
    )
    def __str__(self):
        return self.Project_name