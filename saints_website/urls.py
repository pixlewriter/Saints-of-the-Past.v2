from django.urls import path

from . import views

app_name = 'saints_website'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),

    # Show all topics.
    path('saints/', views.saints, name='saints'),

    # Detail page for a single topic.
    path('saints/<int:saint_id>/', views.saint, name='saint'),
]