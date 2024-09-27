from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel
from applications.entradas.models import Entry
from .managers import FavoritesManagers

class Favorites(TimeStampedModel):
    """ Modelo para favoritos  """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='user_favorites',
        on_delete=models.CASCADE
    )
    
    entry = models.ForeignKey(
        Entry, 
        on_delete=models.CASCADE,
        related_name='entry_favorites'
    )


    objects = FavoritesManagers()


    class Meta:
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'
        unique_together = ('user', 'entry')

    def __str__(self) -> str:
        return self.entry.tilte