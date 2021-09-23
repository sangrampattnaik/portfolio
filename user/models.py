import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import datetime
import os
from uuid import uuid4


def path_and_rename(instance, filename):
    upload_to = 'media_files'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = f'{instance.pk}.{ext}'
    else:
        # set filename as random string
        filename = f'{uuid4().hex}.{ext}'
    # return the whole path to the file
    return os.path.join(upload_to, filename)

class TimeStampMixin(models.Model):
    id = models.CharField(max_length=60,editable=False,primary_key=True,default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class User(AbstractUser):
    first_name = None
    last_name = None

    email = models.EmailField(_("Email"),unique=True)
    full_name = models.CharField(_("Full Name"),max_length=100,help_text="Short Name e.g Chiku")
    short_name = models.CharField(_("Short Name"),max_length=100,help_text="Short Name e.g Chiku")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','full_name','short_name']

    class Meta:
        verbose_name_plural = 'User'


class UserDetails(TimeStampMixin):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_details')
    mobile = models.CharField(_("Mobile Number"),max_length=10, unique=True)
    city = models.CharField(_("City"),max_length=100)
    country = models.CharField(_("Country"),max_length=100)
    designation = models.CharField(_("Designation"),max_length=100)
    description = models.TextField(_("Description"))
    contact_me_email = models.EmailField(_("Contact me email"),null=True,blank=True,help_text="It will on display on Contact me email")
    about_me_text = models.TextField(_("About me"))
    about_image = models.ImageField(_("About Image"),upload_to=path_and_rename)
    years_of_exp = models.PositiveIntegerField(_("Experience in years"))
    companies_worked = models.PositiveIntegerField(_("Number of companies worked"))
    completed_projects = models.PositiveIntegerField(_("Number of Completed projecrts"))
    cv_in_pdf = models.FileField(_("Resume/CV"),help_text=".pdf allowed only",upload_to=path_and_rename)
    contact_me_new_project_image = models.ImageField(_("Contact me image"),upload_to=path_and_rename)
    facebook_link = models.URLField(_("Facebook link"),null=True,blank=True)
    linkedin_link = models.URLField(_("Linkedin link"),null=True,blank=True)
    github_link = models.URLField(_("Github link"),null=True,blank=True)
    youtube_link = models.URLField(_("Youtube Link"),null=True,blank=True)
    skype_link = models.URLField(_("Skype Link"),null=True,blank=True)
    tweeter_link = models.URLField(_("Tweeter Link"),null=True,blank=True)
    instagram_link = models.URLField(_("Instagra Link"),null=True,blank=True)
    
    class Meta:
        verbose_name_plural = 'Dashboard'


class Skills(TimeStampMixin):
    user_details = models.ForeignKey(UserDetails,on_delete=models.CASCADE,related_name='skills')
    skill_title = models.CharField(_("Skill"),max_length=100)
    skill_experience = models.PositiveIntegerField(_("Skill Experience"))

    class Meta:
        verbose_name_plural = 'Skill'


class SkillAttribute(TimeStampMixin):
    skill = models.ForeignKey(Skills,on_delete=models.CASCADE,related_name="skill_attributes")
    name = models.CharField(_("Attribute Name"),max_length=100)
    percentage = models.PositiveIntegerField(_("Skill percentage"))


class Portfolio(TimeStampMixin):
    user_details = models.ForeignKey(UserDetails,on_delete=models.CASCADE, related_name="portfolio")
    portfolio_title = models.CharField(_("Portfolio title"),max_length=64, help_text="portfolio title")
    portfolio_description = models.TextField(_("Portfolio description"))
    link = models.URLField(_("Portfolio link"))
    portfolio_image = models.ImageField(upload_to=path_and_rename)


class Projects(TimeStampMixin):
    PROJECT_TYPE = (
        ('company', 'COMPANY'),
        ('personal', 'PERSONAL')
    )
    user_details = models.ForeignKey(UserDetails, on_delete=models.CASCADE, related_name="projects")
    project_type = models.CharField(_("Project type"), max_length=64, choices=PROJECT_TYPE, help_text="project type")
    project_name = models.CharField(_("Project name"), max_length=64, help_text="project name")
    company_name = models.CharField(_("Company name"), max_length=64, help_text="company name")
    start_date = models.DateField(help_text="start date", blank=True, null=True)
    end_date = models.DateField(help_text="end date", blank=True, null=True)
    project_link = models.URLField(_("project link"), blank=True, null=True)
    github_repository_link = models.URLField(_("Github repository link"), blank=True, null=True)
