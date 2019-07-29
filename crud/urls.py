from django.contrib import admin
from django.urls import path
import crudapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crudapp.views.home, name = 'home'),
    path('blog/<int:blog_id>', crudapp.views.detail, name = 'detail'),
    path('new/', crudapp.views.new, name = 'new'),
    path('create', crudapp.views.create, name = 'create'),
    path('blog/<int:blog_id>/delete', crudapp.views.delete, name = 'delete'),
    path('blog/<int:blog_id>/edit', crudapp.views.edit, name = 'edit'),
    path('blog/<int:blog_id>/update', crudapp.views.update, name = 'update'),
]
