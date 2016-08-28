"""
Views for the Signups API.
"""
from rest_framework import generics, status
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from . import models, serializers

class IsStaffOrPostOnly(BasePermission):
    """
    Permission class to allow all methods if the user is staff and only allow
    POST if not.
    """
    def has_permission(self, request, view):
        """
        Return True if the method is POST, or if the request user is staff.
        Return False otherwise.
        """
        return request.method == 'POST' or \
                (request.user and request.user.is_staff)


class SignupView(generics.ListCreateAPIView):
    """
    API viewset that allows the viewing of (if admin) and creation of signups.
    """
    queryset = models.Signup.objects.all()
    serializer_class = serializers.SignupSerializer
    permission_classes = (IsStaffOrPostOnly,)

