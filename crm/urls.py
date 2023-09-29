from django.contrib import admin
from django.urls import path
from management_app.views import some_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pdf/<int:order_id>/', some_view, name='pdf_view'),
]
