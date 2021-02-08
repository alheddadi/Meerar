import django_filters
from django_filters import DateFilter,CharFilter
from .models import *

class FilterServeds(django_filters.FilterSet):
    startDate =DateFilter(field_name ='Date',lookup_expr='gte')
    endDate =DateFilter(field_name ='Date',lookup_expr='lte')
    #endDate =CharFilter(field_name ='note',lookup_expr='icontain')
    class Meta:
        model = Reports
        fields= 'Product',
        exclude = ['date_created']
       
        #exclude=['date_created']

