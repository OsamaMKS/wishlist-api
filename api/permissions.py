from rest_framework.permissions import BasePermission
from datetime import date


class IsOwnerOrStaff(BasePermission):
     message = "You can't view the details of this item as you did not add it"

     def has_object_permission(self, request, view, obj):
         if request.user.is_staff or obj.added_by == request.user:
             return True
         return False
