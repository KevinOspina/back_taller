def jwt_response_payload_handler(token, user=None, request=None):
    response = {
        'token': token,
        'user': '%s %s' % (user.first_name, user.last_name),
        'permissions': [str(p) for p in user.get_all_permissions()]
    }
    return response
