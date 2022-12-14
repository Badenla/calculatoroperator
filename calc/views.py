from rest_framework.decorators import api_view
from django.http import JsonResponse


@api_view(['POST'])
def operate(request):
    invalid = None
    operations = ['addition', 'subtraction', 'multiplication']
    operation_act = request.data["operation_type"]
    x = request.data["x"]
    y = request.data["y"]

    if operation_act not in operations:
        invalid = 'Use: <addition | subtraction | multiplication>'
    if type(x) is not int:
        invalid = 'x must be an integer'
    if type(y) is not int:
        invalid = 'y must be an integer'

    if invalid:
        return JsonResponse({'msg': invalid}, status=400)

    if operation_act == 'addition':
        result = x + y
    elif operation_act == 'subtraction':
        result = x + y
    else:
        result = x * y
    return JsonResponse({
        'slackUsername': 'Ayoleyi',
        'result': result,
        'operation_type': operation_act,
    }, status=200)