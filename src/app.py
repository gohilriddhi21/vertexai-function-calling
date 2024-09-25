import vertexai
from vertexai.generative_models import GenerativeModel
model = GenerativeModel("gemini-1.5-pro-001")

response = model.generate_content(
    "What's the exchange rate for euros to dollars today?"
)
print(response.text)