from django.urls import path
from polling.views import PollListView, PollDetailView

urlpatterns = [
    path('', PollListView.as_view(), name="poll_index"), # note the difference in using a list view, need to add .as_view() - why parens?
    path('polls/<int:pk>/', PollDetailView.as_view(), name="poll_detail"), 
        # pk is primary key, generic detail view needs to use pk and not the specific name we had before
]