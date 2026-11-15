from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    if any(item in ingredients.casefold() for item in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
