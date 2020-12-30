from django.http import JsonResponse

'''
    `ViewDoesNotExist` => 404
    `PermissionDenied` => 403
    `SuspiciousOperation` => 400
'''

def bad_request(message='Bad Request'):
    if 'application/json' in request.META.get('HTTP_ACCEPT')  and \
        not 'text/html' in request.META.get('HTTP_ACCEPT'):
        response = JsonResponse({'error': 'bad request', 'message': message})
        response.status_code = 400
        return response
    return render_template('400.html'), 400


def unauthorized(message='Must login/bad request!'):
    if 'application/json' in request.META.get('HTTP_ACCEPT')  and \
        not 'text/html' in request.META.get('HTTP_ACCEPT'):
        response = JsonResponse({'error': 'unauthorized', 'message': message})
        response.status_code = 401
        return response
    return render_template('401.html'), 401


def forbidden(message='This is Forbidden'):
    if 'application/json' in request.META.get('HTTP_ACCEPT')  and \
        not 'text/html' in request.META.get('HTTP_ACCEPT'):
        response = JsonResponse({'error': 'forbidden', 'message': message})
        response.status_code = 403
        return response
    return render_template('403.html'), 403


def page_not_found(e='Resource Not Found'):
    if 'application/json' in request.META.get('HTTP_ACCEPT')  and \
        not 'text/html' in request.META.get('HTTP_ACCEPT'):
        response = JsonResponse({'error': 'not found', 'message': message})
        response.status_code = 404
        return response
    return render_template('404.html'), 404


def internal_server_error(e):
    if 'application/json' in request.META.get('HTTP_ACCEPT')  and \
        not 'text/html' in request.META.get('HTTP_ACCEPT'):
        response = JsonResponse({'error': 'internal server error', 'message': message})
        response.status_code = 500
        return response
    return render_template('500.html'), 500
