# from django.contrib import admin
# from django.urls import path
# from .api import ListApi, CardApi
# from django.views.generic import TemplateView
#
# urlpatterns = [
#     path('lists/', ListApi.as_view()),
#     path('cards/', CardApi.as_view()),
#     path('home', TemplateView.as_view(template_name="home.html")),
# ]

from .api import ListViewSet, CardViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'lists', ListViewSet)
router.register(r'cards', CardViewSet)

urlpatterns = router.urls
