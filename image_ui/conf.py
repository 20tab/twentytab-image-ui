from appconf import AppConf
from django.conf import settings


class ImageUIConf(AppConf):
    ADMIN_THUMBNAIL_DEFAULT_TEMPLATE = u"admin/default_thumbnail.html"
    STATIC_URL = u'/static/'
    JQUERY_LIB = u"{}{}".format(
        getattr(settings, u'STATIC_URL', u'/static/'),
        u"image_ui/js/jquery-2.1.0.min.js"
    )
    JQUERYUI_LIB = u"{}{}".format(
        getattr(settings, u'STATIC_URL', u'/static/'),
        u"image_ui/js/jquery-ui-1.10.4.custom.min.js"
    )

    def configure_admin_thumbnail_default_template(self, value):
        if not getattr(settings, 'ADMIN_THUMBNAIL_DEFAULT_TEMPLATE', None):
            self._meta.holder.ADMIN_THUMBNAIL_DEFAULT_TEMPLATE = value
            return value
        return getattr(settings, 'ADMIN_THUMBNAIL_DEFAULT_TEMPLATE')

    def configure_static_url(self, value):
        if not getattr(settings, 'STATIC_URL', None):
            self._meta.holder.STATIC_URL = value
            return value
        return getattr(settings, 'STATIC_URL')

    def configure_jquery_lib(self, value):
        if not getattr(settings, 'JQUERY_LIB', None):
            self._meta.holder.JQUERY_LIB = value
            return value
        return getattr(settings, 'JQUERY_LIB')

    def configure_jqueryui_lib(self, value):
        if not getattr(settings, 'JQUERYUI_LIB', None):
            self._meta.holder.JQUERYUI_LIB = value
            return value
        return getattr(settings, 'JQUERYUI_LIB')