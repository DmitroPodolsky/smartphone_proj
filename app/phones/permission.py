from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import serializers
class IsAuthenticatedOrReadOnlyAndOwner(BasePermission):
    def has_permission(self, request, view):
        if 'pk' in view.kwargs and view.kwargs['pk']:
            if request.method in SAFE_METHODS:
                return True
            try:
               obj = view.get_queryset()[0]
            except:
                raise serializers.ValidationError({'error':'wrong id'})
            if bool(request.user and request.user.is_authenticated and (obj.accounts_id == request.user.id or request.user.is_staff)) == False:
                raise serializers.ValidationError({'error': 'wrong token or you not author this comment'})
            return True
        else:
            return bool(
                request.method in SAFE_METHODS or
                request.user and
                request.user.is_authenticated)