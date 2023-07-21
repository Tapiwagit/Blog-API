from rest_framework import permissions


class IsAuthOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Auth users only cna see listy view
        if request.user.is_authenticated:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        # read permissions are allowed to author of post
        return obj.author == request.user
