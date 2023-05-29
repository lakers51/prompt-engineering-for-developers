import requests
import json

url = "https://santengptpoc2023-wouter.openai.azure.com/openai/deployments/bonzigpt35/chat/completions?api-version=2023-03-15-preview"
prompt = "I have 7 days vacation in June. Schdeule a plan and output by markdown  "  # "Schedule a 2 day trip in Shanghai, output by markdown"
payload = json.dumps({
    "messages": [{
        "role": "system",
        "content": "You are a helpful assistant."
    }, {
        "role": "user",
        "content": prompt
    }],
    "max_tokens":
    600,
    "n":
    1,
    "temperature":
    1
})
headers = {
    'Content-Type': 'application/json',
    'api-key': '1aea88b604d644ba97fb78a32fcbaa1d'
}
# Call Http
response = requests.request("POST", url, headers=headers, data=payload)
response_dict = response.json()
# Output
# print(response_dict)
print("id:", response_dict["id"])
print("object:", response_dict["object"])
print("created:", response_dict["created"])
print("model:", response_dict["model"])
print("usage: ", 'completion_tokens:',
      response_dict["usage"]["completion_tokens"], 'prompt_tokens:',
      response_dict["usage"]["prompt_tokens"], 'total_tokens:',
      response_dict["usage"]["total_tokens"])
print("message:\n", response_dict["choices"][0]["message"]["content"])

# if text:
#     if "\n\n" in text:
#         text_list = text.split("\n\n")
#         for item in text_list:
#             print(item)
#     else:
#         print(text)
# else:
#     print("No output")
