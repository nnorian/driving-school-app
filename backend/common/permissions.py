from rest_framework.permissions import BasePermission

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return getattr(request.user, "role", None) == request.user.ROLE_STUDENT
    

class IsInstructor(BasePermission):
    def has_permission(self, request, view):
        return getattr(request.user, "role", None) == request.user.ROLE_INSTRUCTOR

class IsDirector(BasePermission):
    def has_permission(self, request, view):
        return getatt(request.user, "role", None) == request.user.ROLE_DIRECTOR