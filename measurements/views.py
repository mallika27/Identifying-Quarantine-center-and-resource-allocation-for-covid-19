from django.shortcuts import render, get_object_or_404
from .models import Measurement, Quarantine,city
from django.db.models import Q
from .forms import MeasurementModelForm
from geopy.geocoders import Photon
from geopy.distance import geodesic
from .utils import get_geo, get_center_coordinates, get_zoom
from django.views.generic import TemplateView, ListView
import operator
from functools import reduce
#from django.db import connection
import folium
import math
# Create your views here.

def calculate_distance_view(request):
    # initial values
    distance = None
    destination = None
    
    obj = get_object_or_404(Measurement, id=1)
    form = MeasurementModelForm(request.POST or None)
    geolocator = Photon(user_agent='measurements')

    ip = '117.203.227.120'
    country, city, lat, lon = get_geo(ip)
    location = geolocator.geocode(city)

    # location coordinates
    l_lat = lat
    l_lon = lon
    pointA = (l_lat, l_lon)
    all_members = Quarantine.objects.all
    #new= Quarantine.objects.location
   # tally=[]
    #for j in range(100):
     #   tally.append(j)
    #for i in tally:
     #   lon = Quarantine.objects.filter(id == i).Longitude
      #  lat = Quarantine.objects.filter(id == i).Latitude
        # loc= Quarantine.objects.
       # pointa = (lon, lat)
        #distance = round(geodesic(pointA, pointa).km, 2)


    # initial folium map
    m = folium.Map(width=800, height=500, location=get_center_coordinates(l_lat, l_lon), zoom_start=8)
    # location marker
    folium.Marker([l_lat, l_lon], tooltip='click here for more', popup=city['city'],
                      icon=folium.Icon(color='purple')).add_to(m)




    #earth_radius=6371
    #cities = Location.objects.filter().annotate(
     #   distance=earth_radius * ACos(Cos(Radians(l_lat)) * Cos(Radians("latitude")) * Cos(
      #      Radians("longitude") - Radians(l_lon)) + Sin(Radians(l_lat)) * Sin(
       #     Radians('latitude')))).filter(distance__lt=in_radius).order_by("distance")
    #return cities


    if form.is_valid():
        instance = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)

        # destination coordinates
        d_lat = destination.latitude
        d_lon = destination.longitude
        pointB = (d_lat, d_lon)
        # distance calculation
        distance = round(geodesic(pointA, pointB).km, 2)
        m = folium.Map(width=800, height=500, location=get_center_coordinates(l_lat, l_lon, d_lat, d_lon),
                           zoom_start=get_zoom(distance))
        # location marker
        folium.Marker([l_lat, l_lon], tooltip='click here for more', popup=city['city'],
                          icon=folium.Icon(color='purple')).add_to(m)
        # destination marker
        folium.Marker([d_lat, d_lon], tooltip='click here for more', popup=destination,
                          icon=folium.Icon(color='red', icon='cloud')).add_to(m)

        # draw the line between location and destination
        line = folium.PolyLine(locations=[pointA, pointB], weight=5, color='blue')
        m.add_child(line)

        instance.location = location
        instance.distance = distance

        #R = 6371000  # radius of Earth in meters
        #phi_1 = math.radians(l_lat)
        #phi_2 = math.radians(d_lat)
        #delta_phi = math.radians(d_lat - l_lat)
        #delta_lambda = math.radians(d_lon - l_lon)
        #a = math.sin(delta_phi / 2.0) ** 2 + \
        #    math.cos(phi_1) * math.cos(phi_2) * \
        #    math.sin(delta_lambda / 2.0) ** 2
        #c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        #instance.s = (R * c) / 1000.0  # output distance in kilometers
        #instance.save()









    
    m = m._repr_html_()

    context = {
        'distance' : distance,
        'destination': destination,
        'form': form,
        'map': m,
        'all': all_members,

    }

    return render(request, 'main.html', context)


class SearchResultsView(ListView):
    model = city

    template_name = 'check.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        #test= reduce((operator.and_, (city(Place__icontains=query))))
        if query:
            object_list = city.objects.filter(Q(city__icontains=query))
            return object_list
        else:
            print ("Location not found")
    def calculate_distance_view(request):
        # initial values
        distance = None
        destination = None
        obj = get_object_or_404(Measurement, id=1)
        form = MeasurementModelForm(request.POST or None)
        geolocator = Photon(user_agent='measurements')
        ip = '117.203.227.120'
        country, city, lat, lon = get_geo(ip)
        location = geolocator.geocode(city)
        # location coordinates
        l_lat = lat
        l_lon = lon
        pointA = (l_lat, l_lon)
        all_members = Quarantine.objects.all
        m = folium.Map(width=800, height=500, location=get_center_coordinates(l_lat, l_lon), zoom_start=8)
        # location marker
        folium.Marker([l_lat, l_lon], tooltip='click here for more', popup=city['city'],
                      icon=folium.Icon(color='purple')).add_to(m)
        if form.is_valid():
            instance = form.save(commit=False)
            destination_ = form.cleaned_data.get('destination')
            destination = geolocator.geocode(destination_)
            # destination coordinates
            d_lat = destination.latitude
            d_lon = destination.longitude
            pointB = (d_lat, d_lon)
            # distance calculation
            distance = round(geodesic(pointA, pointB).km, 2)
            m = folium.Map(width=800, height=500, location=get_center_coordinates(l_lat, l_lon, d_lat, d_lon),
                           zoom_start=get_zoom(distance))
            # location marker
            folium.Marker([l_lat, l_lon], tooltip='click here for more', popup=city['city'],
                          icon=folium.Icon(color='purple')).add_to(m)
            # destination marker
            folium.Marker([d_lat, d_lon], tooltip='click here for more', popup=destination,
                          icon=folium.Icon(color='red', icon='cloud')).add_to(m)
            # draw the line between location and destination
            line = folium.PolyLine(locations=[pointA, pointB], weight=5, color='blue')
            m.add_child(line)
            instance.location = location
            instance.distance = distance
        m = m._repr_html_()
        context = {
        'distance' : distance,
        'destination': destination,
        'form': form,
        'map': m,
        'all': all_members,
        }
        return render(request, 'check.html', context)




class HomePageView(TemplateView):
    template_name = 'index.html'
class AboutView(TemplateView):
    template_name='about.html'
class Harvesine:
    def __init__(self, coord1, coord2):
        lon1, lat1 = coord1
        lon2, lat2 = coord2

        R = 6371000  # radius of Earth in meters
        phi_1 = math.radians(lat1)
        phi_2 = math.radians(lat2)

        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)

        a = math.sin(delta_phi / 2.0) ** 2 + \
            math.cos(phi_1) * math.cos(phi_2) * \
            math.sin(delta_lambda / 2.0) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        self.meters = R * c  # output distance in meters
        self.km = self.meters / 1000.0  # output distance in kilometers
        self.miles = self.meters * 0.000621371  # output distance in miles
        self.feet = self.miles * 5280  # output distance in feet






