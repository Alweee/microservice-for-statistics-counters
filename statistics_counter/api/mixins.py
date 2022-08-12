from rest_framework import viewsets, mixins


class CreateRetrieveDestroyViewSet(mixins.ListModelMixin,
                                   mixins.CreateModelMixin,
                                   mixins.RetrieveModelMixin,
                                   mixins.DestroyModelMixin,
                                   viewsets.GenericViewSet):
    pass
