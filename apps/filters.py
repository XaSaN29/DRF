from django_filters import rest_framework as filters
from .models import Menyu, Comment


class MenyuFilter(filters.FilterSet):
    class Meta:
        model = Menyu
        fields = ['name', 'price', 'category']
