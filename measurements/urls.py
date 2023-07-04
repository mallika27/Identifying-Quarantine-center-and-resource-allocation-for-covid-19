from django.urls import path
from .views import calculate_distance_view
from .views import SearchResultsView,HomePageView,AboutView

app_name = 'measurements'

urlpatterns = [
    path('', calculate_distance_view, name='calaculate-view'),
    path('about/',AboutView.as_view(),name='about'),
    path('searcher/', SearchResultsView.as_view(), name='search'),
    path('index/', HomePageView.as_view(), name='index')
    #path('check')

]
