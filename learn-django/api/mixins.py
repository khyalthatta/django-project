from rest_framework.mixins import ListModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet


class ListUpdateMixin(ListModelMixin, UpdateModelMixin, GenericViewSet):
    pass
