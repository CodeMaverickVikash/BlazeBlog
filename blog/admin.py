from django.contrib import admin
# from django.db import models
from .models import Blog_categories, Cantact, BlogPost
# from pagedown.widgets import AdminPagedownWidget

@admin.register(Blog_categories)
class CategoryTable(admin.ModelAdmin):
    # formfield_overrides = {
    #     models.TextField: {'widget': AdminPagedownWidget},
    # }
    list_display = ['category', 'desc', 'slug']

@admin.register(BlogPost)
class BlgTable(admin.ModelAdmin):
    list_display = ['blg_title', 'blg_desc', 'slug', 'cat_slug']  
    class Media:
        js = ('js/tinyInject.js',)
    # formfield_overrides = {
    #     models.TextField: {'widget': AdminPagedownWidget},
    # }

@admin.register(Cantact)
class ContactTable(admin.ModelAdmin):
    list_display = ['full_name', 'email_address', 'password']    

# @admin.register(Answer)
# class AnswerTable(admin.ModelAdmin):
#     # formfield_overrides = {
#     #     models.TextField: {'widget': AdminPagedownWidget},
#     # }
#     list_display = ['answer', 'que_slug']  

# admin.site.register(Categories, Category)
# admin.site.register(Questions, AdminQue)
# admin.site.register(Cantact, ContactTable)
# admin.site.register(Answer, AnswerTable)