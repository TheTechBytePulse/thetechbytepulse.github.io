+++
date = '2025-07-08T13:16:32Z'
draft = false
tags = ["Hugo", "Google Search Console", "SEO", "GitHub Pages", "Static Site Generator", "Tutorial"]
categories = ["Web Development", "Blogging"]
title = '🔎 How to verify your Hugo site with Google Search Console'
description = "A step-by-step guide on how to verify your Hugo static site with Google Search Console by placing the HTML verification file in the static directory."

[cover]
  image = "/images/github-pages-google-cover.jpg"
  alt = "The logos of GitHub Pages and Google Search Console."
  caption = "Get your GitHub Pages site indexed by Google."
+++
To verify your Hugo site with Google Search Console, you need to place the verification file in the static directory of your Hugo project and then publish your site. Hugo will automatically serve files from the static directory at the root of your site.

{{< youtube s0Tuat2VReQ >}}  


**Here's a step-by-step guide:**

1.  Create the static directory: If you don't already have one, create a directory named static at the root of your Hugo project. 
    
2.  **Place the verification file:** Put your Google verification file (e.g., googleXXXXXXXX.html) inside the static directory. 
    
3.  **Publish your site:** Build and deploy your Hugo site using your preferred method (e.g., Netlify, GitHub Pages, etc.). 
    
4.  **Verify in Search Console:** Once your site is live, go to Google Search Console and select the "HTML file" verification method. Enter the URL of your verification file (e.g., https://yourdomain.com/googleXXXXXXXX.html) and click "Verify". 
    

**Important Considerations:** 

*   **File Location:** Ensure the verification file is placed directly inside the static directory, not within any subfolders.
    
*   **File Extension:** If you are having trouble with the .html extension, try accessing the file without it (e.g., https://yourdomain.com/googleXXXXXXXX) as Hugo might handle the extension automatically.
    
*   **Theme Overrides:** If you are using a theme, make sure it's not overriding the static directory or its contents. Check your theme's documentation or settings.
    
*   **Hugo Version:** If you are using an older version of Hugo, consider updating to the latest version as it may contain fixes for file serving issues.