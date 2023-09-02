from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    page_query_param = 'page'
    page_size = 7

class ChategoryPaginator(PageNumberPagination):
    page_query_param = 'page'
    page_size = 3