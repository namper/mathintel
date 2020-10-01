GRAPHENE = {
    "SCHEMA": "user.schema.schema",
    'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ],
}

AUTH_USER_MODEL = 'user.User'

GRAPHQL_JWT = {
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LONG_RUNNING_REFRESH_TOKEN': True,

    "JWT_ALLOW_ANY_CLASSES": [
        "graphql_auth.mutations.Register",
        "graphql_auth.mutations.VerifyAccount",
        "graphql_auth.mutations.ResendActivationEmail",
        "graphql_auth.mutations.SendPasswordResetEmail",
        "graphql_auth.mutations.PasswordReset",
        "graphql_auth.mutations.ObtainJSONWebToken",
        "graphql_auth.mutations.VerifyToken",
        "graphql_auth.mutations.RefreshToken",
        "graphql_auth.mutations.RevokeToken",
        "graphql_auth.mutations.VerifySecondaryEmail",
    ],
}
GRAPHQL_AUTH = {
    'LOGIN_ALLOWED_FIELDS': ['email', 'username'],
}
