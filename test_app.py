from seleniumbase import BaseCase

class MyTest(BaseCase):
    def test_title_and_form(self):
        self.open("http://127.0.0.1:5000")
        self.assert_text("Hello, World!", "h1")
        self.type('input[name="name"]', "Eylem")
        self.click('input[name="subscribe"]')
        self.click("button")
