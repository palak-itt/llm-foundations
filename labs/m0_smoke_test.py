from lab_utils.clients import ask_claude, ask_local, ask_gpt
import time


q = "Can you explain a relevant software engineer who is FAANG level?"

# text, usage, dt = ask_claude(q)
# print("Claude response:", text)
# print("Usage:", usage)
# print("Latency (s):", dt)

# # M0 Tests
# start = time.time()
# text, usage, dt = ask_gpt(q)
# print("GPT response:", text)
# print("Usage:", usage)
# print("Latency (s):", dt)

# text, usage, dt = ask_local(q)
# print("Local model response:", text)
# print("Usage:", usage)
# print("Latency (s):", dt)
# end = time.time() - start
# print("Total Latency (s):", end)    

# FROM M1 Tests
q1 = "How many r's are in 'strawberry'?"
q2 = "What is 48213 × 3917?"

start = time.time()
text, usage, dt = ask_gpt(q1)
print("GPT response:", text)
print("Usage:", usage)
print("Latency (s):", dt)

text, usage, dt = ask_gpt(q2)
print("GPT response:", text)
print("Usage:", usage)
print("Latency (s):", dt)

end = time.time() - start
print("Total Latency (s):", end)
# FROM M1 Tests
q1 = "How many r's are in 'strawberry'?"
q2 = "What is 48213 × 3917?"

start = time.time()
text, usage, dt = ask_local(q1)
print("Local model response:", text)
print("Usage:", usage)
print("Latency (s):", dt)

text, usage, dt = ask_local(q2)
print("Local model response:", text)
print("Usage:", usage)
print("Latency (s):", dt)

end = time.time() - start
print("Total Latency (s):", end)