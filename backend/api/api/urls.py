"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
## We don't need Django admin panel for now
# from django.contrib import admin
# We need include for append Django REST framework URLs
from django.urls import re_path, path, include

# Our app REST API view
from rest.views import InspectionList

urlpatterns = [
    ## We don't need Django admin panel for now
    #path('admin/', admin.site.urls),
    path('api/solargrade/inpsections', InspectionList.as_view()),
    # Django REST browsable API authorization support
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
