from django.urls import path
from .views import ContentListView,ContentDetailView

app_name = 'blog'

urlpatterns = [
    path('',ContentListView.as_view(),name="content_list"),
    path("<slug:slug>/",ContentDetailView.as_view(),name="content_detail")
]