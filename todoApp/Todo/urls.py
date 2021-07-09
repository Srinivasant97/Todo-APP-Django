from django.urls import path
from .views import List,Details,Create,Update,Delete,Login,Register
from django.contrib.auth.views import LogoutView


urlpatterns = [
	path('logout/', LogoutView.as_view(next_page="login"),name="logout"),
    path('login/', Login.as_view(),name="login"),
    path('register/', Register.as_view(),name="register"),
    path('', List.as_view(),name="list"),
    path('details/<int:pk>', Details.as_view(),name="detail"),
    path('todoCreate/', Create.as_view(),name="create"),
    path('todoUpdate/<int:pk>', Update.as_view(),name="update"),
    path('todoDelete/<int:pk>', Delete.as_view(),name="delete"),
]
 

