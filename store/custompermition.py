from rest_framework import permissions


class isAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        print("askljdf")
        return request.method in permissions.SAFE_METHODS or request.user.is_staff
    
class creatorOrAdminOnly(permissions.BasePermission):
    def has_object_permission(self, request,view,obj):
        print("done all write tha tis all i need to do ")
        return bool( request.user.is_staff or request.user == obj.customer.user)