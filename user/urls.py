from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name = 'index'),
    path('secret/', views.secret, name = 'secret_view')
 ]

urlpatterns += [
    path('accounts/email/', RedirectView.as_view(url='/')),
    # Other URL patterns here
]