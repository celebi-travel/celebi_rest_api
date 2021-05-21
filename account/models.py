from PIL.Image import Image
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from common.base_model import BaseModel

"""
post , user vs 
"""


class Account(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')

    biography = models.TextField(blank=True, null=True)
    profile_photo = models.ImageField(null=True, blank=True, upload_to='profile_photos/%Y/%m/')
    birth_of_date = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    active = models.BooleanField(default=True)
    """
    sehir
    ülke
    cüzdan
    rotalar
    """

    class Meta:
        ordering = ('created_at',)
        verbose_name = _('Hesap')
        verbose_name_plural = _('Hesaplar')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.id = self.user.id
        # image resize
        super().save(*args, **kwargs)

        if self.profile_photo:  # eğer foto varsa
            img = Image.open(self.profile_photo.path)
            if img.height > 600 or img.width > 600:
                output_size = (600, 600)
                img.thumbnail(output_size)
                img.save(self.profile_photo.path)
