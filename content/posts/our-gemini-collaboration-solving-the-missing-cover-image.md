+++
title = "Our Gemini Collaboration: Solving the Mystery of the Missing Cover Image"
date = '2025-07-29T12:00:00+00:00'
draft = false
author = "Prateep Gedupudi"
tags = ["Gemini", "Hugo", "CSS", "Debugging", "Web Development", "Case Study"]
categories = ["AI & Software", "Gemini Journals"]
series = ["Gemini Journals"]
description = "A step-by-step case study of how a frustrating CSS issue was diagnosed and solved with the help of the Gemini AI assistant, highlighting a real-world debugging journey."

[cover]
  image = "/images/our-gemini-collaboration-solving-the-missing-cover-image-cover.jpg"
  alt = "An illustration showing a magnifying glass over a web page, focusing on a missing image."
  caption = "The case of the missing cover image."
+++

Every person who works with computers knows this feeling: you make a change that should work, but it doesn't. This is a story about one of those times. I was working with the [Gemini CLI](/posts/a-day-with-gemini/) on a seemingly simple problem: making sure the main picture (the "cover image") for my blog posts showed up on all pages. This turned into a fun little mystery that led us to look deep into the website's code.

### The Goal: Cover Images Everywhere

My goal was simple. I wanted the cover images for my blog posts to show up on all the pages that list my posts, like the homepage, category pages, and tag pages. At first, they were only showing up on the homepage.

### Try #1: Changing the Main Settings

My first idea, and Gemini's too, was to check the website's main settings file. The theme I'm using has a section for the cover image, so we changed the settings to make sure the images were not hidden.

```yaml
cover:
    hidden: false
    hiddenInList: false
    hiddenInSingle: false
```

We saved the change, thinking this would fix the problem. But it didn't. The cover images were still missing from the category and tag pages.

### Try #2: Changing the Website's Template

If the main settings didn't work, the next logical step was to think that the website's template for the list pages was overriding our settings.

Gemini looked at the theme's files and found a line of code that was checking the settings of each individual post, not the main settings file. This seemed to be the problem. To fix it, Gemini created a new version of the file that would use the main settings.

We saved the change. But it *still* didn't work.

### The Real Problem: A Single Line of Code

This was very confusing. The settings were right, and the template was now told to show the images. What else could be hiding them?

This is when Gemini had a great idea. If the website's structure was right, then the problem must be in the way the website was being styled. The problem was in the **CSS**, the code that controls how a website looks.

The template adds a special name, `tag-entry`, to posts when they are on a tag or category page. Gemini searched the CSS files for this name and found the problem:

```css
.tag-entry .entry-cover {
    display: none;
}
```

There it was. A simple line of code that was telling the browser to hide the cover image on any post on a tag or category page. No matter what we did with the settings or the template, this one line of code would always hide the image.

### The Solution: A Simple Fix

Now that we knew the real problem, the fix was easy. We didn't need to change the theme's files. Instead, we created a new CSS file and added one line of code to undo the theme's style:

```css
.tag-entry .entry-cover {
    display: block;
}
```

The theme is set up to automatically use this new file, so it was the perfect place to put our fix.

With this final change, the cover images showed up on all the pages, just like I wanted.

### What We Learned

This was a great reminder that fixing problems is a process of elimination. We started with the most likely problem (the settings), then moved to the next (the template), and finally found the real problem in a place we didn't think to look at first (the CSS). It shows that it's important to understand all the different parts of a website and how they work together. It was also a great example of how an AI can help you solve a problem, even when the first few guesses are wrong.

### The Gemini Journals Series

1.  [A Day with Gemini: From Code to Content](/posts/a-day-with-gemini/)
2.  [From Lovable Dev to Gemini CLI: A Developer's Journey](/posts/from-lovable-dev-to-gemini-cli/)
3.  [The Gemini CLI Sandbox: A Secure Environment for AI-Powered Development](/posts/gemini-cli-sandbox-security/)
4.  [Dynamic SEO Schemas with Gemini Journals](/posts/gemini-journals-dynamic-seo-schemas/)
5.  [My Lovable AI Experience: A Journey of Collaboration](/posts/my-lovable-ai-experience/)
6.  [Our Gemini Collaboration: A Deep Dive](/posts/our-gemini-collaboration-a-deep-dive/)
7.  **Our Gemini Collaboration: Solving the Missing Cover Image (This Post)**
8.  [Gemini CLI in the Cloud: Secure and Isolated Development with Codespaces/Gitpod](/posts/gemini-cli-in-the-cloud/)