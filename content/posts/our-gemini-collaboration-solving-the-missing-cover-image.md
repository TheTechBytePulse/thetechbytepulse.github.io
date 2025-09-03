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

Every developer knows the feeling: you make a change that should work, but for some reason, it doesn't. This is the story of one such recent interaction with the [Gemini CLI](/posts/a-day-with-gemini/), where a seemingly simple task—making sure cover images appeared everywhere—turned into a fascinating debugging journey that led us deep into the theme's CSS.

### The Goal: Consistent Cover Images

The goal was straightforward. I wanted the cover images for my blog posts to be visible on all list pages, including the homepage, category pages, and tag pages. Initially, they were only showing up on the homepage.

### Attempt #1: The Global Configuration

My first thought, and Gemini's, was to check the site's main configuration file, `config.yaml`. The PaperMod theme has a `cover` section that seems to control this exact behavior. We uncommented the section and set all the `hidden` parameters to `false`:

```yaml
cover:
    hidden: false
    hiddenInList: false
    hiddenInSingle: false
```

We committed the change, confident this would solve the problem. It didn't. The cover images were still missing from the category and tag pages.

### Attempt #2: The Template Override

If the global configuration wasn't being respected, the next logical step was to assume the theme's template file for list pages (`list.html`) had its own logic that was overriding our settings.

Gemini dived into the theme files and found this line in `themes/PaperMod/layouts/_default/list.html`:

```go-template
{{- $isHidden := (.Param "cover.hiddenInList") | default (.Param "cover.hidden") | default false }}
```

This code checks the *front matter* of each individual post, not the site's `config.yaml`. This seemed to be the smoking gun. To fix it, Gemini created a custom override of the `list.html` file in my site's `layouts/_default/` directory and changed the line to respect the global site parameters.

We committed the change. And yet, it *still* didn't work.

### The Real Culprit: A Single Line of CSS

This was a head-scratcher. The configuration was right, and the template logic was now explicitly told to show the images. What else could be hiding them?

This is where the debugging process took a crucial turn. Gemini realized that if the HTML was being generated correctly, the problem must be in the final rendering layer: the **CSS**.

The `list.html` template adds a special class, `tag-entry`, to posts when they are on a taxonomy page (like a tag or category list). Gemini searched the theme's CSS files for this specific class and found the culprit in `common/post-entry.css`:

```css
.tag-entry .entry-cover {
    display: none;
}
```

There it was. A simple, direct CSS rule that explicitly told the browser to hide the cover image on any post appearing in a tag or category list. No amount of configuration or template changes could have overridden this without touching the CSS.

### The Solution: A CSS Override

The fix was now clear and simple. We didn't need to edit the theme directly. Instead, we created a custom CSS file at `assets/css/extended/custom.css` with a single rule to counteract the theme's style:

```css
.tag-entry .entry-cover {
    display: block;
}
```

The PaperMod theme is designed to automatically load any CSS in this `extended` directory, making it the perfect place for custom styles.

With this final change, the cover images appeared exactly as intended on all pages.

### What This Teaches Us

This collaboration was a powerful reminder that debugging is a process of elimination. We started with the most likely suspect (configuration), moved to the next (templates), and finally uncovered the true cause in a place we hadn't initially considered (CSS). It highlights the importance of understanding the different layers that make up a website and how they interact. It was a great real-world example of how an AI assistant can work through a problem logically, even when the initial assumptions are wrong.

### The Gemini Journals Series

1.  [A Day with Gemini: From Code to Content](/posts/a-day-with-gemini/)
2.  [From Lovable Dev to Gemini CLI: A Developer's Journey](/posts/from-lovable-dev-to-gemini-cli/)
3.  [The Gemini CLI Sandbox: A Secure Environment for AI-Powered Development](/posts/gemini-cli-sandbox-security/)
4.  [Dynamic SEO Schemas with Gemini Journals](/posts/gemini-journals-dynamic-seo-schemas/)
5.  [My Lovable AI Experience: A Journey of Collaboration](/posts/my-lovable-ai-experience/)
6.  [Our Gemini Collaboration: A Deep Dive](/posts/our-gemini-collaboration-a-deep-dive/)
7.  **Our Gemini Collaboration: Solving the Missing Cover Image (This Post)**
8.  [Gemini CLI in the Cloud: Secure and Isolated Development with Codespaces/Gitpod](/posts/gemini-cli-in-the-cloud/)