from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from lab_utils.clients import ask_claude, ask_local, ask_gpt

train_x = [
    "great product, loved it", "terrible, broke in a day", "works perfectly",
    "waste of money", "absolutely fantastic quality", "awful experience",
    "very happy with this", "do not buy, disappointing",
]

train_y = [1, 0, 1, 0, 1, 0, 1, 0]

test_x =  [
    "not bad at all",              # negation trick
    "I expected more, honestly",   # implicit negative
    "This slaps",                  # slang positive
    "Perfectly adequate. Meh.",    # mixed
]

vec = TfidfVectorizer()
X = vec.fit_transform(train_x)

# print(X.toarray())

# Classical ML
lr = LogisticRegression().fit(X, train_y)
# small neural net (a tiny deep model)
mlp = MLPClassifier(hidden_layer_sizes=(16,16), max_iter = 2000, random_state=0).fit(X, train_y)

for t in test_x:
    xv = vec.transform([t])
    llm, _, _ = ask_local(
        f"Classify the sentiment of this review as POSITIVE or NEGATIVE. " + 
        f"Reply with one word.\n Review: {t}"
    ), None, None
    print(f"{t!r:35} LR={lr.predict(xv)[0]} MLP={mlp.predict(xv)[0]} LLM={llm[0].strip()}")

for t in test_x:
    xv = vec.transform([t])
    print(repr(t),
          "knwoen words:", xv.nnz,
          "LR probabilites:" , lr.predict_proba(xv).round(3),
          "MLP probabilites:" , mlp.predict_proba(xv).round(3))
          
