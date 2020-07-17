from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Setting(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud emas'),
    )
    title = models.CharField(max_length=222)
    keywords = models.CharField(max_length=222)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=222)
    address = models.CharField(max_length=222, blank=True)
    phone = models.CharField(max_length=222, blank=True)
    fax = models.CharField(max_length=222, blank=True)
    email = models.CharField(max_length=222, blank=True)
    smtserver = models.CharField(max_length=222, blank=True)
    smtemail = models.CharField(max_length=222, blank=True)
    smtpassword = models.CharField(max_length=222, blank=True)
    smtport = models.CharField(max_length=222, blank=True)
    icon = models.ImageField(upload_to='images/', blank=True)
    facebook = models.CharField(max_length=222, blank=True)
    instagram = models.CharField(max_length=222, blank=True)
    twitter = models.CharField(max_length=222, blank=True)
    youtube = models.CharField(max_length=222, blank=True)
    telegram = models.CharField(max_length=222, blank=True)
    aboutus = RichTextUploadingField()
    contact = RichTextUploadingField()
    references = RichTextUploadingField()
    status = models.CharField(max_length=155, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title