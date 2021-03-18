from django.http import JsonResponse


def alunos(request):
    if request.method == 'GET':
        return JsonResponse({
            'id': 1,
            'nome': 'Beck'
        })
