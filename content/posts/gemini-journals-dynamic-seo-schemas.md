+++
title = "Gemini Journals: That Time I Taught My AI Assistant a New Trick"
date = "2025-08-07T18:30:00Z"
draft = false
tags = ["Hugo", "SEO", "Schema.org", "Gemini", "AI Collaboration", "Developer Story"]
series = ["Gemini Journals"]
categories = ["AI & Software", "Gemini Journals"]
description = "My journey from a one-size-fits-all SEO strategy to a dynamic, intelligent schema system on my Hugo blog, all thanks to a little nudge in the right direction with my AI partner, Gemini."
author = "Prateep Gedupudi"

[cover]
  image = "/images/gemini-journals-dynamic-seo-schemas-cover.png"
  alt = "An abstract image representing structured data and SEO."
  caption = "Visualizing the move to a more structured and dynamic data schema. Image credit: [Google Search Central](https://developers.google.com/search/docs/appearance/structured-data/article)"
+++

## The SEO Problem That Was Hiding in Plain Sight

I had a feeling something was wrong with my website. I was writing news articles, but they weren't showing up in Google's "Top Stories" section. I looked at my website's code and found the problem: every single post, from a deep explanation of AI to a news story about the new iPhone, was being labeled with the same generic "BlogPosting" tag.

For a search engine like Google, this is like putting a newspaper and a diary in the same folder. It's not very smart. My news articles weren't being seen as *news*, which meant I was missing out on a lot of readers. It was time to fix this.

## Working with an AI, Not Just Giving Orders

I told my AI coding partner, Gemini, about the problem. Its first idea was to build a whole new system for labeling my posts. This was a good idea, but I had a feeling there was a better way. My website's theme, PaperMod, is very popular, so I thought it might already have a way to do this.

This is where working with an AI gets really cool. I told Gemini, "I think the theme might already have a way to do this. Can you check?"

That one question changed everything. Gemini immediately started looking through the theme's files and found the answer: a file called `layouts/partials/templates/schema_json.html`.

## The Simple Fix

After looking at the file, Gemini came up with a much better plan. Instead of building something new, we would just make one small change to the existing file.

We copied the file to a special folder on my website (so we wouldn't mess up the original theme) and changed this one line of code:

```go-template
"@type": "BlogPosting",
```

To this:

```go-template
"@type": "{{ .Params.schemaType | default \"BlogPosting\" }}",
```

That's it! This one line changed my whole SEO strategy. It tells my website to check the settings of each post for a `schemaType`. If it finds one, it will use it. If not, it will just use the old "BlogPosting" tag. This is a very smart and simple fix.

To make sure I understood everything, Gemini even explained the difference between the different types of tags:

| Feature | `Article` (for general posts) | `BlogPosting` | `NewsArticle` |
| :--- | :--- | :--- | :--- |
| **Best For** | General articles, guides, and pages that don't change much. | Regular blog posts and opinion pieces. | News stories, announcements, and reports. |
| **What it Tells Google** | "This is an article." | "This is a blog post." | "This is a news report." |
| **How it Affects SEO** | Standard | Good for blog searches | **Best for showing up in news sections** |
| **Example** | [A detailed guide on "What is AI?"]({{< ref "what-is-ai.md" >}}) | [A post on "My Experience with Gemini"]({{< ref "our-gemini-collaboration-solving-the-missing-cover-image.md" >}}) | [An article on "Apple Releases iOS 26"]({{< ref "apple-releases-ios-26-public-beta.md" >}}) |

## A Smarter Blog and a Better Team

With that one change, my blog is now much smarter. I can label my news posts as news, my guides as articles, and my blog posts as blog posts.

This experience taught me that working with an AI is like having a conversation. Sometimes, the best thing you can do is give it a little hint or suggestion. That's when you can find the best and smartest solutions.

### The Gemini Journals Series

1.  [A Day with Gemini: From Code to Content](/posts/a-day-with-gemini/)
2.  [From Lovable Dev to Gemini CLI: A Developer's Journey](/posts/from-lovable-dev-to-gemini-cli/)
3.  [The Gemini CLI Sandbox: A Secure Environment for AI-Powered Development](/posts/gemini-cli-sandbox-security/)
4.  **Dynamic SEO Schemas with Gemini Journals (This Post)**
5.  [My Lovable AI Experience: A Journey of Collaboration](/posts/my-lovable-ai-experience/)
6.  [Our Gemini Collaboration: A Deep Dive](/posts/our-gemini-collaboration-a-deep-dive/)
7.  [Our Gemini Collaboration: Solving the Missing Cover Image](/posts/our-gemini-collaboration-solving-the-missing-cover-image/)
8.  [Gemini CLI in the Cloud: Secure and Isolated Development with Codespaces/Gitpod](/posts/gemini-cli-in-the-cloud/)

