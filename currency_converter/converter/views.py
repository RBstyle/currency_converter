from rest_framework.decorators import api_view
from rest_framework.response import Response

from converter.utils import converter


@api_view(["GET"])
def rates(request):
    if request.method == "GET":
        from_input = request.query_params.get("from")
        to_input = request.query_params.get("to")
        value_input = request.query_params.get("value")

        result = converter(from_input, to_input, value_input)

        return Response(result)
