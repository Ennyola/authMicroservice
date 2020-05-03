import graphene
import graphql_jwt
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserType(DjangoObjectType):
     class Meta:
         model = User
         fields = ['id','email', 'username']
        
    

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()

    class Arguments:
        # firstname = graphene.String(required=True)
        # lastname = graphene.String(required=True)
        email = graphene.String(required=True)
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        

    def mutate(self, info,email,username,password):
        if User.objects.filter(email = email ).exists():
            raise Exception("email already exists")
        elif User.objects.filter(username = username ).exists():
            raise Exception("username Already exists")
        else:
            user = User(email = email, username = username)
            user.set_password(password)
            user.save()
        


        return CreateUser(user = user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    


class Query:
    user = graphene.Field(UserType)
    
    def resolve_user(self, info, **kwargs):
        user = info.context.user
    
        if not user.is_authenticated:
            raise Exception('No logged in User')
        return user

