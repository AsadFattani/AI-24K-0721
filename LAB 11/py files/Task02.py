# Task 2: Email Spam Classification
# Reference: Lab_10_supervised_learning.ipynb

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import random

# 1. Generate synthetic email dataset
def generate_email_dataset(n_samples=1000, random_state=42):
	random.seed(random_state)
	np.random.seed(random_state)
	spam_words = ["free", "win", "winner", "cash", "prize", "urgent", "offer", "buy", "cheap", "click"]
	ham_words = ["meeting", "project", "schedule", "report", "update", "team", "regards", "attached", "review", "thanks"]
	data = []
	for _ in range(n_samples):
		is_spam = np.random.binomial(1, 0.4)  # 40% spam
		n_words = np.random.randint(5, 30)
		if is_spam:
			words = np.random.choice(spam_words, size=np.random.randint(2, 6)).tolist()
			words += np.random.choice(ham_words, size=n_words - len(words)).tolist()
			random.shuffle(words)
			text = " ".join(words)
			hyperlinks = np.random.binomial(1, 0.7)  # 70% of spam have hyperlinks
			sender = random.choice(["promo@spam.com", "lottery@win.com", "offers@cheap.com", "unknown@random.com"])
		else:
			words = np.random.choice(ham_words, size=n_words).tolist()
			text = " ".join(words)
			hyperlinks = np.random.binomial(1, 0.1)  # 10% of ham have hyperlinks
			sender = random.choice(["boss@company.com", "colleague@work.com", "hr@company.com", "friend@email.com"])
		data.append({
			"email_text": text,
			"length": len(text),
			"hyperlinks": hyperlinks,
			"sender": sender,
			"spam": is_spam
		})
	return pd.DataFrame(data)

# 2. Preprocess dataset
def preprocess(df):
	# Convert sender to categorical feature
	df = df.copy()
	df["sender"] = df["sender"].astype("category")
	sender_dummies = pd.get_dummies(df["sender"], prefix="sender")
	# Convert text to TF-IDF features
	tfidf = TfidfVectorizer(max_features=50)
	X_text = tfidf.fit_transform(df["email_text"]).toarray()
	X = np.concatenate([
		X_text,
		df[["length", "hyperlinks"]].values,
		sender_dummies.values
	], axis=1)
	y = df["spam"].values
	return X, y, tfidf

# 3. Train/test split
df = generate_email_dataset(n_samples=1000)
X, y, tfidf = preprocess(df)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# 5. Evaluate model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# 6. Deploy: classify new emails
def classify_new_email(email_text, length, hyperlinks, sender, tfidf, model, sender_categories):
	# Prepare sender dummies
	sender_vec = np.zeros(len(sender_categories))
	if sender in sender_categories:
		sender_vec[sender_categories.index(sender)] = 1
	# Prepare text features
	X_text = tfidf.transform([email_text]).toarray()[0]
	features = np.concatenate([
		X_text,
		[length, hyperlinks],
		sender_vec
	]).reshape(1, -1)
	pred = model.predict(features)[0]
	return pred

# Example usage:
sender_categories = list(pd.get_dummies(df["sender"], prefix="sender").columns)
new_email = {
	"email_text": "free cash offer click urgent winner",  # spammy
	"length": 35,
	"hyperlinks": 1,
	"sender": "promo@spam.com"
}
result = classify_new_email(
	new_email["email_text"],
	new_email["length"],
	new_email["hyperlinks"],
	new_email["sender"],
	tfidf,
	model,
	sender_categories
)
print("New email classified as:", "Spam" if result == 1 else "Not Spam")
