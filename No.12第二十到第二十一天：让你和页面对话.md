作业提交截止时间：09-01

# 第二十到第二十一天：让你和页面对话

## 课程目标

  * 掌握 JavaScript 事件的概念，并能写出基本的事件相关的代码
  * 掌握如何通过 JavaScript 操作 DOM 的样式

## 课程描述

### 阅读

首先学习了解 JavaScript 事件的知识

  * [W3School 事件](http://www.w3school.com.cn/js/js_htmldom_events.asp)
  * [MDN 事件](https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/Building_blocks/Events)
  * [HTML DOM Text 对象](http://www.w3school.com.cn/jsref/dom_obj_text.asp)
  * [HTML DOM Button 对象](http://www.w3school.com.cn/jsref/dom_obj_pushbutton.asp)

### 编码

    
    
    <input id="name" type="text">    
    <button id="submit-btn">Submit</button>
    

在HTML中增加上面的代码，然后通过JavaScript编写如下功能：

  * 当点击按钮 `submit-btn` 时，在console中输出 `name` 中的内容
  * 在输入过程中，如果按回车键，则同样执行上一条的需求
  * 在输入过程中，如果按 ESC 键，则把输入框中的内容清空

### 阅读

接下来学习如何用 JavaScript 操作 DOM 样式

  * [W3School 样式](http://www.w3school.com.cn/js/js_htmldom_css.asp)
  * [W3School HTML DOM Style 对象](http://www.w3school.com.cn/jsref/dom_obj_style.asp)
  * [javascript 动态修改css样式方法汇总(四种方法)](https://www.cnblogs.com/aademeng/articles/6279060.html)
  * [cssText的用法以及特点](https://www.cnblogs.com/majingyi/p/6840818.html)
  * [JavaScript之ClassName属性学习](https://www.cnblogs.com/GreenLeaves/p/5757216.html)

### 编码

控制元素的显示及隐藏

    
    
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">    
        <title>IFE ECMAScript</title>
        <style>
            select {
                display: none;
            }
        </style>
    </head>
    <body>            
        <label>
            <input id="school" name="status" type="radio">
            School
        </label>
        <label>
            <input id="company" name="status" type="radio">
            Company
        </label>
    
        <select id="school-select">        
            <option>北京邮电大学</option>
            <option>黑龙江大学</option>
            <option>华中科技大学</option>
        </select>
    
        <select id="company-select">        
            <option>百度</option>
            <option>爱奇艺</option>        
        </select>
    </body>
    </html>
    

基于如上 HTML，实现以下功能：

  * 当用户选择了 School 的单选框时，显示 School 的下拉选项，隐藏 Company 的下拉选项
  * 当用户选择了 School 的单选框时，显示 Company 的下拉选项，隐藏 School 的下拉选项

### 编码

再次结合事件和样式设置，进行练习

    
    
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">    
        <title>IFE ECMAScript</title>
        <style>
            .palette {
                margin: 0;
                padding: 0;
                list-style: none;
            }
            .palette li {
                width: 40px;
                height: 40px;
                border: 1px solid #000;
                cursor: pointer;
            }
        </style>
    </head>
    <body>            
        <ul class="palette">
            <li style="background-color:crimson"></li>
            <li style="background-color:bisque"></li>
            <li style="background-color:blueviolet"></li>
            <li style="background-color:coral"></li>
            <li style="background-color:chartreuse"></li>
            <li style="background-color:darkolivegreen"></li>
            <li style="background-color:cyan"></li>
            <li style="background-color:#194738"></li>        
        </ul>
    
        <p class="color-picker"></p>
    
        <script>
            var list = document.querySelectorAll("li");
            for (var i = i = 0, len = list.length; i < len; i++) {
                list[i].onclick = function(e) {
                    var t = e.target;
                    var c = t.style.backgroundColor;
                    var p = document.getElementsByClassName("color-picker")[0]
                    p.innerHTML = c;
                    p.style.color = c;
    
                }
            }
        </script>
    </body>
    </html>
    

基于如上 HTML，实现如下功能：

  * 点击某一个 Li 标签时，将 Li 的背景色显示在 P 标签内，并将 P 标签中的文字颜色设置成 Li 的背景色

### 阅读

继续阅读，再次理解 JavaScript 的事件机制，并了解事件代理

  * [初步理解JS的事件机制](https://www.cnblogs.com/lazychen/p/5664788.html)
  * [js中的事件委托或是事件代理详解](https://www.cnblogs.com/liugang-vip/p/5616484.html)
  * [关于JS事件冒泡与JS事件代理（事件委托）](https://blog.csdn.net/supercoooooder/article/details/52190100)
  * [JavaScript事件代理和委托](https://segmentfault.com/a/1190000002613617)

### 编码

基于上面的学习，如果你上一个练习没有用到事件代理的方式，那么请重构上一个编码练习，如果已经用到了，则进入下一个练习

### 阅读

在进行下一个练习之前，我们顺便学习一个新知识：定时

  * [W3School SetTimeout](http://www.w3school.com.cn/jsref/met_win_settimeout.asp)
  * [JS中setTimeout()的用法详解](http://www.jb51.net/article/35535.htm)
  * [W3School SetInterval](http://www.w3school.com.cn/jsref/met_win_setinterval.asp)
  * [js setInterval详解](https://www.cnblogs.com/everest33Tong/p/6322484.html)
  * [JavaScript中SetInterval与setTimeout的用法详解](http://www.jb51.net/article/74606.htm)

### 编码

    
    
    <div id="fade-obj" style="width:300px;height:300px;background:#000"></div>
    <button id="fade-btn">淡出</button>
    

针对以上 HTML，分别使用 setTimeout 和 setInterval 实现以下功能：

  * 点击按钮时，开始改变 fade-obj 的透明度，开始一个淡出（逐渐消失）动画，直到透明度为0
  * 在动画过程中，按钮的状态变为不可点击
  * 在动画结束后，按钮状态恢复，且文字变成“淡入”
  * 在 按钮显示 淡入 的状态时，点击按钮，开始一个“淡入”（逐渐出现）的动画，和上面类似按钮不可点，直到透明度完全不透明
  * 淡入动画结束后，按钮文字变为“淡出”
  * 暂时不要使用 CSS animation （以后我们再学习）

### 阅读

在进行今天最后一个练习时，我们来学习一个新概念：CSS Sprite

  * [浅谈CSS Sprite和实例解析](https://blog.csdn.net/u011349149/article/details/24181675)
  * [CSS 使用Sprites技术实现圆角效果](http://www.jb51.net/article/83111.htm)
  * [SS Sprites:实用技术还是生厌之物](http://www.zhangxinxu.com/wordpress/2010/03/%E7%BF%BB%E8%AF%91-css-sprites%E5%AE%9E%E7%94%A8%E6%8A%80%E6%9C%AF%E8%BF%98%E6%98%AF%E7%94%9F%E5%8E%8C%E4%B9%8B%E7%89%A9%EF%BC%9F/)

### 编码

学习来实现一个帧动画：

  * 基于一个我们提供的图片，实现 [IFE2016中Erik笑容的动画](http://ife.baidu.com/2016/static/index.html)
  * 图片地址：<http://ife.baidu.com/2016/static/img/erik_ce204002.jpg>
  * 注意，依然不要使用 CSS animation，因为我们这里要学习的是使用 JavaScript 来操作 CSS，而不是为了完成这个任务。

### 阅读

最后，可以通过阅读标准，加深理解

  * [W3C](https://www.w3.org/TR/2000/REC-DOM-Level-2-Events-20001113/events.html)

### 提交

把你今天觉得做得最好的代码放在Github后进行提交

### 总结

依然把今天的学习用时，收获，问题进行记录

### 下一个任务预告

我们已经通过许多练习让你体会了 JavaScript 究竟用来干嘛，明天开始，我们将回到许多基础概念，并通过练习来巩固一些基础知识

