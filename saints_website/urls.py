from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
app_name = 'saints_website'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),

    # Show all topics.
    path('saints/', views.saints, name='saints'),

    # Detail page for a single topic.
    path('saints/<int:saint_id>/', views.saint, name='saint'),

    #search results
    path('saints/search_results/', views.search_results, name='search_results'),

    # prayers
    path('prayers', views.prayers, name='prayers'),

    # calendar
    path('calendar', views.calendar, name='calendar')

]
