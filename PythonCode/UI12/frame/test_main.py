from PythonCode.UI12.frame.main_page import MainPage


class TestMain:
    def test_main_page(self):
        main = MainPage().goto_market().goto_search()