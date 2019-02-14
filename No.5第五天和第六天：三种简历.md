作业提交截止时间：09-01

# 第五天和第六天 三种简历

## 课程目标

通过阅读及一个小型练习，掌握 CSS 盒模型及通过Float进行简单的布局

## 课程描述

### 阅读

今天我们要学习非常重要的一些知识，这些知识会伴随着你的前端生涯.  
首先我们先学习一下盒模型的概念

  * [MDN-盒模型](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Introduction_to_CSS/Box_model)
  * [MDN-再述盒模型](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Styling_boxes/Box_model_recap)
  * [W3C](https://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#box-model)

接下来我们了解一下浮动

  * [MDN-浮动](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/CSS_layout/Floats)
  * [W3C 浮动](https://www.w3.org/TR/2011/REC-CSS2-20110607/visuren.html#floats)
  * [如何理解 CSS 中的浮动布局方式？](https://www.zhihu.com/question/19915431)
  * [What methods of ‘clearfix’ can I use?](https://stackoverflow.com/questions/211383/what-methods-of-clearfix-can-i-use)
  * [清除浮动（clearfix hack）](http://zh.learnlayout.com/clearfix.html)

### 编码

今天的任务，我们将不在codepen上来实现，打开你电脑本地的代码编辑器（如VSCode，Sublime或者其它），创建一个项目目录，在目录下创建一个resume.html，再创建一个css目录，在css目录下创建一个style_1.css文件。

然后基于上面的阅读学习，实现如下设计稿的一份简历页面，HTML内容写在resume.html中，样式写在style_1.css中。

![设计稿](https://b.bdstatic.com/searchbox/icms/searchbox/img/resume1.png)

实现过程中，请注意：

  * 实现时必须保证布局的一致
  * 字体、宽高、边距等不需要完全一致

### 阅读

在进行今天的第二个练习时，我们希望你首先阅读一些来自企业的HTML及CSS规范，比如下方的百度规范，你也可以自行搜索其他公司的编码规范

  * [编码规范](https://github.com/ecomfe/spec)

然后学习规范后，我们继续下一个编码任务

### 编码

依然还是使用resume.html，在css目录下创建style_2.css，然后在resume.html的CSS文件引用改为style_2.css。

参照下方设计稿进行页面实现。HTML代码请在上一个任务的基础上，根据样式需要进行调整。并在style_2.css中写入新样式。

![设计稿](https://b.bdstatic.com/searchbox/icms/searchbox/img/resume2.png)

### 编码

最后一个任务，我们把这个挑战极端一些。在css目录中创建style_3.css。把resume.html中引用的css改为style_3.css。

参照下方设计稿进行页面实现。HTML代码请在上一个任务的基础上，根据样式需要进行调整。并在style_3.css中写入新样式

![设计稿](https://b.bdstatic.com/searchbox/icms/searchbox/img/resume3.png)

### 编码

接下来，请你把resume.html中引用的css文件从style_3.css改回style_1.css或者style_2.css，看一下样式是否还健在？

如果没有，请对HTML或CSS代码进行相应调整，保证，无论是用 style_1.css 还是 style_2.css 或是
style_3.css，都可以保证页面按照设计稿的要求呈现。也就是说同一份HTML，可以在改变CSS代码的情况下，实现不同样式，达到HTML结构内容和CSS样式的解耦。

### 提交

把你的代码提交到 Github，把 Github 地址提交到作业里，如果有余力的同学，可以学习如何在Github中预览你的HTML代码，并提交预览地址。

  * [这里有很多方法](https://www.zhihu.com/question/24156818)

### 验证

这两天的内容稍多，请反复确认你是否掌握了以下概念

  * 盒模型的概念
  * inline、block和inline-block的概念
  * 内外边距，宽度，高度，box-sizing等属性
  * 浮动，清除浮动
  * 如何使用浮动进行布局

### 总结

依然把今天的学习用时，收获，问题进行记录

### 明天预告

明天的任务依然是一个跨天的带有较多练习的任务，我们将开始学习其他布局的方式，并迎接更真实的编码作业。

