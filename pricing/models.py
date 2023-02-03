from django.db import models


class DistanceBasePricing(models.Model): # DBP
    up_to_distance = models.FloatField(default=0, help_text="In kms")
    price = models.FloatField(default=0, help_text="In Rupees")
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.price}rs upto {self.up_to_distance}'

    class Meta:
        unique_together = ('up_to_distance', 'is_active',)
        ordering = ('-is_active', 'up_to_distance',)


class TimeMultiplierFactor(models.Model): #TMF
    up_to_time = models.FloatField(default=0, help_text="In Hours")  # in hours
    factor = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Upto {self.up_to_time} hour - {self.factor}x'

    class Meta:
        unique_together = ('up_to_time', 'is_active',),
        ordering = ('-is_active', 'up_to_time',)


class DistanceAdditionalPrice(models.Model): # DAP
    price = models.FloatField(default=0, help_text="In Rupees")
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.price}rs/Km'

    class Meta:
        ordering = ('-is_active',)


from django.dispatch import receiver
from django.db.models.signals import (
  pre_save,
  post_save,
  post_delete,
)


@receiver(pre_save, sender=DistanceAdditionalPrice)
def DistanceAdditionalPrice_pre_save_receiver(sender, instance, *args, **kwargs):
    if instance.is_active:
        if instance.id:
            DistanceAdditionalPrice.objects.exclude(id=instance.id).update(is_active=False)
        else:
            DistanceAdditionalPrice.objects.update(is_active=False)

