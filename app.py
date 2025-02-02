from openai import OpenAI

client = OpenAI(
base_url = "https://integrate.api.nvidia.com/v1",
api_key = "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"
)

completion = client.chat.completions.create(
model="nvidia/llama-3.1-nemotron-70b-instruct",
messages=[{"role":"user","content":"Provide me a paragraph about AI"}],
temperature=0.5,
top_p=1,
max_tokens=1024,
stream=True
)

for chunk in completion:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")