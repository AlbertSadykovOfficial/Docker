import unittest
import identidock


class TestCase(unittest.TestCase):
    # Инициалзация тестовой версии приложения с исп Flask
    def setUp(self):
        identidock.app.config["TESTING"] = True
        self.app = identidock.app.test_client()

    # Тестирование метода, вызывающего URL / 
    # С передачей в поле значения Moby Dick
    # Затем мы проверяем код возврата на равенстов 200
    # Полученные данные должны содержать Hello и Moby Dick
    def test_get_mainpage(self):
        page = self.app.post("/", data=dict(name="Moby Dock"))
        assert page.status_code == 200
        assert 'Hello' in str(page.data)
        assert 'Moby Dock' in str(page.data)

    # Проверка правильности экранирования  HTML-элементов
    def test_html_escaping(self):
        page = self.app.post("/", data=dict(name='"><b>TEST</b><!--'))
        assert '<b>' not in str(page.data)


if __name__ == '__main__':
    unittest.main()
