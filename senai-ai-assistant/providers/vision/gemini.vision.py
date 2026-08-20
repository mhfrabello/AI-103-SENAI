#providers/vision/gemini_vision.py
import google.generativeai as genai
from services.settings_service import load_settings
settings = load_settings()

genai.configure(api_key = settings["GEMINI_API_KEY"])

model = genai.GenerativeModel(settings["GEMINI_LLM_MODEL"])

def describe_image(
        image_bytes,
        prompt=None):

    if not prompt:

        prompt = """
        Descreva detalhadamente a imagem.
        """

        response = model.generate_content(
            [
                prompt,
                {
                    "mime_type": "image/jpeg",
                    "data": image_bytes

                }
            ]
        )

        return response.text