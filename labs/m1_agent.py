import ollama
from lab_utils.clients import OLLAMA_MODEL
import os
import openai
import json
def calculator(expression: str) -> str:
    allowed = set("0123456789+-*/(). ")
    if not set(expression) <= allowed:
        raise "error: invalid characters"
    try:
        return str(eval(expression, {"__builtins__": {}}, {}))
    except Exception as e:
        raise ValueError(f"error: {e}")

def get_word_length(word: str) -> int:
    return str(len(word))
    # return str(word.count('r'))

TOOLS = {"calculator": calculator, 'get_word_length': get_word_length}

tools_specs = [{
    "type": "function",
    "function": {
        "name": "calculator",
        "description": "Evaluate an arithmetic expression.",
        "parameters": {
            "type": "object",
            "properties": {"expression" : {"type": "string"}},
            "required": ["expression"],
        },
    }
}]
tools_specs.append({
    "type": "function",
    "function": {
        "name": "get_word_length",
        "description": "Get the length of a word.",
        "parameters": {
            "type": "object",
            "properties": {"word": {"type": "string"}},
            "required": ["word"],
        },
    },
})

# messages = [{"role": "user", "content": "What is 48213*3917 and divide the result by 7. Also how many 'r' in 'strarwberrries'"}]
messages = [{"role": "user", "content": "How to reach to america from india?'"}]

for step in range(5):
    resp = ollama.chat(model=OLLAMA_MODEL, messages=messages, tools = tools_specs)
    msg = resp.message
    messages.append(msg)
    print(messages)

    if not msg.tool_calls:
        print("FINAL: ", msg.content)
        break

    for call in msg.tool_calls:
        name = call.function.name
        args = call.function.arguments
        print()
        print(f"[step {step}] model called {name} ({args})")
        result = TOOLS[name](**args)
        print()
        print(result)
        print()
        messages.append({"role": "tool", "name":name, "content": result})

# GPT_MODEL = os.getenv("OPENAI_MODEL", "gpt-6-luna")
# client= openai.OpenAI()
# for step in range(5):
#     resp = client.chat.completions.create(model=GPT_MODEL, messages=messages, tools = tools_specs, reasoning_effort='none')
#     print(resp)
#     msg = resp.choices[0].message
#     messages.append(msg)
#     print(messages)

#     if not msg.tool_calls:
#         print("FINAL: ", msg.content)
#         break

#     for call in msg.tool_calls:
#         name = call.function.name
#         args = json.loads(call.function.arguments)
#         print()
#         print(f"[step {step}] model called {name} ({args})")
#         result = TOOLS[name](**args)
#         print()
#         print(result)
#         print()
#         messages.append({"role": "tool", "tool_call_id": call.id, "content": result})

   
