from django.urls import path
from recipes import views as recipe_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', recipe_views.recipe_list, name='home'),
    path('<int:pk>/', recipe_views.recipe_detail, name='recipe_detail'),
    path('new/', recipe_views.recipe_create,name='recipe_create'),
    path('<int:pk>/edit/', recipe_views.recipe_edit, name='recipe_edit'),
    path('<int:pk>/delete/', recipe_views.recipe_delete, name='recipe_delete'),
    path('<int:pk>/comment/', recipe_views.add_comment, name='add_comment'),
    path('signup/', recipe_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='recipe_list'), name='logout'),
    path('search/', recipe_views.search, name='search'),
    
]
#path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
#path('logout/', auth_views.LogoutView.as_view(next_page='recipe_list'), name='logout'),