from django.urls import path
from . import views
urlpatterns = [
   	path('',views.signin),
   	path('postsign/',views.postsign),
   	path('logout/',views.logout,name="log"),
   	path('postadmin/',views.createpro),
]
