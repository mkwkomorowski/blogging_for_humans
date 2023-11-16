"""
blogging_for_humans Django application initialization.
"""

import logging
from django.apps import AppConfig
from edx_django_utils.plugins import PluginURLs, PluginSettings
from openedx.core.djangoapps.plugins.constants import ProjectType, SettingsType


log = logging.getLogger(__name__)


class BloggingForHumansConfig(AppConfig):
    name = "blogging_for_humans"
    label = "blogging_for_humans"
    verbose_name = "My Open edX Plugin"

    # See: https://edx.readthedocs.io/projects/edx-django-utils/en/latest/edx_django_utils.plugins.html
    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: name,
                PluginURLs.REGEX: "^blogging_for_humans/",
                PluginURLs.RELATIVE_PATH: "urls",
            }
        },
        PluginSettings.CONFIG: {
            ProjectType.LMS: {
                SettingsType.PRODUCTION: {PluginSettings.RELATIVE_PATH: "settings.production"},
                SettingsType.COMMON: {PluginSettings.RELATIVE_PATH: "settings.common"},
                SettingsType.DEVSTACK: {PluginSettings.RELATIVE_PATH: "settings.devstack"},
            }
        },
    }
    
    def ready(self):
        log.debug("{label} is ready.".format(label=self.label))
