"""
Django settings for filmlog project.

Generated by 'django-admin startproject' using Django 5.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x3pgm))50*6$%+4rfohj=(^u1rw2oy2&%c#(2j_!c$nff^l3o3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'film',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'filmlog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'filmlog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Redirect user yang belum login
LOGIN_URL = '/login/'

# Konfigurasi upload media (gambar cover film)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

JAZZMIN_SETTINGS = {
    # Site branding
    "site_title": "FilmLog Admin",
    "site_header": "🎬 FilmLog Admin",
    "site_brand": "FilmLog",
    "welcome_sign": "Selamat datang di panel admin FilmLog!",
    
    # Logo settings
    "site_logo": None,
    "login_logo": None,
    "site_icon": None,
    
    # Layout & Navigation
    "show_sidebar": True,
    "navigation_expanded": True,
    "sidebar_disable_expand": False,
    "sidebar_fixed": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["film", "auth"],
    
    # Theme configuration
    "theme": "flatly",
    "dark_mode_theme": None,
    "custom_css": "css/custom_admin.css",
    "custom_js": None,
    
    # User settings
    "user_avatar": None,
    "show_ui_builder": False,
    
    # Top menu configuration - KOSONG untuk navbar biru kosong
    "topmenu_links": [],
    
    # Sidebar menu customization
    "usermenu_links": [
        {"name": "🌐 Lihat Website", "url": "/", "new_window": True},
        {"model": "auth.user"}
    ],
    
    # Model icons
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "film": "fas fa-film",
        "film.film": "fas fa-video",
        "film.review": "fas fa-star",
        "film.genre": "fas fa-tags",
    },
    
    # Default icon for models/apps
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    
    # Custom links in sidebar
    "custom_links": {
        "film": [{
            "name": "Statistik Film",
            "url": "admin:index",
            "icon": "fas fa-chart-bar",
            "permissions": ["film.view_film"]
        }]
    },
    
    # Related modal
    "related_modal_active": False,
    
    # UI Tweaks
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs"
    },
    
    # Language
    "language_chooser": False,
}
