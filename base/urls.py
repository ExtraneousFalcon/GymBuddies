from django.urls import path
from .views import BlogCreate, PlanList, home, BlogList, plandetail, workout_search, CustomLoginView, RegisterPage, BlogDetail, planlist, PlanCreate, sample
from .views import addworkout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('blogs', BlogList.as_view(), name="blogs"),
    path('blogs/<int:pk>',BlogDetail.as_view(), name="blog"),
    path('blog-create/',BlogCreate.as_view(), name='blog-create'),
    #path('blog-update/<int:pk>',BlogUpdate.as_view(), name='blog-update'),
    path('login/',CustomLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='home'),name="logout"),
    path('register/',RegisterPage.as_view(),name="register"),
    path('plans',planlist, name="plans"),
    path('plan/<int:id>',plandetail, name="plan"),
    path('plan-create/',PlanCreate.as_view(),name="plan-create"),
    path('sample',sample, name="sample"),
    path('workout_search/<int:id>',workout_search, name="workout_search"),
    path('addworkout/<str:name>/<int:id>', addworkout, name="addworkout")
]