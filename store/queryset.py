from django.db.models import QuerySet
from django.db.models import Aggregate, Sum, Count, Q
from django.db import models


class ProductQuerySet(QuerySet):
    def is_free(self):
        return self.filter(is_free=True)

    def search(self, query):
        lookups = (Q(name__icontains=query) |
                   Q(description__icontains=query) |
                   Q(category__icontains=query)
                   )
        return self.filter(lookups).distinct()
