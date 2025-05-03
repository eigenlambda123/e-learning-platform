from rest_framework.permissions import BasePermission

class IsEnrolled(BasePermission):
    def object_has_permission(self, request, view, obj):
        return obj.students.filter(id=request.user.id).exist()