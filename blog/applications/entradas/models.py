from datetime import timedelta, datetime
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField
from .managers import EntryManager

class Category(TimeStampedModel):
    """ Categorias de una entrada """
    short_name = models.CharField(
        'Nombre corto',
        max_length=15,
        unique=True
    )
    name = models.CharField(
        'Nombre',
        max_length=30
    )


    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self) -> str:
        return self.name
    

class Tag(TimeStampedModel):
    """ etiquetas de un articulo"""
    name = models.CharField(
        'Nombre', 
        max_length=30)


    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Tags'

    def __str__(self) -> str:
        return self.name
    

class Entry(TimeStampedModel):
    """ Modeo para las entradas o articulos """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE
    )
    Tag = models.ManyToManyField(Tag)
    title = models.CharField(
        'Titulo',
        max_length=200
    )
    resume = models.TextField()
    content = RichTextUploadingField('contenido')
    public = models.BooleanField(default=False)
    image = models.ImageField(
         'Imagen', 
         upload_to='Entry', 
    )
    portada = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    #
    slug = models.SlugField(editable=False, max_length=300)

    objects = EntryManager()

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def __str__(self) -> str:
        return f"{self.title} {self.id}"
    
    def save(self, *args, **kwargs):
        # Calculamos el total de segundos de la hora actual
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds = int(total_time.total_seconds())
        slug_unique = f"{self.title}{seconds}"
        self.slug = slugify(slug_unique)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy(
            'entrada_app:Entrada', 
            kwargs={'slug': self.slug}
            )