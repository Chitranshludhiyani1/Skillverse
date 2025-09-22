from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path("explore/", views.explore, name="explore"),
    path("post/<int:pk>/", views.read_post, name="read_post"),
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("create/", views.create_post, name="create_post"),
    path('delete/<int:t_id>/',views.delete,name='delete')
    
]

