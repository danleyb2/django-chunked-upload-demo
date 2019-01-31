from django.conf import settings
from django.urls import path, include


from django.contrib import admin
admin.autodiscover()

from demo.views import (
    ChunkedUploadDemo, MyChunkedUploadView, MyChunkedUploadCompleteView
)

urlpatterns = [
    path('', ChunkedUploadDemo.as_view(), name='chunked_upload'),
    path('api/chunked_upload/', MyChunkedUploadView.as_view(), name='api_chunked_upload'),
    path('api/chunked_upload_complete/', MyChunkedUploadCompleteView.as_view(), name='api_chunked_upload_complete'),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
