# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import User, UserDetails, Skills, SkillAttribute, Portfolio, Projects


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'password',
        'last_login',
        'is_superuser',
        'username',
        'is_staff',
        'is_active',
        'date_joined',
        'email',
        'full_name',
        'short_name',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
    )
    raw_id_fields = ('groups', 'user_permissions')


@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'updated',
        'user',
        'mobile',
        'city',
        'country',
        'designation',
        'description',
        'contact_me_email',
        'about_me_text',
        'about_image',
        'years_of_exp',
        'companies_worked',
        'completed_projects',
        'cv_in_pdf',
        'contact_me_new_project_image',
        'facebook_link',
        'linkedin_link',
        'github_link',
        'youtube_link',
        'skype_link',
        'tweeter_link',
        'instagram_link',
    )
    list_filter = ('created', 'updated', 'user')


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'updated',
        'user',
        'skill_title',
        'skill_experience',
    )
    list_filter = ('created', 'updated', 'user')


@admin.register(SkillAttribute)
class SkillAttributeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'updated',
        'skill',
        'name',
        'percentage',
    )
    list_filter = ('created', 'updated', 'skill')
    search_fields = ('name',)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'updated',
        'user',
        'portfolio_image',
        'portfolio_title',
        'portfolio_description',
        'link',
    )
    list_filter = ('created', 'updated', 'user')


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'updated',
        'user',
        'project_name',
        'project_type',
        'company_name',
        'start_date',
        'end_date',
        'project_link',
        'github_repository_link',
    )
    list_filter = ('created', 'updated', 'user', 'start_date', 'end_date')
