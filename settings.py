from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = 'your-secret-key-here'  # замените на случайную строку в продакшене

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'crispy_forms',
    'crispy_bootstrap5',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalog.apps.CatalogConfig',
    'django_extensions',
    'blog',
    'users',
]

CRISPY_TEMPLATE_PACK = 'bootstrap5'

AUTH_USER_MODEL = "users.User"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # папка для общих шаблонов проекта
        ],
        'APP_DIRS': True,  # автоматически ищет папку templates в каждом приложении
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ADMIN_EMAIL = 'walfisch91@gmail.com'
ADMINS = [('Admin', ADMIN_EMAIL)]
MANAGERS = ADMINS

# Режим разработки: письма падают в консоль (терминал runserver)
# Режим продакшена: письма уходят на реальный SMTP
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'noreply@skystore.local'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.yandex.ru'           # <-- замените на свой почтовый сервер
    EMAIL_PORT = 465
    EMAIL_USE_SSL = True
    # EMAIL_USE_TLS = True                  # раскомментируйте, если порт 587
    # EMAIL_PORT = 587

    EMAIL_HOST_USER = 'blog@skystore.local' # <-- ваша РЕАЛЬНАЯ почта
    EMAIL_HOST_PASSWORD = 'пароль_приложения'  # <-- пароль приложения, не обычный!

    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER    # отправитель = ваша почта (обязательно!)
    SERVER_EMAIL = EMAIL_HOST_USER 


print("=" * 50)
print("BASE_DIR:", BASE_DIR)
print("STATICFILES_DIRS:", STATICFILES_DIRS)
print("=" * 50)

LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = 'catalog:home'