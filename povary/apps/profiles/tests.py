# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from registration.models import RegistrationProfile


class RegistrationTest(TestCase):
    def test_registration(self):
        """
        Test if registration of users works fine
        """
    	data = {
    		"username": "testuser",
    		"email": "pochechyev@gmail.com",
    		"password1": "1",
    		"password2": "1"
    	}
        response = self.client.post(reverse('registration_register'), data)
        user = User.objects.get(username="testuser")
        self.assertEqual(user.is_active, True)

    def test_signal_profile_creation(self):
        """
        Test if profile was created after user creation
        """
        user = User.objects.create(username="testuser")
        self.assertNotEqual(user.profile, None)