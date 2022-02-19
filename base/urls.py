from django.urls import path
from .views import BlogCreate, BlogUpdate, home, BlogList, workouts, CustomLoginView, RegisterPage, BlogDetail, myworkout, addworkout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('blogs', BlogList.as_view(), name="blogs"),
    path('blogs/<int:pk>',BlogDetail.as_view(), name="blog"),
    path('blog-create/',BlogCreate.as_view(), name='blog-create'),
    path('blog-update/<int:pk>',BlogUpdate.as_view(), name='blog-update'),
    path('workouts', workouts, name="workouts"),
    path('login/',CustomLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='home'),name="logout"),
    path('register/',RegisterPage.as_view(),name="register"),
    path('myworkout/',myworkout, name="myworkout"),
    path('addworkout/<str:name>', addworkout, name="addworkout")
]