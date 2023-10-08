from django.urls import path
from .import views
from django .http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('kiraz', views.kiraz),
    path('erik', views.erik, name = 'erik.html'),
    path('ayva', views.ayva, name = 'Ayva.html'),
    path('ayva1', views.ayva1, name = 'Ayva1.html'),
    path('incir', views.incir, name = 'incir.html'),
    path('kavun', views.kavun, name = 'Kavun.html'),
    path('Home_page', views.home_page, name = 'Home_page.html'),
    path('Blog', views.blog, name = 'Blog.html'),
    path('Kalori_calculator', views.kalori_calculator, name = 'Kalori_calculator.html'),
    path('About_us', views.about_us, name = 'About_us.html'),
    path('Contact_us', views.contact_us, name = 'Contact_us.html'),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)