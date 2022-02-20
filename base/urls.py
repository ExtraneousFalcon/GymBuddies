from django.urls import path
from .views import BlogCreate, PlanList, home, BlogList, plandetail, workouts, CustomLoginView, RegisterPage, BlogDetail, planlist, PlanCreate, sample
from .views import myworkout, addworkout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('blogs', BlogList.as_view(), name="blogs"),
    path('blogs/<int:pk>',BlogDetail.as_view(), name="blog"),
    path('blog-create/',BlogCreate.as_view(), name='blog-create'),
    #path('blog-update/<int:pk>',BlogUpdate.as_view(), name='blog-update'),
    path('workouts', workouts, name="workouts"),
    path('login/',CustomLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='home'),name="logout"),
    path('register/',RegisterPage.as_view(),name="register"),
    path('plans',planlist, name="plans"),
    path('plan/<int:id>',plandetail, name="plan"),
    path('plan-create/',PlanCreate.as_view(),name="plan-create"),
    path('sample',sample, name="sample"),
    path('workout_search',workouts, name="workout_search"),
    path('myworkout/',myworkout, name="myworkout"),
    path('addworkout/<str:name>', addworkout, name="addworkout")
]