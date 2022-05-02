from rest_framework.pagination import PageNumberPagination


class MoviesPagination(PageNumberPagination):
    # Default elements per page
    page_size = 10
    # Implement managing number of elements per page; Max = 100
    page_size_query_param = 'size'
    max_page_size = 100
