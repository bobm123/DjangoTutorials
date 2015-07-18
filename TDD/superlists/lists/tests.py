from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from django.shortcuts import render
from django.template.loader import render_to_string

from lists.views import home_page
from lists.models import Item


class SmokeTest(TestCase):

#    def test_bad_maths(self):
#        self.assertEqual(1 + 1, 3)

    def test_good_maths(self):
        self.assertEqual(1 + 1, 2)


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') 
        self.assertEqual(found.func, home_page)
        
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        #print ('***************')
        #print (response.content)
        #print ('***************')
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
        
    def test_home_page_can_save_a_POST_request(self):
        myListItem = 'A new list item'
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = myListItem
    
        response = home_page(request)
    
        self.assertEqual(Item.objects.count(), 1)  #1
        new_item = Item.objects.first()  #2 same as: objects.all()[0]
        self.assertEqual(new_item.text, 'A new list item')  #3

        # Expecting a redirect now...
        #self.assertIn(myListItem, response.content.decode())
        #expected_html = render_to_string(
        #    'home.html',
        #    {'new_item_text':  myListItem}
        #)
        #self.assertEqual(response.content.decode(), expected_html)
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')


    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.count(), 0)
        

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
        
        