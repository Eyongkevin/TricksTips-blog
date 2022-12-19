from pathlib import Path

SITE_ID = 1

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Application definition

DEFAULT_APPS = [
    # add default apps here
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
]
CREATED_APPS = [
    # add created apps here
    "blogs.blog.apps.BlogConfig",
    "blogs.like.apps.LikeConfig",
    "blogs.category.apps.CategoryConfig",
    "blogs.core.apps.CoreConfig",
]

THIRD_PARTY_APPS = [
    # add third-party apps here
    "rangefilter",
    "taggit",
    "django_ckeditor_5",
]

INSTALLED_APPS = [*DEFAULT_APPS, *CREATED_APPS, *THIRD_PARTY_APPS]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(BASE_DIR.joinpath("templates"))],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


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

STATIC_URL = "/static/"
STATICFILES_DIRS = [str(BASE_DIR.joinpath("static"))]
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

customColorPalette = [
    {"color": "hsl(4, 90%, 58%)", "label": "Red"},
    {"color": "hsl(340, 82%, 52%)", "label": "Pink"},
    {"color": "hsl(291, 64%, 42%)", "label": "Purple"},
    {"color": "hsl(262, 52%, 47%)", "label": "Deep Purple"},
    {"color": "hsl(231, 48%, 48%)", "label": "Indigo"},
    {"color": "hsl(207, 90%, 54%)", "label": "Blue"},
]

# CKEDITOR_5_CUSTOM_CSS = 'path_to.css' # optional
# CKEDITOR_5_FILE_STORAGE = "path_to_storage.CustomStorage" # optional
# CKEDITOR_5_CONFIGS = {
#     "default": {
#         "skin": "moono",
#         "toolbar": [
#             "heading",
#             "|",
#             "bold",
#             "italic",
#             "link",
#             "bulletedList",
#             "numberedList",
#             "blockQuote",
#             "imageUpload",
#         ],
#     },
#     "extends": {
#         "blockToolbar": [
#             "paragraph",
#             "heading1",
#             "heading2",
#             "heading3",
#             "|",
#             "bulletedList",
#             "numberedList",
#             "|",
#             "blockQuote",
#         ],
#         "toolbar": [
#             "heading",
#             "|",
#             "outdent",
#             "indent",
#             "|",
#             "bold",
#             "italic",
#             "link",
#             "underline",
#             "strikethrough",
#             "code",
#             "subscript",
#             "superscript",
#             "highlight",
#             "|",
#             "codeBlock",
#             "sourceEditing",
#             "insertImage",
#             "bulletedList",
#             "numberedList",
#             "todoList",
#             "|",
#             "blockQuote",
#             "imageUpload",
#             "|",
#             "fontSize",
#             "fontFamily",
#             "fontColor",
#             "fontBackgroundColor",
#             "mediaEmbed",
#             "removeFormat",
#             "insertTable",
#         ],
#         "image": {
#             "toolbar": [
#                 "imageTextAlternative",
#                 "|",
#                 "imageStyle:alignLeft",
#                 "imageStyle:alignRight",
#                 "imageStyle:alignCenter",
#                 "imageStyle:side",
#                 "|",
#             ],
#             "styles": [
#                 "full",
#                 "side",
#                 "alignLeft",
#                 "alignRight",
#                 "alignCenter",
#             ],
#         },
#         "table": {
#             "contentToolbar": [
#                 "tableColumn",
#                 "tableRow",
#                 "mergeTableCells",
#                 "tableProperties",
#                 "tableCellProperties",
#             ],
#             "tableProperties": {
#                 "borderColors": customColorPalette,
#                 "backgroundColors": customColorPalette,
#             },
#             "tableCellProperties": {
#                 "borderColors": customColorPalette,
#                 "backgroundColors": customColorPalette,
#             },
#         },
#         "heading": {
#             "options": [
#                 {
#                     "model": "paragraph",
#                     "title": "Paragraph",
#                     "class": "ck-heading_paragraph",
#                 },
#                 {
#                     "model": "heading1",
#                     "view": "h1",
#                     "title": "Heading 1",
#                     "class": "ck-heading_heading1",
#                 },
#                 {
#                     "model": "heading2",
#                     "view": "h2",
#                     "title": "Heading 2",
#                     "class": "ck-heading_heading2",
#                 },
#                 {
#                     "model": "heading3",
#                     "view": "h3",
#                     "title": "Heading 3",
#                     "class": "ck-heading_heading3",
#                 },
#             ]
#         },
#     },
#     "list": {
#         "properties": {
#             "styles": "true",
#             "startIndex": "true",
#             "reversed": "true",
#         }
#     },
# }

CKEDITOR_5_CONFIGS = {
    "default": {
        "skin": "moono",
        "toolbar": [
            "heading",
            "|",
            "italic",
            "link",
            "bulletedList",
            "numberedList",
            "blockQuote",
            "imageUpload",
        ],
    },
    "extends": {
        "blockToolbar": [
            "paragraph",
            "heading1",
            "heading2",
            "heading3",
            "|",
            "bulletedList",
            "numberedList",
            "|",
            "blockQuote",
        ],
        "toolbar": [
            "heading",
            "|",
            "outdent",
            "indent",
            "|",
            "linespace",
            "bold",
            "italic",
            "link",
            "underline",
            "strikethrough",
            "code",
            "subscript",
            "superscript",
            "highlight",
            "|",
            "codeBlock",
            "sourceEditing",
            "insertImage",
            "bulletedList",
            "numberedList",
            "todoList",
            "|",
            "blockQuote",
            "imageUpload",
            "|",
            "fontSize",
            "fontFamily",
            "fontColor",
            "fontBackgroundColor",
            "mediaEmbed",
            "removeFormat",
            "insertTable",
        ],
        "image": {
            "toolbar": [
                "imageTextAlternative",
                "|",
                "imageStyle:alignLeft",
                "imageStyle:alignRight",
                "imageStyle:alignCenter",
                "imageStyle:side",
                "|",
            ],
            "styles": [
                "full",
                "side",
                "alignLeft",
                "alignRight",
                "alignCenter",
            ],
        },
        "table": {
            "contentToolbar": [
                "tableColumn",
                "tableRow",
                "mergeTableCells",
                "tableProperties",
                "tableCellProperties",
            ],
            "tableProperties": {
                "borderColors": customColorPalette,
                "backgroundColors": customColorPalette,
            },
            "tableCellProperties": {
                "borderColors": customColorPalette,
                "backgroundColors": customColorPalette,
            },
        },
        "heading": {
            "options": [
                {
                    "model": "paragraph",
                    "title": "Paragraph",
                    "class": "ck-heading_paragraph",
                },
                {
                    "model": "heading1",
                    "view": "h1",
                    "title": "Heading 1",
                    "class": "ck-heading_heading1",
                },
                {
                    "model": "heading2",
                    "view": "h2",
                    "title": "Heading 2",
                    "class": "ck-heading_heading2",
                },
                {
                    "model": "heading3",
                    "view": "h3",
                    "title": "Heading 3",
                    "class": "ck-heading_heading3",
                },
            ]
        },
    },
    #     "list": {
    #         "properties": {
    #             "styles": "true",
    #             "startIndex": "true",
    #             "reversed": "true",
    #         }
    #     },
}
