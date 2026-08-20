#services/vision_service.py
from services.settings_service import (load_settings)

def describe_image(
        image_bytes,
        prompt=None):
    settings = load_settings()
    provider = settings["VISION_PROVIDER"]

    if provider == "gemini":
        from providers.vision.gemini_vision \
            import describe_image

    elif provider == "azure":
        from providers.vision.azure.vision \
            import describe_image

    elif provider == "ollama":
        from providers.vision.ollama_vision \
            import describe_image

    return describe_image(
        image_bytes,
        prompt
    )
