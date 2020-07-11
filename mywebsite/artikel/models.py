from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class ModelArtikel(models.Model):

    image      = models.ImageField(upload_to='upload/')  
    judul       = models.CharField(max_length=50)
    kategori    = models.CharField(max_length=50)
    body        = models.TextField()
    penulis     = models.CharField(max_length=50)
    publish     = models.DateTimeField(auto_now_add=True)
    update      = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.judul)
        super().save()

    def __str__(self):
        return "{}.{}".format(self.id,self.judul)

   # def get_absolute_url(self):
       # return reverse('manage-artikel') # setelah tambah artikel, kembali ke halaman index
    



