from django.urls import include, path

from .views import HomePageView, SearchResultsView, ProfileView, SignUpView, RestrictionsView

urlpatterns = [
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("", HomePageView.as_view(), name="home"),
    path("restrictions", RestrictionsView.as_view(), name="restrictions"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', ProfileView.as_view(), name="profile"),
    path("signup/", SignUpView.as_view(), name="signup")
]