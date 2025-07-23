+++
title = '{{ replace .File.ContentBaseName "-" " " | title }}'
date = {{ .Date }}
draft = true
tags = ["", ""]
series = [""]
category = ""
description = ""

[cover]
  image = "/images/{{ .File.ContentBaseName }}-cover.png"
  alt = ""
  caption = ""
+++

Your content goes here.