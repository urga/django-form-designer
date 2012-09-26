from form_designer.contrib.cms_plugins.form_designer_form.models import CMSFormDefinition
from form_designer.exceptions import HttpRedirectException
from form_designer.views import process_form
from form_designer import settings

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.conf import settings as django_settings
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _


class FormDesignerPlugin(CMSPluginBase):
    model = CMSFormDefinition
    module = _('Form Designer')
    name = _('Form')
    admin_preview = False

    def render(self, context, instance, placeholder):
        if instance.form_definition.form_template_name:
            self.render_template = instance.form_definition.form_template_name
        else:
            self.render_template = settings.DEFAULT_FORM_TEMPLATE

        disable_redirection = 'form_designer.middleware.RedirectMiddleware' not in django_settings.MIDDLEWARE_CLASSES
        response = process_form(context['request'], instance.form_definition, context, disable_redirection=disable_redirection)
        if isinstance(response, HttpResponseRedirect):
            raise HttpRedirectException(response, "Redirect")
        return response



plugin_pool.register_plugin(FormDesignerPlugin)
