import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User

class CreateUser(graphene.Mutation):

    user = graphene.Field(UserType)

    class Arguments:
        firstname = graphene.String(required=True)
        lastname = graphene.String(required=True)
        email = graphene.String(required=True)
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, firstname,lastname,email,username,password):
        user = User(first_name = firstname, last_name = lastname, email = email, username = username)
        user.set_password(password)
        user.save()

        return CreateUser(user = user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


class Query:
    user = graphene.List(UserType)

    def resolve_user(self, info, **kwargs):
        return  User.objects.all()
