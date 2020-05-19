def jwt_response_payload_handler(token, user=None, request=None):
    response = {
        'token': token,
        'user': '%s %s' % (user.first_name, user.last_name),
        'permissions': [str(p) for p in user.get_all_permissions()]
    }
    return response


GRADE_CHOICES = (
    ("Nulo", "Nulo"),
    ("Medio", "Medio"),
    ("Significativo", "Significativo"),
    ("Alto", "Alto"),
    ("Muy Alto", "Muy Alto")
)

PRINCIPLE_CHOICES = (
    ("Orientación", "Orientación"),
    ("Elementos persuasivos", "Elementos persuasivos"),
    ("Orientación de aprendizaje", "Orientación de aprendizaje"),
    ("Recompensas basadas en logros", "Recompensas basadas en logros"),
    ("Logros adaptables", "Logros adaptables"),
    ("Factores de diversión", "Factores de diversión"),
    ("Transformador", "Transformador"),
    ("Orientado al bienestar", "Orientado al bienestar"),
    ("Genera investigación", "Genera investigación"),
    ("Basado en el conocimiento", "Basado en el conocimiento")
)

EVIDENCE_CHOICES = (
    ("Roles", "Roles"),
    ("Materiales", "Materiales"),
    ("Pasos", "Pasos"),
    ("Reglas", "Reglas"),
    ("Objetivos", "Objetivos"),
)
