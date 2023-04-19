from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
	path('', views.IndexView.as_view(), name="home"),
	path('contact/', views.ContactView.as_view(), name="contact"),
	path('project/', views.ProjectView.as_view(), name="projects"),
	path('project/<slug:slug>', views.ProjectDetailView.as_view(), name="project"),
	path('experience/', views.ExperienceView.as_view(), name="experiences"),
	path('experience/<slug:slug>', views.ExperienceDetailView.as_view(), name="experience"),
	]
