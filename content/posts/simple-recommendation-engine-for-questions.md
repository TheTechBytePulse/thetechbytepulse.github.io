+++
title = "🔍 How to Build a Simple Question Recommendation Engine from Articles and Videos"
date = "2026-07-17T16:00:00Z"
draft = false
author = "Prateep Gedupudi"
tags = ["AI", "NLP", "Recommendation Engine", "Python", "Machine Learning", "Developer Tools", "Tutorial"]
series = ["AI Series"]
categories = ["AI & Software"]
description = "Learn how to build a simple recommendation engine that suggests relevant questions from a corpus of articles or videos — no PhD required. A beginner-friendly guide using Python and sentence embeddings."

[cover]
  image = "/images/simple-recommendation-engine-for-questions-cover.jpeg"
  alt = "A recommendation engine matching questions to articles and videos"
  caption = "Finding the right question from a sea of content."
+++

**Ever watched a YouTube video or read an article and thought — "what are the key questions I should be asking about this topic?" Or maybe you have a large collection of content and want to automatically surface the most relevant questions for any given input. That's exactly what a recommendation engine for questions does. And it's simpler to build than you think.**

This guide walks through the concept and a working Python implementation — no machine learning background required.

### 🧩 The Core Idea

The basic concept is straightforward:

1. You have a **corpus** — a collection of articles, video transcripts, or documents.
2. You have a set of **questions** — either pre-written or extracted from the corpus.
3. When a user provides an input (a topic, a sentence, or another question), the engine finds and returns the **most relevant questions** from the corpus.

The magic that makes this work is called **semantic similarity** — measuring how close two pieces of text are in *meaning*, not just in exact words.

For example, "How does solar energy work?" and "What is the process behind photovoltaic cells?" are very different sentences but mean almost the same thing. A good recommendation engine understands that.

### 🔑 Key Concept: Embeddings

To measure semantic similarity, we convert text into **embeddings** — lists of numbers (vectors) that represent the meaning of a sentence in a mathematical space. Sentences with similar meanings end up with similar vectors.

Think of it like a map. Cities that are close to each other on a map are geographically similar. Sentences that are close to each other in vector space are semantically similar.

We'll use a pre-trained model from the `sentence-transformers` library to generate these embeddings. It does all the heavy lifting for us.

### 🛠️ What You'll Need

Install the required libraries:

```bash
pip install sentence-transformers scikit-learn
```

That's it. No GPU, no cloud service, no API key.

### 📚 Step 1: Prepare Your Corpus

Your corpus can be articles, blog posts, or video transcripts. For this example, let's use a small set of tech-related questions extracted from a few articles:

```python
corpus_questions = [
    "What is artificial intelligence?",
    "How does machine learning differ from deep learning?",
    "What are the benefits of solar energy?",
    "How do you install Ollama on a MacBook?",
    "What is vibe-coding and how does it work?",
    "How do AI agents plan and execute tasks?",
    "What is the difference between on-grid and off-grid solar?",
    "How does Gemma 4 run on low-memory devices?",
    "What programming languages are best for AI development?",
    "How does semantic search work?",
]
```

In a real system, you'd extract these questions automatically from your content — more on that at the end.

### 🔢 Step 2: Generate Embeddings

Now convert all the corpus questions into vectors:

```python
from sentence_transformers import SentenceTransformer

# Load a lightweight pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings for all corpus questions
corpus_embeddings = model.encode(corpus_questions)
```

The model `all-MiniLM-L6-v2` is small, fast, and works well for most use cases. It runs entirely on your local machine.

### 🔍 Step 3: Find the Most Relevant Questions

When a user types a query, encode it the same way and find the closest matches using **cosine similarity** — a measure of how similar two vectors are:

```python
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def recommend_questions(user_query, top_n=3):
    # Encode the user's input
    query_embedding = model.encode([user_query])

    # Calculate similarity between query and all corpus questions
    similarities = cosine_similarity(query_embedding, corpus_embeddings)[0]

    # Get the top N most similar questions
    top_indices = np.argsort(similarities)[::-1][:top_n]

    print(f"\nTop {top_n} recommended questions for: '{user_query}'\n")
    for i, idx in enumerate(top_indices):
        print(f"{i+1}. {corpus_questions[idx]}  (score: {similarities[idx]:.2f})")
```

### ▶️ Step 4: Try It Out

```python
recommend_questions("I want to learn about AI tools for developers")
```

**Output:**
```
Top 3 recommended questions for: 'I want to learn about AI tools for developers'

1. What programming languages are best for AI development?  (score: 0.61)
2. How do AI agents plan and execute tasks?  (score: 0.58)
3. What is artificial intelligence?  (score: 0.54)
```

Try another one:

```python
recommend_questions("setting up renewable energy at home")
```

**Output:**
```
Top 3 recommended questions for: 'setting up renewable energy at home'

1. What is the difference between on-grid and off-grid solar?  (score: 0.72)
2. What are the benefits of solar energy?  (score: 0.68)
3. How does Gemma 4 run on low-memory devices?  (score: 0.21)
```

Notice how the engine correctly matched "renewable energy at home" to solar-related questions without any exact word overlap.

### 🏗️ Putting It All Together

Here's the complete script:

```python
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Your question corpus
corpus_questions = [
    "What is artificial intelligence?",
    "How does machine learning differ from deep learning?",
    "What are the benefits of solar energy?",
    "How do you install Ollama on a MacBook?",
    "What is vibe-coding and how does it work?",
    "How do AI agents plan and execute tasks?",
    "What is the difference between on-grid and off-grid solar?",
    "How does Gemma 4 run on low-memory devices?",
    "What programming languages are best for AI development?",
    "How does semantic search work?",
]

# Load model and encode corpus
model = SentenceTransformer('all-MiniLM-L6-v2')
corpus_embeddings = model.encode(corpus_questions)

def recommend_questions(user_query, top_n=3):
    query_embedding = model.encode([user_query])
    similarities = cosine_similarity(query_embedding, corpus_embeddings)[0]
    top_indices = np.argsort(similarities)[::-1][:top_n]

    print(f"\nTop {top_n} recommended questions for: '{user_query}'\n")
    for i, idx in enumerate(top_indices):
        print(f"{i+1}. {corpus_questions[idx]}  (score: {similarities[idx]:.2f})")

# Test it
recommend_questions("I want to learn about AI tools for developers")
recommend_questions("setting up renewable energy at home")
```

### 🎬 Scaling It Up: Real Articles and Videos

For a real-world corpus, you wouldn't hand-write questions. Instead:

*   **From articles:** Use an LLM (like [Gemma 4 running locally](/posts/run-gemma4-offline-ollama-macbook/)) to auto-generate questions from each article. Prompt: *"Generate 5 key questions this article answers."*
*   **From videos:** Get the auto-generated transcript from YouTube, then feed it to an LLM to extract questions the same way.
*   **Pre-compute embeddings:** For large corpora, generate and save all embeddings to disk once (using `numpy.save`), then load them on startup instead of recomputing every time.

### 🔮 What You Can Build with This

This simple engine is the foundation for a lot of useful tools:

*   **FAQ bots** — match user questions to a database of answered questions
*   **Content discovery** — "readers who asked this also asked..."
*   **Study assistants** — given a topic, surface the most important questions to study
*   **Search improvement** — augment keyword search with semantic matching

The whole thing runs locally, costs nothing, and can be up and running in under 30 minutes. That's the power of modern open-source AI tooling — what used to require a team of ML engineers can now be built by any developer with a Python environment.
