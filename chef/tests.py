'''
  // written by: Patrick Carra
  // tested by: Patrick Carra
  // debugged by: Patrick Carra
  // etc.
'''

from django.contrib.auth.models import AnonymousUser
from django.http import Http404
from django.test import TestCase, RequestFactory
from django.urls import resolve
from django.urls.exceptions import Resolver404
from mixer.backend.django import mixer

from . import views
from tickets.models import Orderstable

# Create your tests here.
class ViewRequestFactoryTestMixin(object):
    longMessage = True
    view_class = None

    def get_response(self, method):
        factory = RequestFactory()
        req = getattr(factory, method) ('/')
        req.user = AnonymousUser()
        return self.view_class.as_view() (req, *[], **{})

    def is_callable(self):
        resp = self.get_response('get')
        self.assertEqual(resp.status_code, 200)

class ViewTestMixin(object):
    """Mixin with shortcuts for view tests"""
    longMessage = True #More verbose error messages
    view_class = None

    def get_view_kwarg(self):
        """
        Returns a dict representing the view's kwargs, if
        necessary.
        If the URL of this view is constructed via kwargs, you can
        override this method and return the proper kwargs for the 
        test.
        """
        return {}

    def get_response(self, method, user, data, args, kwargs):
        """Creates a request and a response object"""
        factory= RequestFactory()
        req_kwargs = {}
        if data:
            req_kwargs.update({'data': data})
        req = getattr(factory, method)('/', **req_kwargs)
        req.user = user if user else AnonymousUser()
        return self.view_class.as_view() (req, *args, **kwargs)

    def is_callable(self, user=None, post=False, to=None, data={}, args=[], kwargs={},):
        """Initiates a call and tests the outcome."""
        view_kwargs = kwargs or self.get_view_kwargs()
        resp = self.get_response(
            'post' if post else 'get',
            user=user,
            data=data,
            args=args,
            kwargs=view_kwargs,
        )
        if to:
            self.assertIn(resp.status_code, [301, 302],
                            msg="The request was not redirected.")
            name = resp.url.split('?')[0].split('#')[0].url_name
            try:
                self.AssertEqual(
                    resolve(name, to,
                    msg='Should redirect to "{}".'.format(to)))
            except Resolver404:
                raise Exception(
                                'Could not resolve "{}".'.format(resp.url))
        else:
            self.AssertEqual(resp.status_code, 200)

    def is_not_callable(self, **kwargs):
        """Tests if call raises a 404."""
        with self.assertRaises(Http404):
            self.is_callable(**kwargs)

class ExampleViewTestCase(ViewRequestFactoryTestMixin, TestCase):
    view_class = views.dashboard
    
    def test_get(self):
        self.is_callable()

class UpdateViewTestCase(ViewTestMixin, TestCase):
    """Tests for the 'UpdateView' class."""
    view_class = views.sendBack

    def setUp(self):
        self.obj = mixer.blend(Orderstable)

    def get_view_kwargs(self):
        return {'pk': self.obj.pk}

    def test_anonymous(self):
        self.is_callable(to='login')

    def test_get(self):
        self.is_callable(user=mixer.blend('auth.User'))

    def test_post(self):
        self.is_callable(post=True, user=mixer.blend('auth.User'),
                         data={'messsage': 'what did they order?'}, to='whatever')