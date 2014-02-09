twentytab-image-ui
==================

A django app that implements an admin to have thumbnails with colorbox.js

## Installation

Use the following command: <b><i>pip install twentytab-image-ui</i></b>


## Usage


```py
from django.contrib import admin
from testapp.models import ModelTest
from image_ui.admin import AdminThumbnail, ColorBoxAdmin


class ModelTestAdmin(ColorBoxAdmin):
    admin_thumbnail = AdminThumbnail(image_field='thumb', original_image='image')

    list_display = (..., 'admin_thumbnail', ...)

admin.site.register(ModelTest, ModelTestAdmin)


```