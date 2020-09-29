import graphene
from graphene_django import DjangoObjectType
from user.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return User.objects.all()


class CreateUser(graphene.Mutation):
    id = graphene.Int()
    username = graphene.String()
    email = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()

    class Arguments:
        username = graphene.String()
        email = graphene.String()

    def mutate(self, info, username, email):
        user = User(username=username, email=email)
        user.save()

        return CreateUser(
            id=user.id,
            email=user.email,
            username=user.username
        )


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


Query: graphene.ObjectType
Mutation: graphene.ObjectType

schema = graphene.Schema(query=Query, mutation=Mutation)
