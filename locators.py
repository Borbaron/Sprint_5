from selenium.webdriver.common.by import By


class Locators:
    KABINET_BUTTON = [By.XPATH, "/html/body/div/div/header/nav/a/p"] #Кнопка Личный кабинет
    VOITI_V_ACCAUNT_BUTTON = [By.XPATH, "//button[text()='Войти в аккаунт']"] #Кнопка Войти в аккаунт
    ENTER_BUTTON = [By.XPATH, "//button[text()='Войти']"] #Кнопка Войти
    ORDER_BUTTON = [By.XPATH, "//button[text()='Оформить заказ']"] #Кнопка оформить заказ
    
    REG_LINK = [By.XPATH, "/html/body/div/div/main/div/div/p[1]/a"] #Ссылка на регистрацию
    REG_BUTTON = [By.XPATH, "/html/body/div/div/main/div/form/button"] #Кнопка зарегистрироваться

    ENT_EMAIL = [By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input"] #Плейсхолдер ИМЕЙЛ во входе
    ENT_PASS = [By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input"] #Плейсхолдер ПАРОЛЬ во входе
    ENT_LINK = [By.XPATH, "/html/body/div/div/main/div/div/p/a"] #Ссылка на вход в форме регистрации

    REG_NAME = [By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input"] #Плейсхолдер ИМЯ в регистрации
    REG_EMAIL = [By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input"] #Плейсхолдер ИМЕЙЛ в регистрации
    REG_PASS = [By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input"] #Плейсхолдер ПАРОЛЬ в регистрации

    ENTER_TEXT = [By.XPATH, "/html/body/div/div/main/div/h2"] #Заголовок Вход
    INCORRECT_PASS = [By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/p"] #Надпись Некорректный пароль
    RECOVER_PASS = [By.LINK_TEXT, "Восстановить пароль"] #Ссылка на восстановление пароля
    HISTORY_LINK = [By.XPATH, "/html/body/div/div/main/div/nav/ul/li[2]/a"] #Ссылка на историю заказов
    CONSTRUCT_BUT = [By.XPATH, "/html/body/div/div/header/nav/ul/li[1]/a/p"] #Кнопка конструктор
    LOGO = [By.XPATH, "/html/body/div/div/header/nav/div/a"] #Лого сайта