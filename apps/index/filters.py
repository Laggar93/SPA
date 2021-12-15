import django_filters
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Spa
from django_filters.rest_framework import FilterSet, CharFilter, ModelMultipleChoiceFilter, ModelChoiceFilter



class SpaFilter(django_filters.FilterSet):
    class Meta:
        model = Spa
        fields = ('name',)

    name = CharFilter(lookup_expr='icontains', distinct=True,)
