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

As a developer, optimizing website performance is a top priority, and one of the most effective ways to achieve this is by compressing images. Large image files can significantly slow down page load times, leading to a poor user experience. While there are many tools available for image compression, macOS users have a powerful and convenient utility built right into the operating system: `sips` (Scriptable Image Processing System).

In this tutorial, we'll explore how to use `sips` to quickly and efficiently compress images, making your website faster and more efficient.

### Prerequisites

The best part about using `sips` is that it comes pre-installed on macOS. This means there are no external dependencies or installations required. All you need is:

- A computer running macOS.
- Access to the Terminal application.

### Compressing a Single Image

Let's start with the basics. To compress a single image, you can use the `--resampleHeight` or `--resampleWidth` option to resize the image, which in turn reduces the file size. For example, to resize an image to a maximum width of 1024 pixels while maintaining the aspect ratio, you would use the following command:

```bash
sips --resampleWidth 1024 your-image.jpg
```

This command will overwrite the original file with the new, smaller version. If you want to keep the original, make sure to create a backup first.

### Compressing Multiple Images

Now, let's consider a more practical scenario where you have a directory full of images for your website. Compressing them one by one would be tedious, but with a simple `for` loop, you can process them all at once.

Navigate to the directory containing your images and run the following command:

```bash
for i in *.jpg; do sips --resampleWidth 1024 "$i"; done
```

This command iterates through all files ending with `.jpg` in the current directory and resizes each to a maximum width of 1024 pixels.

### Advanced Compression with Quality Adjustment

For even greater control over the file size, you can adjust the image quality. The `--setProperty` option allows you to change the format and quality of JPEG images. For example, to set the quality to medium, you can use:

```bash
sips -s format jpeg -s formatOptions "medium" your-image.jpg
```

You can also combine this with resizing for maximum effect:

```bash
for i in *.jpg; do sips --resampleWidth 1024 -s format jpeg -s formatOptions "medium" "$i"; done
```

This command will resize all JPEG images to a width of 1024 pixels and set their quality to medium, resulting in a significant reduction in file size.

### Conclusion

The `sips` command-line tool is a powerful and convenient utility for macOS users who need to perform quick and efficient image compression. By mastering a few simple commands, you can dramatically reduce the size of your website's images, leading to faster load times and a better user experience. The next time you need to optimize images, give `sips` a try—you might be surprised at how easy and effective it is.
