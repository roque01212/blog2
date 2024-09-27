from django.db import models


class FavoritesManagers(models.Manager):

    def entradas_user(self, user):
        return self.filter(
            entry__public = True,
            user = user
        ).order_by('-created')
    

    def comprobar_si_existe(self, usuerio, entrada):
        return self.filter(
            user = usuerio, 
            entry = entrada
            ).exists()