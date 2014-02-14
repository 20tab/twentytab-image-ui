from django.conf import settings
from django.contrib import admin
from imagekit.admin import AdminThumbnail as IKAdminThumbnail
from django.template.loader import render_to_string
from . import conf


class AdminThumbnail(IKAdminThumbnail):
    """
    A convenience utility for adding thumbnails to Django's admin change list.
    """
    def __init__(self, image_field, template=None, original_image=None):
        """
        :param image_field: The name of the ImageField or ImageSpecField on the
            model to use for the thumbnail.
        :param template: The template with which to render the thumbnail

        """
        self.image_field = image_field
        self.template = template or getattr(settings,
                                            "ADMIN_THUMBNAIL_DEFAULT_TEMPLATE",
                                            "imagekit/admin/thumbnail.html")
        self.original_image = original_image

    def __call__(self, obj):
        if callable(self.image_field):
            thumbnail = self.image_field(obj)
        else:
            try:
                thumbnail = getattr(obj, self.image_field)
            except AttributeError:
                raise Exception('The property %s is not defined on %s.' % \
                        (self.image_field, obj.__class__.__name__))

        try:
            original_image = getattr(obj, self.original_image, None)
        except:
            original_image = None
        if not original_image:
            original_image = getattr(thumbnail, 'source_file', None) or thumbnail

        template = self.template

        return render_to_string(template, {
            'model': obj,
            'thumbnail': thumbnail,
            'original_image': original_image,
        })


class ColorBoxAdmin(admin.ModelAdmin):
    """
    Abstract admin option class to add colorbox.js (jQuery plugin)
    """
    class Media:
        css = {u"all": (u"{}image_ui/colorbox/colorbox.css".format(settings.STATIC_URL),)}
        js = (settings.JQUERY_LIB,
              settings.JQUERYUI_LIB,
              u'{}image_ui/colorbox/jquery.colorbox-min.js'.format(settings.STATIC_URL),
              u'{}image_ui/js/colorbox-init.js'.format(settings.STATIC_URL))

    class Meta:
        abstract = True


class ColorBoxPositionAdmin(admin.ModelAdmin):
    """
    Abstract admin option class to add colorbox.js (jQuery plugin)
    """
    class Media:
        css = {u"all": (u"{}image_ui/colorbox/colorbox.css".format(settings.STATIC_URL),)}
        js = (settings.JQUERY_LIB,
              settings.JQUERYUI_LIB,
              u'{}image_ui/js/admin-list-reorder.js',
              u'{}image_ui/colorbox/jquery.colorbox-min.js'.format(settings.STATIC_URL),
              u'{}image_ui/js/colorbox-init.js'.format(settings.STATIC_URL))

    class Meta:
        abstract = True
