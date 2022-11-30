from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('events/', views.events_index, name='index'),
  path('events/create/', views.EventCreate.as_view(), name='events_create'),
  path('events/<int:event_id>/', views.events_detail, name='detail'),
  path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='events_update'),
  path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='events_delete'),
  path('accounts/signup/', views.signup, name='signup'),
  path('events/<int:event_id>/add_comment/', views.add_comment, name='add_comment'),
  path('events/<int:event_id>/add_photo/', views.add_photo, name='add_photo'),
  path('comments/<int:pk>/update/', views.CommentUpdate.as_view(), name='comment_update'),
  path('comments/<int:pk>/delete/', views.CommentDelete.as_view(), name='comment_delete'),
  path('events/my_index/', views.events_my_index, name='my_index'),
  path('events/events_seattle/', views.events_seattle, name='events_seattle'),
  path('events/events_losangeles/', views.events_losangeles, name='events_losangeles'),
  path('events/events_sanfrancisco/', views.events_sanfrancisco, name='events_sanfrancisco'),
  path('rate/<int:event_id>/', views.rate, name='add_rating'),
  path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))),
] 
