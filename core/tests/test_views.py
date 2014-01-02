from django.test import TestCase
from django.core.urlresolvers import reverse as r


class IndexTest(TestCase):

    def setUp(self):
        url = r('core:index')
        self.resp = self.client.get(url)

    def test_get(self):
        'GET deve retornar status 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_html(self):
        pass

    def test_template(self):
        'Index must use a templa  core/index.html'
        self.assertTemplateUsed(self.resp, 'core/index.html')


class ListVideoTest(TestCase):

    def setUp(self):
        url = r('core:videos')
        self.resp = self.client.get(url)

    def test_get(self):
        'GET deve retornar status 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Index must use a templa  core/videos.html'
        self.assertTemplateUsed(self.resp, 'core/videos.html')


class PlayerTest(TestCase):

    def setUp(self):
        url = r('core:video_player',kwargs={'slug':'teste-video'})
        self.resp = self.client.get(url)

    def test_get(self):
        'GET deve retornar status 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Index must use a template  core/index.html'
        self.assertTemplateUsed(self.resp, 'core/player.html')

    def test_html(self):
        '''
        Deve possuir o elemento do video, titulo, categoria,
        descricao
        '''
        self.assertContains(self.resp, 'video')


