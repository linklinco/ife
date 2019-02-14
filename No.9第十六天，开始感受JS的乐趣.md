作业提交截止时间：09-01

# 第十六天，开始感受JS的乐趣

## 课程目标

从今天开始，我们要开始学习在Web开发中使用 JavaScript/ECMAScript 来实现各种各样的交互逻辑及数据处理，今天的目标是初步了解
JavaScript/ECMAScript 是什么，开始学习基本的语法，并通过几个小例子的练习，来初步感受语言的魅力。

已经有经验的同学，可以直接跳过此课。

### 阅读

首先我们阅读一些定义和历史，放轻松阅读，不用背下来。

  * [W3School JavaScript](http://www.w3school.com.cn/js/js_intro.asp)
  * [MDN 什么是JavaScript？](https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
  * [一文读懂JavaScript和ECMAScript的区别](http://developer.51cto.com/art/201711/557514.htm)
  * [W3School JavaScript历史](http://www.w3school.com.cn/js/pro_js_history.asp)

### 编码

接下来，我们用一些小练习来感受一下 JavaScript。

在你的IDE（Visual Studio Code或其它）中新建一个js_16.html（也可以其它名字）的文件，然后把下面代码复制粘贴到文件中：

    
    
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">    
        <title>IFE ECMAScript</title>
    </head>
    <body>
        <h1>Demo</h1>
        <p id="content-wrapper">Hello World</p>
        <script>
            console.log(document.getElementById("content-wrapper").innerHTML);
        </script>
    </body>
    </html>
    

然后使用 Chrome 浏览器打开这个网页。并打开 Chrome 的开发者工具（不知道如何打开的请自行百度）。

这时候你可以发现在开发者工具的 Console 中应该有输出`Hello World`了。在这个例子中，`script`标签中的内容就是
JavaScript
代码，在这个代码中，我们只有一行代码，我们执行力`console.log`一个函数，用于在Chrome中的Console中输出一个内容，这将是我们今后写
JavaScript 代码中最常用的调试手段之一，当然你也可以尝试一下十多年前前端工程师的调试方法，把`console.log`换成`alert`。

在这一行代码中，还可以关注的是 `document.getElementById` 和 `innerHTML`，可以通过自行搜索了解他们是什么意思。

接下来，我们给这个代码加一些内容：

    
    
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">    
        <title>IFE ECMAScript</title>
    </head>
    <body>
        <h1>Demo</h1>
        <p id="content-wrapper">你是谁？</p>
        <input id="name-input" type="text" placeholder="输入你的名字">
        <button id="send-btn">发送</button>
        <script>        
            document.getElementById("send-btn").onclick = function() {
                document.getElementById("content-wrapper").innerHTML = 'Hello ' + document.getElementById("name-input").value;
            }
        </script>
    </body>
    </html>
    

把刚才的代码替换一下，然后尝试在浏览器中运行一下，在输入框中输入一些文字，然后点按钮。看看发生了什么。

在这个短小的例子中，我们简单演示了 JavaScript
用得最多的场景，从提供给用户的表单组件中获取输入内容，然后做一些处理，并在页面中做出对应的呈现。好，接下来，需要你大量的进行阅读和练习

### 阅读

我们开始学习 JavaScript 的基础语法，变量，函数等概念，你先阅读一遍，然后我们会有对应练习提供给您。

  * [《JavaScript 高级程序设计》](https://book.douban.com/subject/10546125/)
  * [W3School JS教程](http://www.w3school.com.cn/js/index.asp)，从JS简介阅读到运算符

### 编码

    
    
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">    
        <title>IFE ECMAScript</title>
    </head>
    <body>        
        <input id="first-number" type="number" value="0" placeholder="第一个数字">
        <input id="second-number" type="number" value="0" placeholder="第二个数字">
        <button id="add-btn">加</button>
        <button id="minus-btn">减</button>
        <button id="times-btn">乘</button>
        <button id="divide-btn">除</button>
        <p id="result">运算结果</p>
        <script>
    
        </script>
    </body>
    </html>
    

复制以上代码到你的IDE中，然后在`script`标签中编写代码，实现以下需求：

  * 点对应加减乘除按钮的时候，将两个输入框中的数字做对应的算术，并将结果显示在id为result的p标签内。
  * 暂时不用做任何异常处理

### 任务编码

好的，上面只是小练习，还记得最开始你做的简历任务吗？今天最后的任务是在你的简历任务中尝试实现以下需求：

  * 在简历中增加一些按钮，比如 **和你打招呼** ， **点开看看我的特殊爱好** ，然后点了按钮以后，在Console或者是页面某个节点来展示一段特殊内容

### 提交

把你的简历代码及预览进行提交

### 总结

依然把今天的学习用时，收获，问题进行记录

### 下一个任务预告

明天我们继续学习 JavaScript 中的基础语法

