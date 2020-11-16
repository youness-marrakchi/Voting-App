from django.urls import path
from . import views

app_name = "pages"
urlpatterns = [
    path("", views.index, name="index"),
]
# we use <> to pass-in parameters
