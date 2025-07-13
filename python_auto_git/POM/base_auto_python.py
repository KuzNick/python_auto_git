# Создай базовый класс BasePage с методом __init__(self, driver)
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        

# Наследуй LoginPage(BasePage); добавь методы open() и login()      
class LoginPage(BasePage):
    def open(self):
        print("Method open")
        return "http://google.com"
        
    def login(self):
        print("Method login")
        return "Успешный вход"
        
