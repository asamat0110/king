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
