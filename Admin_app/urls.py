from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
# -------------------------------- adminlogin & adminlogout -------------------------------- #
        path('',views.Adminlogin,name='Adminlogin'),
        path('dashboard/',views.admindashboard,name='admindashboard'),
        path('add_product/',views.add_product,name='add_product'),
        path('update_product/<int:id>/',views.UpdateProduct,name='update_product')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)