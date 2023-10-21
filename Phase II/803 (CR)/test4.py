''' Test 4 - ### - https://chat.openai.com/share/e476a2d0-5c29-4c5b-b5b4-7d977b469787 '''
from functools import reduce
from operator import or_, and_
from django.db.models import Q
from django.views.generic import ListView
from .models import LinnaeanDissertation

class LinnaeanDissertationAdvancedSearchView(ListView):
    model = LinnaeanDissertation
    context_object_name = "dissertation_list"
    template_name = "linnaean_dissertations/dissertation_advanced_search.html"
    ordering = ["liden_number_int", "liden_number"]

    def build_query(self, filter_type, field, query):
        filter_mapping = {
            "less_than": "__lt",
            "greater_than": "__gt",
            "contains": "__icontains",
        }
        query_modifier = filter_mapping.get(filter_type, "")
        if query_modifier:
            new_query = f"{field}{query_modifier}"
            if filter_type == "contains_any":
                query_list = query.split(" ")
                query_filter = reduce(or_, (Q(**{new_query: q}) for q in query_list))
            elif filter_type == "contains_all":
                query_list = query.split(" ")
                query_filter = reduce(and_, (Q(**{new_query: q}) for q in query_list))
            elif filter_type == "contains_not":
                query_filter = ~Q(**{new_query: query})
            else:
                query_filter = Q(**{new_query: query})
            return query_filter
        return Q()

    def get_queryset(self):
        query = Q()
        filter_params = [
            ("liden_number", "liden_number_filter", "liden_number_int"),
            ("respondent", "respondent_filter", "respondent_full"),
            ("title", "title_filter", "title"),
            ("real_date", "real_date_filter", "real_date"),
        ]
        for param, filter_param, field in filter_params:
            value = self.request.GET.get(param)
            if value:
                filter_type = self.request.GET.get(filter_param)
                query &= self.build_query(filter_type, field, value)
        return LinnaeanDissertation.objects.filter(query).order_by(*self.ordering)
