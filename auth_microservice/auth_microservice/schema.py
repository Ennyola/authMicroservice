import graphene
import graphql_jwt
from auth_app.schema import Query as userQuery
from auth_app.schema import Mutation as userMutation

class Query(userQuery, graphene.ObjectType):
    pass

class Mutation(userMutation, graphene.ObjectType):
    pass
    
    
    # token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    # verify_token = graphql_jwt.Verify.Field()
    # refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation = Mutation)