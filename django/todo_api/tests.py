from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from datetime import datetime
from .models import Task
from SDG23.solve import getMaxSum, uniqueChars

class TaskTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_data = {'title': 'Finish the project', 'description': 'Complete the remaining tasks'}
        self.response = self.client.post(reverse('task_list'), self.task_data, format='json')
        self.task_id = self.response.data['id']
        self.due_date = datetime.now()

        self.task_with_due_date_data = {'title': 'Finish the project', 'description': 'Complete the remaining tasks', 'due_date': self.due_date}
        self.response_with_due_date = self.client.post(reverse('task_list'), self.task_with_due_date_data, format='json')
        self.task_with_due_date_id = self.response_with_due_date.data['id']

    def test_create_task(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_get_all_tasks(self):
        response = self.client.get(reverse('task_list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_task(self):
        response = self.client.get(reverse('task_detail', kwargs={'task_id': self.task_id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task(self):
        updated_task = {'title': 'Finish the project', 'description': 'Complete all the remaining tasks', 'due_date': self.due_date}
        response = self.client.patch(reverse('task_detail', kwargs={'task_id': self.task_id}), updated_task, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        response = self.client.delete(reverse('task_detail', kwargs={'task_id': self.task_id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_mark_task_as_complete(self):
        response = self.client.patch(reverse('task_complete', kwargs={'task_id': self.task_id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_completed_tasks(self):
        response = self.client.get(reverse('task_list') + '?status=completed', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_uncompleted_tasks(self):
        response = self.client.get(reverse('task_list') + '?status=uncompleted', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_tasks_by_due_date(self):
        response = self.client.get(reverse('task_list') + '?due_date=' + str(self.due_date.date()), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], self.task_with_due_date_id)
        self.assertEqual(response.data[0]['due_date'], self.due_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ'))

        
####################### Unit test for algorithms Questions in solve.py #######################       
class TestUniqueChars(TestCase):
    def test_empty_string(self):
        self.assertEqual(uniqueChars(''), '')

    def test_whitespace_string(self):
        self.assertEqual(uniqueChars('  \t   '), '')

    def test_all_unique_chars(self):
        self.assertEqual(uniqueChars('abcdefg'), 'abcdefg')

    def test_only_unique_chars(self):
        self.assertEqual(uniqueChars('hello world'), 'helo wrd')
        self.assertEqual(uniqueChars('foo bar baz'), 'fo barz')
        self.assertEqual(uniqueChars('python django'), 'python djag')

    def test_preserves_order(self):
        self.assertEqual(uniqueChars('abca'), 'abc')
        self.assertEqual(uniqueChars('abbac'), 'abc')
        self.assertEqual(uniqueChars('abcabc'), 'abc')


class TestGetMaxSum(TestCase):
    def test_maximum_sum(self):
        self.assertEqual(getMaxSum([1, -2, 3, 4, -5, 8]), 10)
        self.assertEqual(getMaxSum([-1, 2, 3, -4, 5, 10]), 16)
        self.assertEqual(getMaxSum([1, 2, 3, 4, 5]), 15)
        self.assertEqual(getMaxSum([-1, -2, -3, -4, -5]), 0)
        self.assertEqual(getMaxSum([5]), 5)

    def test_empty_or_negative_array(self):
        self.assertEqual(getMaxSum([]), 0)
        self.assertEqual(getMaxSum([-1, -2, -3]), 0)
