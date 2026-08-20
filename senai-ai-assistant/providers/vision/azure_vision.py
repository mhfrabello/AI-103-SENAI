#providers/vision/azure_vision.py
from openai import AzureOpenAI
from services.settings_service import load_settings

settings = load_settings()
client = AzureOpenAI(
    api_key=settings["AZURE_KEY"],
    api_version='2024-10-21',
    azure_endpoint=settings["AZURE_PROJECT_URL"] # AZURE_OPENIA_URL
)
import base64

def describe_image(image_bytes, prompt=None):

    img_base64 = base64.b64encode(
        image_bytes
    ).decode()
    
    response = cliente.chat.completitions.create(
        model = settings["AZURE_LLM_MODEL"],
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url":
                            f"data:image/jpeg;base64, {img_base64}"
                        }
                    }
                ]

            }
        ]
    )

    return response.choices[0].message.content