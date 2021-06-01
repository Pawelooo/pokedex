import django_filters
from django.http import Http404
from django_filters.rest_framework import filters
from rest_framework import viewsets, status

from poke.models import Pokemon
from poke.serializers import PokemonSerializer
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        name = self.request.GET.get('name')
        kind = self.request.GET.get('kind')
        try:
            queryset = Pokemon.objects.all()
            if name is not None:
                queryset = queryset.filter(name=name)
            if kind is not None:
                queryset = queryset.filter(kind__name=kind)
            return queryset
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        try:
            data = Pokemon.objects.get(pk=pk)
            context ={
                "data": data,
                "message": 'Contents returned successfully',
                'success': True
            }
            return Response(context, status=status.HTTP_200_OK)
        except Exception as error:
            context = {'error': str(error), 'success': False, 'message': 'Failed to Get contents'}
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)






