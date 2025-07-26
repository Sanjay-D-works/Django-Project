
from django.contrib import admin
from django.urls import path, include

handler404 = 'myapp.views.custom_page_not_found'

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    
    
]
