from django.urls import path

from . import views
from workforce.views import ResumeListView, ResumeDetailView, ResumeCreateView

urlpatterns = [
    path('', ResumeListView.as_view(), name='resume-list-page'),
    path('create/', ResumeCreateView.as_view(), name='resume-create-page'),
    path('<str:slug>/', ResumeDetailView.as_view(), name='resume-details-page'),
]