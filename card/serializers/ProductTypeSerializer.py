from card.models import ProductType
from common.serializers.BaseSerializer import BaseSerializer


class ProductTypeSerializer(BaseSerializer):
    class Meta:
        model = ProductType
        fields = ('id', 'sup_type', 'sub_type', 'image')
