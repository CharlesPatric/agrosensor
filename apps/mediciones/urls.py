from django.urls import path

from .views import MedicionListAPIView


urlpatterns = [
    path(
        "",
        MedicionListAPIView.as_view(),
        name="mediciones-lista"
    ),
]