from rest_framework import authentication, permissions, viewsets

from .models import Sprint
from .serializers import SprintSerializer


class DefaultsMixin(object):
    """Configuraciones default para autenticacion, permisos, filtros y paginacion de la view"""

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )

    permissions_classes = (
        permissions.IsAuthenticated,
    )

    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class SprintViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """Endpoint de la API para listar y crear sprints."""

    queryset = Sprint.objects.order_by('end')
    serializer_class = SprintSerializer
