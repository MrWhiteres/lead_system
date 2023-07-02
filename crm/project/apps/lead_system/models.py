from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=255, verbose_name='Lid name')
    email = models.CharField(max_length=255, verbose_name='Lid email', unique=True, db_index=True)
    phone = models.CharField(max_length=255, verbose_name='Lid phone', unique=True, db_index=True)
    ip_address = models.GenericIPAddressField(verbose_name='Lid ip address')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Lid create at datetime')

    class Meta:
        verbose_name = 'Lid'
        verbose_name_plural = 'Lids'

    def __str__(self) -> str:
        return f'{self.name}'


class LeadSettings(models.Model):
    lead = models.OneToOneField(Lead, on_delete=models.CASCADE, verbose_name='Lid')
    email = models.BinaryField(verbose_name='Lid email')
    phone = models.BinaryField(verbose_name='Lid phone')

    class Meta:
        verbose_name = 'Lid settings'
        verbose_name_plural = 'Lid settings'

    def __str__(self) -> str:
        return f'{self.lead.name} - settings'
