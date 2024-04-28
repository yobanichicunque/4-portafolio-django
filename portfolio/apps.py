from django.apps import AppConfig

# Configuracion extendida para cambiar la configuracion en
# el sector administrativo


class PortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'
    verbose_name = 'Portafolio'
