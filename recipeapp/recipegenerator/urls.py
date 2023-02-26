from django.urls import include, path

from .views import HomePageView, SearchResultsView, ProfileView

urlpatterns = [
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("", HomePageView.as_view(), name="home"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', ProfileView.as_view(), name="profile")
]