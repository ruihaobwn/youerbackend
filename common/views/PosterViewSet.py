from rest_framework.viewsets import ReadOnlyModelViewSet
from common.models import Poster
from common.serializers import PosterSerializer
from common import filters


class PosterViewSet(ReadOnlyModelViewSet):
    filterset_class = filters.PosterFilter

    queryset = Poster.objects.all()
    serializer_class = PosterSerializer
