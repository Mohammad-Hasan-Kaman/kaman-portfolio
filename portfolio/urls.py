from django.urls import path

from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('cv/', views.cv_page, name='cv'),
    path('cv/download/', views.cv_download, name='cv_download'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'),
    path('contact/', views.contact_submit, name='contact_submit'),
]
