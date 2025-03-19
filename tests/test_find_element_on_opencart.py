from selenium.webdriver.common.by import By


def test_home_page(browser):
    browser.get("http://192.168.100.49:8081/")
    browser.find_element(By.CSS_SELECTOR, "title") #Заголовок
    browser.find_element(By.CLASS_NAME, "dropdown") #Корзина
    browser.find_element(By.NAME, "search") #Поиск
    browser.find_element(By.CLASS_NAME, "product-thumb") #Карточка товара
    browser.find_element(By.LINK_TEXT, "Contact Us") #Футер, кнопка Контакты


def test_category_page(browser):
    browser.get("http://192.168.100.49:8081/en-gb/catalog/desktops")
    browser.find_element(By.ID, "product-list") #Товары в каталоге
    browser.find_element(By.ID, "display-control") #Все фильтры
    browser.find_element(By.CLASS_NAME, "pagination") #Пагинация
    browser.find_element(By.ID, "column-left") #Левая колонка с фильтрами по десктопам
    browser.find_element(By.TAG_NAME, "li") #Фильтр над карточками товаров


def test_product_page(browser):
    browser.get("http://192.168.100.49:8081/en-gb/product/desktops/apple-cinema")
    browser.find_element(By.XPATH, "//*[text()='Apple Cinema 30\"']") #Название товара
    browser.find_element(By.CLASS_NAME, "col-sm") #Описание товара с чекбоксами (не текстовое)
    browser.find_element(By.CLASS_NAME, "img-thumbnail.mb-3") #Картинка товара
    browser.find_element(By.ID, "button-cart") #Кнопка добавить в корзину
    browser.find_element(By.CLASS_NAME, "tab-content") #Описание товара текст


def test_admin_login_page(browser):
    browser.get("http://192.168.100.49:8081/administration/")
    browser.find_element(By.ID, "input-username") #Логин
    browser.find_element(By.ID, "input-password") #Пароль
    browser.find_element(By.CLASS_NAME, "btn.btn-primary") #Кнопка логина
    browser.find_element(By.CLASS_NAME, "card-header") #Шапка админки
    browser.find_element(By.CLASS_NAME, "input-group-text") #Иконка логина


def test_registration_page(browser):
    browser.get("http://192.168.100.49:8081/index.php?route=account/register")
    browser.find_element(By.NAME, "firstname") #Имя
    browser.find_element(By.NAME, "lastname") #Фамилия
    browser.find_element(By.NAME, "email") #Почта
    browser.find_element(By.NAME, "password")  # Пароль
    browser.find_element(By.NAME, "newsletter") #Чекбокс подписки

