from types import SimpleNamespace
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed

class TokenUser(SimpleNamespace):
    @property
    def is_authenticated(self):
        return True

class ServiceJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        user_id = validated_token.get("user_id") or validated_token.get("id")
        if not user_id:
            raise AuthenticationFailed("Token missing user_id")

        payload = validated_token.payload
        return TokenUser(id=user_id, payload=payload)