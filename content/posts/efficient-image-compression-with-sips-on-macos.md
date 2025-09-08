+++
date = '2025-07-27T12:00:00-05:00'
draft = false
tags = ["macOS", "Web Development", "Image Compression", "CLI", "sips"]
categories = ["DIY & How-To"]
title = 'Efficient Image Compression with `sips` on macOS'
description = "Learn how to use the built-in `sips` command-line tool on macOS to quickly and effectively compress images for your website, improving performance and user experience."
[cover]
  image = "/images/efficient-image-compression-with-sips-on-macos-cover.jpeg"
  alt = "An illustration showing an image being compressed."
  caption = "Compressing images with `sips` on macOS."
+++

If you have a website, making it fast is important. One of the best ways to speed up your website is to make your image files smaller. Large images can make your website load slowly, which can be frustrating for visitors. If you use a Mac, you have a powerful tool already built-in to help you with this: `sips`.

In this guide, we'll show you how to use `sips` to make your images smaller, so your website will be faster.

### What You Need

The best part about using `sips` is that it's already on your Mac. You don't need to install anything. All you need is:

- A Mac computer.
- The Terminal app (you can find it in your Applications folder, inside the Utilities folder).

### Making a Single Image Smaller

Let's start with the basics. To make an image smaller, you can change its height or width. This will also make the file size smaller. For example, to make an image 1024 pixels wide (while keeping the picture from looking stretched), you can use this command in the Terminal:

```bash
sips --resampleWidth 1024 your-image.jpg
```

This command will replace the original image with the new, smaller one. If you want to keep the original, make a copy of it first.

### Making Many Images Smaller at Once

What if you have a whole folder of images for your website? Making them smaller one by one would take a long time. But with a simple loop, you can do them all at once.

Go to the folder with your images in the Terminal and run this command:

```bash
for i in *.jpg; do sips --resampleWidth 1024 "$i"; done
```

This command goes through all the files that end in `.jpg` in the folder and makes each one 1024 pixels wide.

### More Control Over File Size

For even smaller file sizes, you can lower the image quality a little bit. You can do this and resize the image at the same time.

```bash
for i in *.jpg; do sips --resampleWidth 1024 -s format jpeg -s formatOptions "medium" "$i"; done
```

This command will make all your JPEG images 1024 pixels wide and set their quality to "medium." This will make the file sizes much smaller.

### Why You Should Use `sips`

The `sips` tool is a great way for Mac users to quickly make images smaller. By learning a few simple commands, you can make your website load faster for your visitors. The next time you need to make your images smaller, give `sips` a try!
