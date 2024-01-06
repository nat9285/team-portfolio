from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import ModelForm
from .models import Project, Category,Page

class ProjectAdminForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'categories': FilteredSelectMultiple("Categories", is_stacked=False),
        }

class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm

class PageForm(admin.ModelAdmin):
    class Meta:
        model = Page
        fields = '__all__'

admin.site.register(Project,ProjectAdmin)
admin.site.register(Category)
admin.site.register(Page,PageForm)