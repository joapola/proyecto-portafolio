from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'
    verbose_name = 'Portafolio'  # Configuarcion extendida para cambiar el nombre de la aplicacion en el sector admin
