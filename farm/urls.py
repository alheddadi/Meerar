from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.loginPage, name="login"),
    path('FarmersHome', views.index, name="home"),
    path('BuyersHome', views.index2, name="home2"),
    path('Register', views.singup, name="register"),
    path('CropPrices', views.newprices, name="prices"),
    path('AboutUs', views.About, name="about"),
    path('MopileApp', views.App, name="app"),
    path('Trucks', views.cars, name="cars"),
    path('Reports', views.reports, name="reports"),
    path('newReports', views.newReports, name="nreports"),
    path('Maps', views.Maps, name="maps"),
    path('NewProduct', views.addnew, name="new"),
    path('products/<str:pk>/', views.product, name="product"),
    path('logout', views.logout, name="logout"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)