from django.urls import path
from . import views

urlpatterns = [
    path('pools/',views.index, name='index'),
    path('pools/question/<int:question_id>', views.exibir, name='exibir'),
    path('pools/question/<int:question_id>/results', views.results, name='results'),
    path('pools/question/<int:question_id>/vote/', views.vote, name='vote'),
    path('pools/question/closed', views.exibir_fechada, name='exibir_fechada'),
    path('pools/question/<int:question_id>/apagar', views.apagar, name='apagar'),
    path('pools/question/<int:question_id>/status', views.status, name='status'),
    path('pools/cadastrar', views.cadastrar, name='cadastrar'),
    path('pools/<int:question_id>/responder',views.responder, name='escolher'),
]
