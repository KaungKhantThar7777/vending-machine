from django.urls import path
from .views import csv_to_json
from graphene_django.views import GraphQLView

urlpatterns = [
    path('csv-to-json/', csv_to_json, name='csv-to-json'),
    path("graphql/", GraphQLView.as_view(graphiql=True)), 
]