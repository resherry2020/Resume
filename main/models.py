

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'
    
    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to="skills")
    is_key_skill = models.BooleanField(default=False)
    userprofile = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='userprofile_skills', null=True)
 
    
    def __str__(self):
        return self.name

class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    debugging_skills = models.ManyToManyField("Skill", blank=True, related_name='related_userprofiles')
    #skills = models.ManyToManyField("Skill", blank=True, related_name='related_userprofiles')
    cv = models.FileField(blank=True, null=True, upload_to="cv")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class ContactProfile(models.Model):
    
    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["timestamp"]
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name",max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f'{self.name}'



class Accomplishment(models.Model):

    class Meta:
        verbose_name_plural = 'Accomplishments'
        verbose_name = 'Accomplishment'
        ordering = ["name"]

    thumbnail = models.ImageField(blank=True, null=True, upload_to="accomplishments")
    name = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    quote = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Media(models.Model):

    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ["name"]
	
    image = models.ImageField(blank=True, null=True, upload_to="media")
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)
    def __str__(self):
        return self.name

class Project(models.Model):

    class Meta:
        verbose_name_plural = 'Project'
        verbose_name = 'Project'
        ordering = ["name"]
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="project")
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/project/{self.slug}"


class Experience(models.Model):

    class Meta:
        verbose_name_plural = 'Experience'
        verbose_name = 'Experience'
        ordering = ["start_date"]

    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="experience")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Experience, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/experience/{self.slug}"


class Education(models.Model):
    class Meta:
        verbose_name_plural = 'Educations'
        verbose_name = 'Education'

    start_date = models.DateField(blank=True, null=True, verbose_name='开始日期')
    end_date = models.DateField(blank=True, null=True, verbose_name='结束日期')
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='学校')
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name='专业')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

