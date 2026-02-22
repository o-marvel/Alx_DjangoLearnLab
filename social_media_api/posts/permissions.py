from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission:
    - Allow everyone to read (GET)
    - Only owner can edit or delete
    """

    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, OPTIONS
        if request.method in SAFE_METHODS:
            return True

        # Only allow owner to edit/delete
        return obj.author == request.user