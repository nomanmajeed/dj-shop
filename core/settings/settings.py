import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-m5!9657vdbrq=yie36)fcqpo@c^ze3%5vkeaxn*prvw!$%%chb"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["dj-shop-nm.herokuapp.com", "127.0.0.1", "localhost"]


# Application definition

INSTALLED_APPS = [
    # Project Apps
    "store",
    "basket",
    "account",
    "payment",
    "orders",
    # Django Default Apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    # 3rd Party Middlewares
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # Django Default Middlewares
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "store.context_processors.categories",
                "basket.context_processors.basket",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATIC_URL = "/static/"

# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

PROJECT_ROOT = os.path.join(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, "staticfiles")
STATIC_URL = "/static/"

# Extra lookup directories for collectstatic to find static files
STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, "static"),)

#  Add configuration for static files storage using whitenoise
STATICFILES_STORAGE = "whitenoise.django.GzipManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Custom user model
AUTH_USER_MODEL = "account.UserBase"
LOGIN_REDIRECT_URL = "/account/dashboard"
LOGIN_URL = "/account/login/"


# Email setting
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Basket session ID
BASKET_SESSION_ID = "basket"

# Stripe Payment
os.environ.setdefault(
    "STRIPE_PUBLISHABLE_KEY",
    "pk_test_51BbYtuJMWp5ChnxjeZRr4Dvtr8IzOSsfSewYg31o815lMGqbVfQTz59tUVWH7Ks4Ug1z7sXgaNb25JpLiOgaboPn000HKcJjUB",
)
STRIPE_SECRET_KEY = (
    "sk_test_51BbYtuJMWp5ChnxjRM6t9vQvB4P2hMUqaXc3CORwOJ4EfVJ7QpZy61Rqe59WBOkiN0gJvfbckZsfV33T9TUnVqKt00An6UjSQW"
)
# STRIPE_ENDPOINT_SECRET = ''
# stripe listen --forward-to localhost:8000/payment/webhook/

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": (
                "%(asctime)s [%(process)d] [%(levelname)s] "
                "pathname=%(pathname)s lineno=%(lineno)s "
                "funcname=%(funcName)s %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "null": {
            "level": "DEBUG",
            "class": "logging.NullHandler",
        },
        "console": {"level": "INFO", "class": "logging.StreamHandler", "formatter": "verbose"},
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
