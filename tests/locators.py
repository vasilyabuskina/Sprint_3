from selenium.webdriver.common.by import By


class TestLocators():
    LOGIN_IN_ACCOUNT_BUTTON = By.XPATH, "//button[contains(text(),'Войти в аккаунт')]"  # кнопка "Войти в аккаунт" на главной стр
    PROFILE_BUTTON = By.XPATH, "//p[contains(text(),'Личный Кабинет')]"  # кнопка "Личный кабинет" на главной ст
    LOGIN_BUTTON = By.XPATH, "// button[text() = 'Войти']"  # кнопка "Войти" на странице login
    LOGIN_LINK_ON_REG_FORM = By.XPATH, "//a[contains(text(),'Войти')]"  # ссылка "Войти" на странице login и стр восстановления пароля
    EMAIL_FIELD_IN_LOGIN_FORM = By.XPATH, "//label[text()='Email']/following-sibling::input"  # поле email в форме login
    PASSWORD_FIELD_IN_LOGIN_FORM = By.XPATH, "//label[text()='Пароль']/following-sibling::input"  # поле password в форме login

    NAME_FIELD_IN_REG_FORM = By.XPATH, "//label[text()='Имя']/following-sibling::input"  # поле Имя в форме регистрации
    EMAIL_FIELD_IN_REG_FORM = By.XPATH, "//label[text()='Email']/following-sibling::input"  # поле email в форме регистрации
    PASSWORD_FIELD_IN_REG_FORM = By.XPATH, "//label[text()='Пароль']/following-sibling::input"  # поле Пароль в форме регистрации
    REGISTRATION_LINK = By.XPATH, "//a[contains(text(),'Зарегистрироваться')]"  # ссылка Зарегистрироваться
    REGISTRATION_BUTTON = By.XPATH, "//button[contains(text(),'Зарегистрироваться')]"  # кнопка Зарегистрироваться
    LOGIN_TEXT_AFTER_REG = By.XPATH, "//h2[contains(text(),'Вход')]"  # надпись вход

    PASSWORD_RESET_BUTTON =By.XPATH, "//a[contains(text(),'Восстановить пароль')]"  # Восстановить пароль
    LOGOUT_BUTTON = By.XPATH, "//button[contains(text(),'Выход')]"  # Выход
    CONSTRUCTOR_BUTTON = By.XPATH, "// p[text() = 'Конструктор']"  # Конструктор
    ASSEMBLE_BURGER = By.XPATH, "// h1[contains(text(), 'Соберите бургер')]"  # Соберите бургер
    STELLAR_BURGERS_LOGO = By.XPATH, "//header/nav[1]/div[1]/a[1]"  # stellar burgers logo
    SAUCES = By.XPATH, "//span[contains(text(),'Соусы')]"  # Соусы
    BUNS = By.XPATH, "//span[contains(text(),'Булки')]"  # Булки
    FILLINGS = By.XPATH, "//span[contains(text(),'Начинки')]"  # Начинки
    WRONG_PASSWORD = By.XPATH, "//p[contains(text(), 'Некорректный пароль')]"  # Некорректный пароль
    NAME_FIELD_IN_PROFILE = By.XPATH, "//input[@name='Name']"  # Поле Имя в личном кабинете
    PREVIOUS_ORDERS = By.XPATH, "//a[contains(text(),'Профиль')]"  # Профиль
    BEEF_METEORITE = By.XPATH, "//p[contains(text(),'Говяжий метеорит (отбивная)')]"  # Говяжий метеорит
