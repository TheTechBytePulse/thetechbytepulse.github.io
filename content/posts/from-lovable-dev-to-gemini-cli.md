+++
title = "From Lovable.dev to Gemini CLI: A Tale of Two AIs in Debugging My SaaS Project"
date = '2025-07-31T12:00:00+00:00'
draft = false
author = "Prateep Gedupudi"
tags = ["Gemini", "Lovable.dev", "SaaS", "Debugging", "Web Development", "Case Study", "AI"]
categories = ["AI & Software", "Gemini Journals"]
series = ["Gemini Journals"]
description = "A case study comparing the experience of using Lovable.dev for bootstrapping a project and the Gemini CLI for deep, iterative debugging."

[cover]
  image = "/images/from-lovable-dev-to-gemini-cli-cover.jpg"
  alt = "An illustration showing a developer working at a computer with the logos of Lovable.dev and Gemini."
  caption = "A tale of two AIs."
+++


I love trying new tools that make my work easier. For my latest project, a website called "[AirDeals](https://test.airdeals.techbytepulse.com)" that helps people find cheap flights, I decided to use AI to help me build it. I used a tool called **Lovable.dev** to create the first version of the website. It was great for getting a working website up and running quickly.

But when I started to fix some small problems (called bugs), I ran out of my free credits on Lovable.dev. This was a good time to try another tool: Google's **[Gemini CLI](/posts/gemini-cli-sandbox-security/)**. I wanted to see if it could help me fix the bugs, even though it had never seen the website's code before.

### The First Bug: The Search Form That Wouldn't Change

The first problem was with the flight search form. It was set up to automatically fill in the user's favorite departure and arrival cities. But if a user tried to type in a new city, the old one would pop right back in.

I explained the problem to Gemini. It looked at the code and suggested a fix. The first try didn't work perfectly. It stopped the form from changing back, but it also stopped the user's favorite cities from loading in the first place.

This is where working with Gemini was great. I told it what was wrong, and it understood what needed to be done. The right solution was to make sure the favorite cities were loaded only once when the page first opened. Gemini added a little piece of code to keep track of this, and it worked!

```javascript
// The code that fixed the problem
const [initialDefaultsSet, setInitialDefaultsSet] = useState(false);

useEffect(() => {
  if (!settingsLoading && settings && !initialDefaultsSet) {
    setOrigin(settings.defaultOrigin || '');
    setDestination(settings.defaultDestination || '');
    setInitialDefaultsSet(true);
  }
}, [settings, settingsLoading, initialDefaultsSet]);
```

This was a good example of how making software is a step-by-step process, whether you're working with a person or an AI.

### The Second Bug: A Problem I'd Seen Before

Next, we moved to the page where users can set up price alerts. When creating a new alert, the currency was stuck on the user's favorite currency, even if they tried to choose a new one.

I had a feeling I knew what was wrong. "This seems like the same problem we just fixed," I told Gemini. It understood right away and used the same fix as before. Just like that, the problem was solved. It was cool to see the AI recognize the same type of problem and use the same solution.

### More Than Just Bugs: Getting Ready for the Real World

With the website working correctly, I asked Gemini a bigger question: "Is this website ready for people to use?"

Gemini gave me a very detailed list of everything I needed to do to get my website ready for the real world. It covered important things like:

-   **Security:** Moving secret codes (like API keys) to a safer place and making sure users' data is protected.
-   **Making it Real:** Switching from a test version of the flight data to the real version.
-   **Making Money:** Adding a way for people to pay for the service, like with Stripe.
-   **Making it Automatic:** Setting up the price checker to run on its own.
-   **Making it Reliable:** Adding tools to track any errors or problems.

To make it even more helpful, Gemini put this whole list into a file called `production_checklist.md` and saved it in my project.

### My Thoughts: A Great New Tool

So, what did I think of the Gemini CLI? It was very impressive. It was able to understand a brand new project, figure out some tricky problems, and work with me to fix them.

This experience also showed me a big difference between the free plans of the two AI tools. Lovable.dev gives you a certain number of free credits each month. Once you use them up, you have to wait until the next month. The Gemini CLI gives you a certain number of free requests every day, and it resets every day. For fixing a lot of bugs in a short time, the daily reset was much better. If I ran out of requests, I could just start again the next day. With a monthly limit, I could have been stuck for weeks.

In the end, the best way to build things is to have a lot of different tools. Lovable.dev was great for starting the project, and the Gemini CLI was perfect for the detailed work that came after. My "AirDeals" website is much better now, and I have a clear plan for what to do next, thanks to my two AI helpers.

### The Gemini Journals Series

1.  [A Day with Gemini: From Code to Content](/posts/a-day-with-gemini/)
2.  **From Lovable Dev to Gemini CLI: A Developer's Journey (This Post)**
3.  [The Gemini CLI Sandbox: A Secure Environment for AI-Powered Development](/posts/gemini-cli-sandbox-security/)
4.  [Dynamic SEO Schemas with Gemini Journals](/posts/gemini-journals-dynamic-seo-schemas/)
5.  [My Lovable AI Experience: A Journey of Collaboration](/posts/my-lovable-ai-experience/)
6.  [Our Gemini Collaboration: A Deep Dive](/posts/our-gemini-collaboration-a-deep-dive/)
7.  [Our Gemini Collaboration: Solving the Missing Cover Image](/posts/our-gemini-collaboration-solving-the-missing-cover-image/)
8.  [Gemini CLI in the Cloud: Secure and Isolated Development with Codespaces/Gitpod](/posts/gemini-cli-in-the-cloud/)