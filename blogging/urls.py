from django.urls import path
from blogging.views import stub_view, BloggingDetailView, BloggingListView

urlpatterns = [
    path('', BloggingListView.as_view(), name="blog_index"),
    path('posts/<int:pk>/', BloggingDetailView.as_view(), name="blog_detail"),
]
