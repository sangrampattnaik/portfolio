from django.contrib import admin
from .models import User, UserDetails, Skills, SkillAttribute, Portfolio, Projects
from django.http import HttpRequest
from typing import Optional
from django.contrib.auth.models import Group

admin.site.unregister(Group)


class TabularInlineMixin(admin.TabularInline):
    extra = 2


class ModelAdminMixin(admin.ModelAdmin):
    # def has_change_permission(self, request: HttpRequest, obj: Optional[_ModelT] = ...) -> bool:
    #     return super().has_change_permission(request, obj=obj)

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
    
    def has_add_permission(self, request: HttpRequest) -> bool:
        return False


class SkillAttribueTabularInlne(TabularInlineMixin):
    model = SkillAttribute


class PortfolioInline(TabularInlineMixin):
    model = Portfolio


class ProjectTabularInline(TabularInlineMixin):
    model = Projects


@admin.register(UserDetails)
class UserDetailsAdmin(ModelAdminMixin):
    list_display = ('created','updated','user','mobile','city','country','designation','description','contact_me_email','about_me_text','about_image','years_of_exp','companies_worked','completed_projects','cv_in_pdf','contact_me_new_project_image','facebook_link','linkedin_link','github_link','youtube_link','skype_link','tweeter_link','instagram_link')
    list_display_links = list_display
    inlines = [ProjectTabularInline,PortfolioInline]
    fieldsets = (
        (
            "About Me",{
                'fields': ['mobile', 'designation', 'description', 'about_me_text', 'about_image','cv_in_pdf']
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


@admin.register(Skills)
class SkillsAdmin(ModelAdminMixin):
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
                'fields': ['skill_title','skill_experience']
            }
        ),
        
    )
    list_display_links = list_display