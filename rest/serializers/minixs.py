class ProcessLanguageMixin(object):
    def get_current_language(self):
        if "request" in self.context:
            _request = self.context["request"]
            _lang = _request.LANGUAGE_CODE
            return _lang


class ProcessCurrentUserMixin(object):

    def get_current_user(self):
        if "request" in self.context:
            _request = self.context["request"]
            user = _request.user
            return user


class ProcessSearchKeywordMixin(object):

    def get_search_keyword(self):
        if "request" in self.context:
            _request = self.context["request"]

            return _request.GET.get("q", "bitcoin")