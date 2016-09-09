from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions, viewsets

from .models import Sprint, Task
from .serializers import SprintSerializer, TaskSerializer, UserSerializer

User = get_user_model()


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


class TaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """Endpoint de la API para listar y crear tareas"""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserViewSet(DefaultsMixin, viewsets.ReadOnlyModelViewSet):
    """Endpoint de la API para listar usuarios"""

    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer
