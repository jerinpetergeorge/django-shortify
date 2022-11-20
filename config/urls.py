from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from shortify import views

urlpatterns = [
    path("", include("pages.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("shortify/", include("shortify.urls")),
    path(
        "s/<str:slug>",
        views.ShortifyRedirectView.as_view(),
        name="shortify-redirect",
    ),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
