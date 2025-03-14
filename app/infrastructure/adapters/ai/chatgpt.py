import contextlib
import json
import logging
from collections.abc import Iterator
from dataclasses import dataclass
from urllib.parse import urljoin

import requests

from config import settings
from domain.ports.ai import AIIntegrationPort
from infrastructure.exceptions.chatgpt import ChatGPTServiceFetchingError

logger = logging.getLogger(__name__)


@dataclass
class ChatGPTIntegrationAPIAdapter(AIIntegrationPort):
    def _handle_error(self, error_message: str, response: requests.Response = None):
        if response:
            error_message += f" - Response: {response.text}"
        logger.error(error_message)
        raise ChatGPTServiceFetchingError()

    @contextlib.contextmanager
    def _request(self, method: str, route: str, **kwargs) -> Iterator[requests.Response]:
        url = urljoin(settings.CHATGPT_API_URL, route)
        headers = kwargs.pop("headers", {})

        headers["Authorization"] = f"Bearer {settings.CHATGPT_API_KEY}"
        headers.setdefault("Content-Type", "application/json")
        try:
            response = requests.request(method, url, headers=headers, **kwargs)
            response.raise_for_status()
            yield response
        except requests.Timeout:
            self._handle_error("Request timed out")
        except requests.HTTPError as http_err:
            status_code = response.status_code if response else "Unknown"
            self._handle_error(f"HTTP error {status_code}: {http_err}", response)
        except json.JSONDecodeError:
            self._handle_error("Failed to decode JSON response", response)
        except requests.RequestException as req_err:
            self._handle_error(f"Request error occurred: {req_err}")
        except Exception as e:
            self._handle_error(f"Unexpected error: {e!r}")

    def generate_text(self, prompt: str) -> dict:
        payload = {
            "model": settings.CHATGPT_MODEL,
            "temperature": 0,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are an AI assistant that extracts structured information from emails "
                        "and responds with a JSON object. Extract the customer's name, phone number, "
                        "location, service requested, and order details."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Extract the information from the following email:\n\n{prompt}\n\n"
                        "Respond ONLY with a JSON object formatted like this:\n"
                        "{\n"
                        '  "customer_name": "...",\n'
                        '  "phone": "...",\n'
                        '  "location": "...",\n'
                        '  "service_requested": "...",\n'
                        '  "order_details": "..." \n'
                        "}\n\n"
                        'If you cannot find a field, set it to an empty string (`""`). '
                        "Do not include any extra text or explanations, return ONLY the JSON object."
                    ),
                },
            ],
        }
        with self._request("POST", "chat/completions", json=payload) as response:
            result = response.json()
        result = json.loads(result["choices"][0]["message"]["content"])
        return result
