
from django.contrib import admin
from django.urls import path, include

handler404 = 'myapp.views.custom_page_not_found'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'))
    
]
