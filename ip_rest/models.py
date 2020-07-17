from django.db import models


class IpAddrStatus(models.TextChoices):
    AVAILABLE = 'available'
    ACQUIRED = 'acquired'


class IpAddr(models.Model):
    cidr = models.CharField(unique=True, max_length=20)
    status = models.CharField(
        max_length=100,
        choices=IpAddrStatus.choices,
        default=IpAddrStatus.AVAILABLE
    )

    def __str__(self):
        return f"{self.cidr} - {self.status}"
