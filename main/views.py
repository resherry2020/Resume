from django.shortcuts import render
from django.contrib import messages
from .models import (
		UserProfile,
		Blog,
		Portfolio,
		Testimonial,
		Certificate,
        Skill
	)

from django.views import generic


from . forms import ContactForm


class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		userprofile = UserProfile.objects.first()
		testimonials = Testimonial.objects.filter(is_active=True)
		certificates = Certificate.objects.filter(is_active=True)
		blogs = Blog.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)
		#me = userprofile
		key_skills = userprofile.userprofile_skills.filter(is_key_skill=True)
		debugging_skills = userprofile.debugging_skills.all()
		coding_skills = userprofile.userprofile_skills.filter(is_key_skill=False).exclude(id__in=debugging_skills)

		me = UserProfile.objects.first()

  
		context["me"] = userprofile
		context["testimonials"] = testimonials
		context["certificates"] = certificates
		context["blogs"] = blogs
		context["portfolio"] = portfolio
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


class PortfolioView(generic.ListView):
	model = Portfolio
	template_name = "main/portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "main/portfolio-detail.html"

class BlogView(generic.ListView):
	model = Blog
	template_name = "main/blog.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-detail.html"