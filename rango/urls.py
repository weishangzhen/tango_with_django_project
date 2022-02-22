from django.urls import path
#from django.conf.urls import url
#from django.urls import include
from rango import views 
app_name='rango'
urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/',views.add_category,name='add_category' ),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('restricted/', views.restricted, name='restricted'),
    path('search/',views.search, name="search"),
    path('account/<username>/',views.ProfileView.as_view(),name="profile"),
    path('register_profile/',views.register_profile,name="register_profile"),
    path('profiles/', views.ListProfilesView.as_view(), name='list_profiles'),
    path('goto/', views.goto_url, name='goto'),
    
]