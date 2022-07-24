
from accounts import urls
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='hm'),
    path('accounts/', include('accounts.urls')),
    path('about/', views.about, name='abt'),
    path('payments/', views.payment, name='pay'),
    path('<slug:c_slug>/', views.home, name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodDetails, name='details'),
    path('search', views.searching, name='search'),
]
