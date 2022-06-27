from django.urls import path
from .views import ContentListView,ContentDetailView,ContentApiView,ContentListApiView

app_name = 'blog'

urlpatterns = [
    path('',ContentListView.as_view(),name="content_list"),
    path('api/list/',ContentListApiView.as_view(),name="content_api_list"),
    path('api/contents/',ContentApiView.as_view(),name="content_api"),
    path('api/contents/<int:id>/',ContentApiView.as_view(),name="content_api"),
    path("<slug:slug>/",ContentDetailView.as_view(),name="content_detail"),
]