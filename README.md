twentytab-image-ui
==================

A django app that implements an admin to have thumbnails with colorbox.js

## Installation

Use the following command: <b><i>pip install twentytab-image-ui</i></b>

## Configuration

Run collectstatic command or map static directory.

## Usage

- models-py

```py

from django.db import models
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField


class ModelTest(models.Model):
    image = models.ImageField(upload_to='your_media_path')
    thumb = ImageSpecField(
        source='image',
        processors=[ResizeToFill(50, 50)],
        format='JPEG',
        options={'quality': 99}
    )

```

- admin.py

```py
from django.contrib import admin
from testapp.models import ModelTest
from image_ui.admin import AdminThumbnail, ColorBoxAdmin


class ModelTestAdmin(ColorBoxAdmin):
    admin_thumbnail = AdminThumbnail(image_field='thumb', original_image='image')

    list_display = (..., 'admin_thumbnail', ...)

admin.site.register(ModelTest, ModelTestAdmin)


```
