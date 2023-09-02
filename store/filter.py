import django_filters
from .models import Chategory

class ChategoryFilter(django_filters.FilterSet):
    relatedproducts_gte = django_filters.NumberFilter(field_name="relatedproducts", lookup_expr='gte')
    relatedproducts_lte = django_filters.NumberFilter(field_name="relatedproducts", lookup_expr='lte')

    class Meta:
        model = Chategory
        fields = ['relatedproducts_gte', 'relatedproducts_lte']