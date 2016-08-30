"""
Tests for the signup views.
"""
from collections import namedtuple
from django.test import TestCase
from .. import views

MockUser = namedtuple('MockUser', ['is_staff'])
MockRequest = namedtuple('MockRequest', ['method', 'user'])

class TestIsStaffOrPostOnlyPermission(TestCase):
    """
    Tests for the IsStaffOfPostOnly custom permission class.
    """
    def test_has_permission_on_post(self):
        """
        Ensure that a user has permission even if not staff.
        """
        user = MockUser(is_staff=False)
        request = MockRequest(method='POST', user=user)
        permission = views.IsStaffOrPostOnly()
        self.assertTrue(permission.has_permission(request, None))

    def test_no_permission_on_get(self):
        """
        Ensure that non-staff users have no permission on get.
        """
        user = MockUser(is_staff=False)
        request = MockRequest(method='GET', user=user)
        permission = views.IsStaffOrPostOnly()
        self.assertFalse(permission.has_permission(request, None))

    def test_staff_permission_on_get(self):
        """
        Ensure that a staff user has permission on get.
        """
        user = MockUser(is_staff=True)
        request = MockRequest(method='GET', user=user)
        permission = views.IsStaffOrPostOnly()
        self.assertTrue(permission.has_permission(request, None))
