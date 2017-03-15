from django.conf.urls import include, url
from sort import views


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^$', include('sort.urls')),
    url(r'^api/v1/sort/books/$', views.SortBooks.as_view(), name='sort-books'),
]
