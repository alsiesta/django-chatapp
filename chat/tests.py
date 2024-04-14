from django.test import TestCase, Client
from django.contrib.auth.models import User
from chat.models import Chat, Message

class IndexViewTest(TestCase):
    def setUp(self):
        print("Running setUp test")
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.chat = Chat.objects.create(id=1)
        self.message = Message.objects.create(text='Hello, World!', chat=self.chat, author=self.user, receiver=self.user)

    def test_index_view(self):
        print("Running test_index_view test")
        self.client.login(username='testuser', password='12345')
        response = self.client.get('/chat/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello, World!')