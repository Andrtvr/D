from django.conf.urls import url
from .views import question_list, popular, question_detail, question_ask, question_answer, answer_st, answer_list


urlpatterns = [
    url(r'^$', question_list, name='question_list'),
    url(r'^question/(?P<pk>\d+)/', question_detail, name='question_detail'),
    url(r'^popular/', popular, name='popular'),
    url(r'^ask/', question_ask, name='question_ask'),
    #url(r'^answer/', question_answer, name='question_answer'),
     url(r'^answer/', answer_st, name='answer11'),
     url(r'^answers/', answer_list, name='answers'),
    #url(r'^signup/', user_signup, name='signup'),
   # url(r'^login/', user_login, name='login'),
   # url(r'^logout/', user_logout, name='logout'),
    #url(r'^new/', test, name='new'),
]
