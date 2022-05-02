from django.contrib import admin

from . import models


admin.site.register(models.Actor)
admin.site.register(models.Movie)
admin.site.register(models.Director)
admin.site.register(models.DirectorGenre)
admin.site.register(models.MovieGenre)
admin.site.register(models.Role)
admin.site.register(models.MovieDirector)
