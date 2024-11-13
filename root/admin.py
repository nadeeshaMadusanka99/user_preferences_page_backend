from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.contrib.admin import AdminSite


class CustomAdminSite(AdminSite):
    site_header = 'Admin Dashboard'
    site_title = 'Admin Dashboard'
    index_title = 'Welcome to the Admin'


class APIAdminView(admin.ModelAdmin):
    change_list_template = 'admin/custom_admin_docs.html'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('api-docs/', self.admin_site.admin_view(self.api_docs_view))
        ]
        return custom_urls + urls

    def api_docs_view(self, request):
        return render(request, 'admin/custom_admin_docs.html')


custom_admin_site = CustomAdminSite(name='custom_admin')
admin.site.register(APIAdminView)
