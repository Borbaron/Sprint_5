from selenium.webdriver.common.by import By


class Locators:
    KABINET_BUTTON = [By.XPATH, "//p[text()='Личный Кабинет']"] #Кнопка Личный кабинет
    VOITI_V_ACCAUNT_BUTTON = [By.XPATH, "//button[text()='Войти в аккаунт']"] #Кнопка Войти в аккаунт
    ENTER_BUTTON = [By.XPATH, "//button[text()='Войти']"] #Кнопка Войти
    ORDER_BUTTON = [By.XPATH, "//button[text()='Оформить заказ']"] #Кнопка оформить заказ
    
    REG_LINK = [By.LINK_TEXT, "Зарегистрироваться"] #Ссылка на регистрацию
    REG_BUTTON = [By.XPATH, "//button[text()='Зарегистрироваться']"] #Кнопка зарегистрироваться

    ENT_EMAIL = [By.NAME, "name"] #Плейсхолдер ИМЕЙЛ во входе
    ENT_PASS = [By.NAME, "Пароль"] #Плейсхолдер ПАРОЛЬ во входе
    ENT_LINK = [By.CSS_SELECTOR, ".Auth_link__1fOlj"] #Ссылка на вход в форме регистрации

    REG_NAME = [By.XPATH, "//label[text()='Имя']/following-sibling::input[@type='text' and @name='name']"] #Плейсхолдер ИМЯ в регистрации
    REG_EMAIL = [By.XPATH, "//label[text()='Email']/following-sibling::input[@type='text']"] #Плейсхолдер ИМЕЙЛ в регистрации
    REG_PASS = [By.NAME, "Пароль"] #Плейсхолдер ПАРОЛЬ в регистрации

    ENTER_TEXT = [By.XPATH, "//h2[text()='Вход']"] #Заголовок Вход
    INCORRECT_PASS = [By.XPATH, "//p[text()='Некорректный пароль']"] #Надпись Некорректный пароль
    RECOVER_PASS = [By.LINK_TEXT, "Восстановить пароль"] #Ссылка на восстановление пароля
    HISTORY_LINK = [By.XPATH, "//a[@href='/account/order-history' and text()='История заказов']"] #Ссылка на историю заказов
    CONSTRUCT_BUT = [By.XPATH, "//p[text()='Конструктор']"] #Кнопка конструктор
    LOGO = [By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2 a"] #Лого сайта
    EXIT_BUTTON = [By.CSS_SELECTOR, "button.Account_button__14Yp3.text.text_type_main-medium.text_color_inactive"] #Кнопка ВЫХОД в личном кабинете

    BUNS_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and not(contains(@class, 'tab_tab_type_current__2BEPc')) and .//span[text()='Булки']]") #Кнопка Булки НЕ активная
    SAUCES_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and not(contains(@class, 'tab_tab_type_current__2BEPc')) and .//span[text()='Соусы']]") #Кнопка Соусы НЕ активная
    TOPPINGS_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and not(contains(@class, 'tab_tab_type_current__2BEPc')) and .//span[text()='Начинки']]") #Кнопка Начинки Не активная

    BUNS_BUTTON_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'tab_tab_type_current__2BEPc') and .//span[text()='Булки']]") #Кнопка Булки АКТИВНАЯ
    SAUCES_BUTTON_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'tab_tab_type_current__2BEPc') and .//span[text()='Соусы']]") #Кнопка Соусы АКТИВНАЯ
    TOPPINGS_BUTTON_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'tab_tab_type_current__2BEPc') and .//span[text()='Начинки']]") #Кнопка Начинки АКТИВНАЯ
