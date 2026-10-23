from lab_utils.clients import ask_claude, ask_local, ask_gpt
import time


q = "Can you explain a relevant software engineer who is FAANG level?"

# text, usage, dt = ask_claude(q)
# print("Claude response:", text)
# print("Usage:", usage)
# print("Latency (s):", dt)

start = time.time()
text, usage, dt = ask_gpt(q)
print("GPT response:", text)
print("Usage:", usage)
print("Latency (s):", dt)

text, usage, dt = ask_local(q)
print("Local model response:", text)
print("Usage:", usage)
print("Latency (s):", dt)
end = time.time() - start
print("Total Latency (s):", end)    