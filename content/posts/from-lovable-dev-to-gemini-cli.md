+++
title = "From Lovable.dev to Gemini CLI: A Tale of Two AIs in Debugging My SaaS Project"
date = '2025-07-31T12:00:00+00:00'
draft = false
author = "Prateep Gedupudi"
tags = ["Gemini", "Lovable.dev", "SaaS", "Debugging", "Web Development", "Case Study", "AI"]
categories = ["AI", "Web Development"]
series = ["Gemini Journals"]
description = "A case study comparing the experience of using Lovable.dev for bootstrapping a project and the Gemini CLI for deep, iterative debugging."

[cover]
  image = "/images/from-lovable-dev-to-gemini-cli-cover.jpg"
  alt = "An illustration showing a developer working at a computer with the logos of Lovable.dev and Gemini."
  caption = "A tale of two AIs."
+++


As a Vibe Coder, I'm always excited to explore new tools that can streamline my workflow. For my latest project, "AirDeals"—a flight deal tracker—I decided to go all-in on AI-driven development from the start. I used the **Lovable.dev** platform to bootstrap and build the entire application, and the experience was fantastic for getting a feature-rich prototype off the ground quickly.

However, as I was getting into the nitty-gritty of debugging, I hit a small roadblock: I had run out of my monthly credits on the platform. This felt like the perfect opportunity to put another tool to the test: Google's **Gemini CLI**. Could it jump into a codebase it had no prior context on and help me squash the remaining bugs? I was eager to find out.

### The First Bug: The Frustratingly Sticky Search Form

The first issue was a tricky one. The main flight search form was designed to load the user's saved preferences (default origin and destination), which was great. But it was too "sticky"—if a user tried to clear a field to type in a new city, the saved default would immediately snap back.

I explained the problem to Gemini. It quickly analyzed the `FlightSearchForm.tsx` component and proposed a fix. Its first attempt was logical, but it didn't quite stick the landing. It prevented the form from being overwritten, but it also stopped the initial preferences from loading at all.

This is where the collaboration shined. After I provided feedback, Gemini understood the nuance required. The correct solution was to ensure the defaults were set only *once* when the component first loaded. Gemini introduced a state flag, `initialDefaultsSet`, to track this, which worked perfectly.

```javascript
// The final, working solution
const [initialDefaultsSet, setInitialDefaultsSet] = useState(false);

useEffect(() => {
  if (!settingsLoading && settings && !initialDefaultsSet) {
    setOrigin(settings.defaultOrigin || '');
    setDestination(settings.defaultDestination || '');
    setInitialDefaultsSet(true);
  }
}, [settings, settingsLoading, initialDefaultsSet]);
```

It was a great example of the iterative process that defines software development, whether you're working with a human or an AI.

### The Second Bug: A Familiar Foe

With one bug down, we moved to the price alerts page. When creating a new alert, the currency field was getting stuck on the user's saved preference, ignoring any new selection.

I immediately had a hunch. "This feels like the exact same bug we just fixed," I told Gemini. It immediately understood the pattern, applied the same `initialDefaultsSet` logic to the `PriceAlerts.tsx` component, and just like that, the issue was resolved. It was impressive to see it recognize a recurring pattern and apply a known solution so quickly.

### Beyond the Bugs: Charting a Course for Production

With the app now working as intended, I decided to push Gemini further. "Is this thing ready for production?" I asked.

What followed was an incredibly thorough and insightful breakdown of everything I'd need to consider for a real-world micro-SaaS application. It covered critical areas like:

-   **Security:** Moving hardcoded API keys to environment variables and implementing Supabase Row Level Security (RLS).
-   **Infrastructure:** Switching from the Amadeus test API to their production environment.
-   **Monetization:** Integrating a payment provider like Stripe.
-   **Automation:** Setting up the price tracking function as a Supabase Cron Job.
-   **Reliability:** Adding proper logging and error tracking.

To make this even more actionable, Gemini compiled the entire list into a `production_checklist.md` file and saved it in my project.

### My Verdict: A Powerful New Tool in the Arsenal

So, how did Gemini CLI fare? Impressively well. It was able to jump into a codebase it had never seen, understand the context from our conversation, diagnose complex React state management issues, and collaborate on fixes.

This experience also highlighted a key difference in their free tier models, especially since I'm not a paying user on either platform. Lovable.dev offers a free plan with 5 daily credits, but it's capped at 30 credits per month. Once I exhausted my monthly quota, my progress on the platform was stalled until the next cycle. Gemini CLI, on the other hand, offers a free tier with a daily limit of 100 requests that resets every day, without a monthly cap. For the kind of focused, high-intensity debugging I was doing, this daily refresh was a game-changer. Hitting a daily limit means I can just pick things up the next day, whereas a monthly limit could have left me blocked for weeks.

Ultimately, the future of development isn't about finding a single, all-powerful AI, but about having a versatile toolkit at your disposal. Lovable.dev was invaluable for getting the project off the ground, and Gemini CLI was the perfect tool for the deep, iterative work that followed. The journey of "AirDeals" is far from over, but it's now more robust and has a clear path forward, thanks to a little help from two very different AI friends.
