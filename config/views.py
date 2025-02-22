from django.utils.translation import gettext
from django.views.generic import TemplateView


class TemplateViewWithContext(TemplateView):
    page_title = None

    def get_context_data(self, **kwargs):
        return {
            "context": {
                "page_title": gettext(self.page_title) if self.page_title else None
            }
        }


class TransactionalLicenceFormView(TemplateViewWithContext):
    template_name = "pages/transactional_licence.html"
    page_title = "transactionallicenceform.title"


class AccessibilityStatement(TemplateViewWithContext):
    template_name = "pages/accessibility_statement.html"
    page_title = "accessibilitystatement.title"


class OpenJusticeLicenceView(TemplateViewWithContext):
    template_name = "pages/open_justice_licence.html"
    page_title = "openjusticelicence.title"


class TermsOfUseView(TemplateViewWithContext):
    template_name = "pages/terms_of_use.html"
    page_title = "terms.title"


class StructuredSearchView(TemplateViewWithContext):
    template_name = "pages/structured_search.html"
    page_title = "search.title"


class NoResultsView(TemplateViewWithContext):
    template_name = "pages/no_results.html"


class CheckView(TemplateViewWithContext):
    template_name = "pages/check.html"


class WhatToExpectView(TemplateViewWithContext):
    template_name = "pages/what_to_expect.html"
