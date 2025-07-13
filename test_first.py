import pytest
from python_auto_git.POM.base_auto_python import LoginPage

def test_login_success():
    page = LoginPage("driver")
    
    # Вызываем метод login
    result = page.login()
    
    # Вызываем метод open
    result1 = page.open()
    
    # Проверяем, что метод login вернул ожидаемый результат
    assert result == "Успешный вход", "Тест провален"
    assert result1 == "http://google.com", "Тест провален"
    
