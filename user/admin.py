from django.contrib import admin
from .models import User, UserDetails, Skills, SkillAttribute, Portfolio, Projects,Qualification
from django.http import HttpRequest, HttpResponse
from typing import Optional
from django.contrib.auth.models import Group

admin.site.unregister(Group)


class CustomAdminSiteForUser(admin.AdminSite):
    site_header = 'User'
    

class TabularInlineMixin(admin.TabularInline):
    extra = 2


class SkillAttribueTabularInlne(TabularInlineMixin):
    model = SkillAttribute


class QualificationTabularInlne(TabularInlineMixin):
    model = Qualification

class PortfolioInline(TabularInlineMixin):
    model = Portfolio


class ProjectTabularInline(TabularInlineMixin):
    model = Projects



class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('created','updated','user','mobile','city','country','designation','description','contact_me_email','about_me_text','about_image','years_of_exp','companies_worked','completed_projects','cv_in_pdf','contact_me_new_project_image','facebook_link','linkedin_link','github_link','youtube_link','skype_link','tweeter_link','instagram_link')
    list_display_links = list_display
    inlines = [ProjectTabularInline,PortfolioInline,QualificationTabularInlne]
    fieldsets = (
        (
            "About Me",{
                'fields': ['user','mobile', 'designation', 'description', 'about_me_text', 'about_image','cv_in_pdf']
            }
        ),
        (
            "Address",{
                'fields': ['city','country','contact_me_new_project_image']
            }
        ),
        (
            "Experiene",{
                'fields': ['years_of_exp','companies_worked','completed_projects']
            }
        ),
        (
            "Social Links",{
                'fields': ['facebook_link', 'linkedin_link', 'github_link', 'youtube_link', 'skype_link', 'tweeter_link', 'instagram_link']
            }
        )
    )
    
    # def add_view(self, request: HttpRequest, form_url: str = ..., extra_context: None = ...) -> HttpResponse:
    #     # breakpoint()
    #     self.get_form(request)(user=request.user)
    #     return super().add_view(request, form_url=form_url, extra_context=extra_context)


class SkillsAdmin(admin.ModelAdmin):
    inlines = [SkillAttribueTabularInlne]
    list_display = (
        'created',
        'updated',
        'user_details',
        'skill_title',
        'skill_experience',
    )
    fieldsets = (
        (
            "User Skills",{
                'fields': ['user_details','skill_title','skill_experience']
            }
        ),
        
    )
    list_display_links = list_display

admin_custom_site = CustomAdminSiteForUser(name='Custom user')

admin_custom_site.register(Skills,SkillsAdmin)
admin_custom_site.register(UserDetails,UserDetailsAdmin)