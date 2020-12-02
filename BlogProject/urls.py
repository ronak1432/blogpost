
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Blog Admin"
admin.site.site_title = "Blog Admin Panel"
admin.site.index_title = "Welcome to Blog Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
]
