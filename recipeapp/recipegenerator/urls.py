from django.urls import include, path

from .views import HomePageView, SearchResultsView, ProfileView, SignUpView, restrictionsview, recipeview, profileview

urlpatterns = [
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("", HomePageView.as_view(), name="home"),
    path("restrictions", restrictionsview, name="restrictions"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', profileview, name="profile"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("recipe/", recipeview, name='recipe')
]