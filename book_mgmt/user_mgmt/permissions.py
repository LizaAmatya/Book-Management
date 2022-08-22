from django.contrib.auth.mixins import PermissionRequiredMixin


class BookManagementPermission(PermissionRequiredMixin):
    permission_required = 'user_mgmt.book_mgmt_perm'

