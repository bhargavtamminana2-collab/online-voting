from django.db import models


class Vote(models.Model):

    voter_id = models.CharField(
        max_length=10,
        unique=True,
        null=True,
        blank=True
    )

    aadhaar_id = models.CharField(
        max_length=12,
        unique=True,
        null=True,
        blank=True
    )

    candidate = models.CharField(max_length=100)

    def __str__(self):

        if self.voter_id:

            return self.voter_id

        return self.aadhaar_id