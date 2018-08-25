from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^myapp/', include('myapp.urls')),
    url(r'^payment/', include('payment.urls', namespace='payment')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
