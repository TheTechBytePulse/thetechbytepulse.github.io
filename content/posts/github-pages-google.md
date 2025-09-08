+++
date = '2025-07-08T13:16:32Z'
draft = false
tags = ["Hugo", "Google Search Console", "SEO", "GitHub Pages", "Static Site Generator", "Tutorial"]
categories = ["Tech Explained"]
title = '🔎 How to verify your Hugo site with Google Search Console'
description = "A step-by-step guide on how to verify your Hugo static site with Google Search Console by placing the HTML verification file in the static directory."

[cover]
  image = "/images/github-pages-google-cover.jpg"
  alt = "The logos of GitHub Pages and Google Search Console."
  caption = "Get your GitHub Pages site indexed by Google."
+++
To get your Hugo website to show up in Google search results, you need to prove to Google that you own the website. You can do this using a free tool from Google called Google Search Console. This guide will show you how to do it.

The easiest way to do this is to upload a special HTML file from Google to your website. Here's how to do it with Hugo.

{{< youtube s0Tuat2VReQ >}} 

**Here's a step-by-step guide:**

1.  **Create a "static" folder:** If you don't already have one, create a folder called `static` in the main folder of your Hugo project.
2.  **Put the Google file in the "static" folder:** Google will give you a special HTML file to download. It will have a name like `googleXXXXXXXX.html`. Put this file inside the `static` folder.
3.  **Publish your website:** Upload your website to the internet like you normally do (using a service like Netlify or GitHub Pages).
4.  **Verify in Search Console:** Once your website is online, go back to Google Search Console and choose the "HTML file" option to verify. Type in the web address of your verification file (for example, `https://yourwebsite.com/googleXXXXXXXX.html`) and click "Verify."

**Important things to remember:**

*   **Where to put the file:** Make sure the Google file is directly inside the `static` folder, not in any other folders inside it.
*   **File name:** If you have trouble with the `.html` part of the file name, try leaving it off (for example, `https://yourwebsite.com/googleXXXXXXXX`). Sometimes Hugo will handle this for you.
*   **Your website's theme:** If you are using a theme for your website, make sure it's not changing how the `static` folder works. You can check the theme's instructions to be sure.
*   **Hugo version:** If you are using an old version of Hugo, you might want to update it to the newest version. This can fix some problems with how files are shown on your website.