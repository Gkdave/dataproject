# from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    # path("admin/",admin.site.urls),
    path('',views.home,name="Home page"),
    path('profile',views.profile,name="profile_page"),
    path('expression',views.expression,name='expression value')

]