from django.urls import path

from shortify import views

app_name = "shortify"
urlpatterns = [
    path("", views.ShortifyCreateView.as_view(), name="create"),
    path("<str:slug>", views.ShortifyDetailView.as_view(), name="detail"),
]
