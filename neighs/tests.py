from django.test import TestCase
from .models import *
from django.contrib.auth.models import User


class LocationTestClass(TestCase):
    def setUp(self):
        self.place = Location(name='Testing',created_on='01/02/22',updated_on='01/03/2022')

    def test_instance(self):
        self.assertTrue(isinstance(self.place, Location))

    def test_save_method(self):
        self.place.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.place.save_location()
        self.place.delete()
        locations = Location.objects.all()
        self.assertFalse(len(locations) > 0)

    def tearDown(self):
        Location.objects.all().delete()

class PostTestClass(TestCase):
    def setUp(self):
        self.posttry = Post(title='post trial',description='This a test')

    def test_instance(self):
        self.assertTrue(isinstance(self.posttry, Post))

    def test_save_method(self):
        self.posttry.save()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete_method(self):
        self.posttry.save()
        self.posttry.delete_post()
        posts = Post.objects.all()
        self.assertFalse(len(posts) > 0)

    def test_get_post(self):
        user = 1
        post = Post.get_post(user)
        self.assertFalse(len(post)>0)
    
    def tearDown(self):
        Post.objects.all().delete()

class BusinessTestClass(TestCase):
    def setUp(self):
        self.businesstry = Business(name='Test Business',location='addis',email='test@test.com',created_at='12/05/21')

    def test_instance(self):
        self.assertTrue(isinstance(self.businesstry, Business))

    def test_create_method(self):
        self.businesstry.save()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)

    def test_delete_method(self):
        self.businesstry.save()
        self.businesstry.delete_business()
        businesses = Business.objects.all()
        self.assertFalse(len(businesses) > 0)

    def tearDown(self):
        Business.objects.all().delete()

class NeighborhoodTestClass(TestCase):
    def setUp(self):
        self.hoodtry = NeighborHood(hood_name='Test Business',hood_image='logo.png',help_line='test@test.com',created_on='01/02/22',updated_on='01/05/22',description='Test hood init',resident_count='2')

    def test_instance(self):
        self.assertTrue(isinstance(self.hoodtry,NeighborHood))

    def test_create_method(self):
        self.hoodtry.save()
        businesses = Business.objects.all()
        self.assertFalse(len(businesses) > 0)
    
    def test_delete_method(self):
        self.hoodtry.save()
        self.hoodtry.delete_neighborhood()
        businesses = Business.objects.all()
        self.assertFalse(len(businesses) > 0)