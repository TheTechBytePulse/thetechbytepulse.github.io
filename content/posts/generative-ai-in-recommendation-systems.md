+++
title = "🎯 Applying Generative AI in Recommendation Systems"
date = "2026-07-17T20:00:00Z"
draft = false
author = "Prateep Gedupudi"
tags = ["AI", "Generative AI", "Recommendation System", "LLM", "NLP", "Machine Learning", "Python", "Developer Tools"]
series = ["AI Series"]
categories = ["AI & Software"]
description = "Traditional recommendation systems match patterns. Generative AI understands context, intent, and nuance. Here's how to combine both to build smarter, more personalised recommendations."

[cover]
  image = "/images/generative-ai-in-recommendation-systems-cover.jpeg"
  alt = "Generative AI powering a recommendation engine"
  caption = "From pattern matching to understanding — the next generation of recommendations."
+++

**Netflix knows what you want to watch next. Spotify knows your mood before you do. Amazon surfaces the exact product you were thinking about. These are classic recommendation systems — and they work well. But they have a fundamental limitation: they match patterns from the past. They don't understand *why* you want something. Generative AI changes that.**

This article explores how generative AI upgrades traditional recommendation systems — and walks through practical implementation patterns you can apply today.

### 🔍 What's Wrong with Traditional Recommendations?

Classic recommendation systems fall into two camps:

*   **Collaborative filtering** — "People like you also liked X." It looks at what similar users did and assumes you'll behave the same way.
*   **Content-based filtering** — "You liked this, so here's something similar." It matches item features to your past preferences.

Both approaches work, but they share a core weakness: they are **backward-looking**. They rely entirely on historical behaviour. They struggle with:

*   **Cold start** — new users with no history get generic recommendations
*   **Context blindness** — they don't know if you're shopping for yourself or as a gift
*   **Intent gaps** — "I want something calming to read on a Sunday afternoon" is not a query a traditional system can handle
*   **Explanation** — they can tell you *what* to read, not *why* it's right for you

This is exactly where generative AI steps in.

### 🧠 What Generative AI Adds

A large language model doesn't just match patterns — it **reasons about meaning**. It can:

*   Understand natural language queries ("something like Inception but more grounded")
*   Explain recommendations in human terms ("Based on your interest in local AI tools, you might enjoy...")
*   Generate personalised summaries of why an item fits a user
*   Handle zero-shot cases — making reasonable recommendations even with no user history
*   Combine structured data (ratings, categories) with unstructured context (reviews, descriptions, user notes)

The result is a system that feels less like a filter and more like a knowledgeable friend.

### 🏗️ The Architecture: Two Patterns

There are two main ways to integrate generative AI into a recommendation pipeline.

**Pattern 1: LLM as the Ranker**

The traditional system generates a candidate pool, and the LLM re-ranks them based on deeper context.

```
User Query
    ↓
Traditional Retrieval (fast, broad) → 50 candidates
    ↓
LLM Re-ranking (slow, precise) → Top 5 with explanations
    ↓
User
```

This is the most practical pattern. The retrieval step handles scale; the LLM handles nuance.

**Pattern 2: LLM as the Query Expander**

The LLM enriches a vague user query before it hits the retrieval system.

```
User: "something relaxing for the weekend"
    ↓
LLM expands → "calm, low-stakes, light fiction, nature themes, short chapters"
    ↓
Semantic Search against content corpus
    ↓
Ranked results
```

Both patterns can be combined for even better results.

### 🛠️ Building It: Step by Step

Let's build a simple generative AI-powered book recommendation system using Python. We'll use sentence embeddings for retrieval and an LLM for re-ranking and explanation.

**Install dependencies:**

```bash
pip install sentence-transformers openai scikit-learn numpy
```

**Step 1: Set up your content corpus**

```python
# A small book corpus — in production this would be thousands of items
books = [
    {"id": 1, "title": "Atomic Habits", "description": "A practical guide to building good habits and breaking bad ones through small, consistent changes."},
    {"id": 2, "title": "The Hitchhiker's Guide to the Galaxy", "description": "A comedic science fiction adventure about the end of the Earth and one man's journey across the universe."},
    {"id": 3, "title": "Deep Work", "description": "How to focus without distraction on cognitively demanding tasks to produce high-quality work."},
    {"id": 4, "title": "Project Hail Mary", "description": "A lone astronaut wakes up with no memory and must save Earth from an extinction-level threat."},
    {"id": 5, "title": "The Pragmatic Programmer", "description": "Timeless advice and best practices for software developers to write better, more maintainable code."},
    {"id": 6, "title": "Sapiens", "description": "A sweeping history of humankind, from early humans to the modern age, examining how Homo sapiens came to dominate the planet."},
    {"id": 7, "title": "Thinking, Fast and Slow", "description": "An exploration of the two systems of thought that drive human decisions — intuition and deliberate reasoning."},
    {"id": 8, "title": "The Martian", "description": "An astronaut stranded on Mars must use his ingenuity and science skills to survive until rescue arrives."},
]
```

**Step 2: Build the semantic retrieval layer**

```python
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

# Pre-compute embeddings for all books
corpus_texts = [f"{b['title']}. {b['description']}" for b in books]
corpus_embeddings = model.encode(corpus_texts)

def retrieve_candidates(query, top_n=5):
    """Fast semantic retrieval — returns top N candidates."""
    query_embedding = model.encode([query])
    scores = cosine_similarity(query_embedding, corpus_embeddings)[0]
    top_indices = np.argsort(scores)[::-1][:top_n]
    return [(books[i], float(scores[i])) for i in top_indices]
```

**Step 3: LLM re-ranking and explanation**

```python
import openai
import json

client = openai.OpenAI(api_key="your-api-key")

def rerank_and_explain(user_query, candidates, user_context=""):
    """Use an LLM to re-rank candidates and generate personalised explanations."""

    candidate_list = "\n".join([
        f"{i+1}. {c['title']}: {c['description']}"
        for i, (c, _) in enumerate(candidates)
    ])

    prompt = f"""You are a personalised book recommendation assistant.

User request: "{user_query}"
{f'Additional context about the user: {user_context}' if user_context else ''}

Here are candidate books retrieved by a search system:
{candidate_list}

Task:
1. Re-rank these books from most to least relevant for this specific user request.
2. For the top 3, write a one-sentence personalised explanation of why it fits.
3. Return a JSON array with fields: title, rank, explanation.

Return only valid JSON, no other text."""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    try:
        return json.loads(response.choices[0].message.content)
    except json.JSONDecodeError:
        return []
```

**Step 4: The LLM query expander**

```python
def expand_query(vague_query):
    """Turn a vague user request into a rich search query."""
    prompt = f"""A user is looking for a book recommendation and said: "{vague_query}"

Expand this into a detailed search description (2-3 sentences) that captures the likely intent, mood, themes, and type of content they want. Be specific. Return only the expanded description, no other text."""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content.strip()
```

**Step 5: Wire it all together**

```python
def recommend(user_query, user_context="", expand=True):
    print(f"\n📚 Finding recommendations for: '{user_query}'\n")

    # Optionally expand vague queries
    search_query = expand_query(user_query) if expand else user_query
    if expand:
        print(f"🔍 Expanded query: {search_query}\n")

    # Retrieve candidates semantically
    candidates = retrieve_candidates(search_query, top_n=5)

    # Re-rank and explain with LLM
    results = rerank_and_explain(user_query, candidates, user_context)

    print("🎯 Top Recommendations:\n")
    for item in results:
        print(f"{item['rank']}. {item['title']}")
        print(f"   → {item['explanation']}\n")

# Try it out
recommend(
    "something to help me think more clearly and make better decisions",
    user_context="software developer, reads mostly non-fiction"
)
```

**Sample output:**
```
📚 Finding recommendations for: 'something to help me think more clearly...'

🔍 Expanded query: The user wants a non-fiction book about improving
cognitive clarity, decision-making frameworks, and rational thinking...

🎯 Top Recommendations:

1. Thinking, Fast and Slow
   → Directly addresses how your two thinking systems influence decisions,
     essential reading for anyone wanting to reason more deliberately.

2. Deep Work
   → Teaches you to eliminate cognitive noise and focus deeply, a practical
     complement to understanding how good thinking actually happens.

3. Atomic Habits
   → Building systematic habits around how you think and work compounds
     over time into dramatically better decision-making.
```

### ⚡ Using a Local LLM Instead

Don't want to pay for API calls? Swap the OpenAI client for [Ollama running Gemma 4 locally](/posts/run-gemma4-offline-ollama-macbook/). The only change needed:

```python
client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # required but unused by Ollama
)
# Then use model="gemma4" in your completions calls
```

Complete privacy, zero API cost, same results.

### 🔮 Where This Is Already Happening

This isn't theoretical — generative AI is actively reshaping recommendations in production:

*   **Spotify** uses LLMs to understand the mood and context behind listening sessions, not just track history
*   **Amazon** generates personalised product descriptions based on what it knows about your purchase intent
*   **Netflix** is experimenting with LLM-generated synopses tuned to individual taste profiles
*   **GitHub Copilot** is essentially a recommendation engine for code — suggesting the most contextually relevant completion based on everything in your file

### 🧩 Key Takeaways

The shift from traditional to generative AI recommendations isn't about replacing what works — it's about adding a layer of **understanding** on top of retrieval. The practical stack looks like this:

| Layer | Technology | Role |
|---|---|---|
| Retrieval | Sentence embeddings + cosine similarity | Fast, scalable candidate generation |
| Understanding | LLM (GPT-4o, Gemma, Llama) | Query expansion, re-ranking, explanation |
| Personalisation | User context in the prompt | Tailoring results to the individual |

Start with the retrieval layer — it's fast and free. Add the LLM layer when you need nuance. The combination is more powerful than either alone, and as the earlier article on [building a question recommendation engine](/posts/simple-recommendation-engine-for-questions/) showed, the retrieval foundation is something you can set up in an afternoon.
