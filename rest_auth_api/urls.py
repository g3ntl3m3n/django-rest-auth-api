
from django.contrib import admin
from django.urls import path, include

from connect import FacebookConnect, TwitterConnect, GithubConnect
from facebookview import FacebookLogin
from githubview import GithubLogin
from twitterview import TwitterLogin

urlpatterns = [
    path('rest', include('rest_auth.urls')),
    path('rest/regist', include('rest_auth.registration.urls')),
    path('rest/facebook', FacebookLogin.as_view(), name='fb_login'),
    path('rest/twitter', TwitterLogin.as_view(), name='twitter_login'),
    path('rest/github', GithubLogin.as_view(), name='github_login'),
    path('rest/facebook/connect', FacebookConnect.as_view(), name='fb_login'),
    path('rest/twitter/connect', TwitterConnect.as_view(), name='twitter_login'),
    path('rest/github/connect', GithubConnect.as_view(), name='github_login'),
    path('admin/', admin.site.urls),
]
