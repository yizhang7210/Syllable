"""syllable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from api.views import users as users_view
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

api_v1_patterns = [
    path('docs/', get_swagger_view(title='Syllable API')),
    path('users/signin', users_view.UserAuthView.as_view()),
]

urlpatterns = [
    path('v1/', include(api_v1_patterns)),
]
