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
from api.views import users as user_views
from api.views import grips as grip_views
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

api_v1_patterns = [
    path('docs', get_swagger_view(title='Syllable API')),
    path('users', user_views.UserDetailView.as_view()),
    path('users/signin/google', user_views.GoogleSignInView.as_view()),
    path('organizations', user_views.OrganizationListView.as_view()),
    path('organizations/<int:id>', user_views.OrganizationDetailView.as_view()),
    path('grips', grip_views.GripListView.as_view()),
    path('grips/search', grip_views.GripSearchView.as_view()),
    path('grips/<int:id>', grip_views.GripDetailView.as_view()),
]

urlpatterns = [
    path('v1/', include(api_v1_patterns)),
]
