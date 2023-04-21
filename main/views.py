from django.shortcuts import render
from django.contrib import messages
from .models import (
		UserProfile,
		Experience,
		Project,
		Accomplishment,
		Education,
        Skill
	)

from django.views import generic


from . forms import ContactForm


class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		userprofile = UserProfile.objects.first()
		accomplishments = Accomplishment.objects.filter(is_active=True)
		educations = Education.objects.filter(is_active=True)
		experiences = Experience.objects.filter(is_active=True)
		project = Project.objects.filter(is_active=True)
		if userprofile:
			key_skills = userprofile.userprofile_skills.filter(is_key_skill=True)
			debugging_skills = userprofile.debugging_skills.all()
			coding_skills = userprofile.userprofile_skills.filter(is_key_skill=False).exclude(id__in=debugging_skills)
		else:
			key_skills = []
			debugging_skills = []
			coding_skills = []

  
		context["me"] = userprofile
		context["accomplishments"] = accomplishments
		context["educations"] = educations
		context["experiences"] = experiences
		context["project"] = project
		context["key_skills"] = key_skills
		context["coding_skills"] = coding_skills
		context["debugging_skills"] = debugging_skills
		
		return context




class ContactView(generic.FormView):
	template_name = "main/contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)


class ProjectView(generic.ListView):
	model = Project
	template_name = "main/project.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class ProjectDetailView(generic.DetailView):
	model = Project
	template_name = "main/project-detail.html"

class ExperienceView(generic.ListView):
	model = Experience
	template_name = "main/experience.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class ExperienceDetailView(generic.DetailView):
	model = Experience
	template_name = "main/experience-detail.html"
 