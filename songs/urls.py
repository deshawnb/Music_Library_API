from django.urls import path
from . import veiws

urlpatterns = {
    path('', veiws.songs_list),
    path('<int:pk>/', veiws.songs_detail)
}