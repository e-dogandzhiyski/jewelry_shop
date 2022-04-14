# from jewelry_shop.shop.views import InternalErrorView
#
#
# def handle_exception(get_response):
#     def middleware(request):
#         response = get_response(request)
#         if response.status_code == 404:
#             return InternalErrorView.as_view()(request)
#             # return internal_error(request)
#
#         return response
#
#     return middleware