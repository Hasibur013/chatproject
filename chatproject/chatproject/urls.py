from django.urls import path, include

# urls.py (project level) additions
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ...
    path('chat/', include('chat.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
