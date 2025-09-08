+++
title = "🚀 From Lovable to Netlify: How I Migrated My AirDeals App for Free (and Kept My Custom Domain!)"
date = "2025-08-10T10:00:00Z"
draft = false
tags = ["Netlify", "Supabase", "Lovable", "Vibe Coding", "Web Development", "Deployment", "Custom Domain", "AI", "Gemini"]
categories = ["AI & Software"]
description = "A step-by-step guide on migrating a vibe-coded frontend from Lovable to Netlify, maintaining a Supabase backend, and setting up a custom subdomain for free."
cover = { image = "/images/netlify-migration-cover.jpg", alt = "Illustration of app migration from one cloud to another.", caption = "Migrating my app for freedom and flexibility." }
+++



My journey with my flight deal finder app, "[AirDeals](https://test.airdeals.techbytepulse.com)," started on a platform called [Lovable](/posts/my-lovable-ai-experience/). It was a great way to quickly build a working app just by describing what I wanted. The app's "brain" (the backend) was on another platform called Supabase, which was great for storing all my data.

### The Custom Domain Problem

As my app got better, I wanted to give it a more professional web address: `test.airdeals.techbytepulse.com`. But I ran into a problem. To use a custom web address on Lovable, I had to pay for their "Pro" plan.

For a personal project like "AirDeals," which is still a work in progress, paying for a subscription just for a custom web address seemed like too much. I loved using Lovable, but this made me look for other options for hosting the part of my app that people see (the frontend).

### Finding a Free Solution with Gemini

I was already using a service called Netlify to host my main blog, `techbytepulse.com`, for free. So I wondered if I could use Netlify for my "AirDeals" app too.

I asked my AI assistant, Gemini, for help. I explained that I wanted to use Netlify for my app's frontend, even though the backend was on Supabase.

Gemini told me that Netlify would be a great choice. It said that Netlify works well with backends like Supabase. This gave me the confidence to move my app.

### Moving the App: A Simple Process

Moving my app to Netlify was surprisingly easy.

1.  **Moving the Frontend to Netlify:** I took the app's files from Lovable and put them on Netlify. Netlify has a feature that automatically updates my app whenever I make changes to the code.

2.  **The Backend Stayed Put:** The best part was that I didn't have to do anything to my Supabase backend. All my data and other backend stuff stayed right where it was. The frontend on Netlify just talks to the backend on Supabase.

3.  **Setting Up the Custom Web Address:** This was the most important step to get my custom web address for free.
    *   I went to the settings for my domain name, `techbytepulse.com`.
    *   I created a new **CNAME record** for `test.airdeals.techbytepulse.com`.
    *   I pointed this new record to my Netlify app's web address.

    After a few minutes, `https://test.airdeals.techbytepulse.com` was working and showing my app, which was still connected to its Supabase backend.

### The Freedom to Choose

Moving my app has been great. I can now host my app on a platform that works for me and my budget, without having to pay for a custom web address. This shows how powerful modern web development is. You can mix and match different services to build great apps that fit your needs.

My "AirDeals" app is now not only working well, but it's also set up in a way that saves me money and gives me the freedom to make changes in the future.
