#  Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai

os.environ["OPENAI_API_KEY"] = '1aea88b604d644ba97fb78a32fcbaa1d'
# OPENAI_API_KEY="1aea88b604d644ba97fb78a32fcbaa1d"
openai.api_type = "azure"
openai.api_base = "https://santengptpoc2023-wouter.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = "IT部门如何帮助销售提高工作效率?列举3点"

response = openai.Completion.create(engine="BonziGPT35",
                                    prompt=prompt,
                                    temperature=1,
                                    max_tokens=600,
                                    top_p=1,
                                    frequency_penalty=0,
                                    presence_penalty=0,
                                    stop=None)

message = response.choices[0].content
print(message)
