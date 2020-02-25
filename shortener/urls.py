from django.urls import path

from shortener.views import ShortenerView, RedirectView

urlpatterns = [
    path('short/', ShortenerView.as_view()),
    path('<str:short_url>', RedirectView.as_view()),
]
