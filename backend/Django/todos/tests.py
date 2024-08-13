from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Todo

# Create your tests here.
class TodoModelTest(TestCase):  
    @classmethod
    def setUpTestData(cls) -> None:
        cls.todo = Todo.objects.create(title='first todo', body='A body of text here')



    def test_model_content(self):
        self.assertEqual(self.todo.title, 'first todo')
        self.assertEqual(self.todo.body, 'A body of text here')
        self.assertEqual(str(self.todo), 'first todo')


    def test_api_listview(self):
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)


    def test_api_detailview(self):
        response = self.client.get(reverse('todo_detail', kwargs={'pk': self.todo.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, 'first todo')

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'first todo')


    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.body}'
        self.assertEquals(expected_object_name, 'A body of text here')