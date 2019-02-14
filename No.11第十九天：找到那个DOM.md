作业提交截止时间：09-01

# 第十九天：找到那个DOM

## 课程目标

掌握 JavaScript 的核心之一：DOM，能够熟悉DOM相关操作，了解JavaScript事件机制

## 课程描述

### 阅读

  * [W3School](http://www.w3school.com.cn/js/js_htmldom.asp)
  * [MDN DOM](https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/Client-side_web_APIs/Manipulating_documents)
  * [《JavaScript 高级程序设计》](https://book.douban.com/subject/10546125/)

### 编码

查找元素练习

    
    
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">    
        <title>IFE ECMAScript</title>
    </head>
    <body>        
        <div id="wrapper">
            <div id="news-top" class="section">
                <h3>Some title</h3>
                <div class="content">
                    <ul>
                        <li><span>HTML</span><a href="">Some Link1</a></li>
                        <li><span>JS</span><a class="active" href="">Some Link2</a></li>
                        <li><span>CSS</span><a href="">Some Link3</a></li>
                        <li><span>JS</span><a href="">Some Link4</a></li>
                    </ul>
                </div>
                <img src="">
                <p class="">Some Text</p>
            </div>
            <div id="news-normal" class="section">
                <h3>Some title</h3>
                <div class="content">
                    <ul>
                        <li><span>HTML</span><a href="">Some Link1</a></li>
                        <li><span>HTML</span><a href="">Some Link2</a></li>
                        <li><span>JS</span><a class="active" href="#">Some Link3</a></li>
                        <li><span>CSS</span><a href="">Some Link4</a></li>
                    </ul>
                </div>
                <img src="">
                <p class="">Some Text</p>
            </div>      
        </div>
        <script>
    
        function getAllListItem() {
            // 返回页面中所有li标签
        }
    
        function findAllHtmlSpanInOneSection(sectionId) {
            // 返回某个section下所有span中内容为HTML的span标签
        }
    
        function findListItem(sectionId, spanCont) {
            // 返回某个section下，所有所包含span内容为spanCont的LI标签
        }
    
        function getActiveLinkContent(sectionId) {
            // 返回某个section下，class为active的链接中包含的文字内容
        }
    
        </script>
    </body>
    </html>
    

使用上诉代码，分别实现 script 标签中的几个函数。

在这个练习中仅允许使用以下 DOM 方法或属性，不得使用高级选择器

  * getElementById()
  * getElementsByTagName()
  * childNodes
  * parentNode

### 阅读

  * [MDN querySelectorAll](https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelectorAll)
  * [MDN document.querySelctor](https://developer.mozilla.org/zh-CN/docs/Web/API/Document/querySelector)
  * [MDN element.querySelector](https://developer.mozilla.org/zh-CN/docs/Web/API/Element/querySelector)

### 编码

再次晚上前面的几个查找元素的练习，但是使用querySelector及querySelectorAll

### 提交

把你今天觉得做得最好的代码放在Github后进行提交

### 总结

依然把今天的学习用时，收获，问题进行记录

### 下一个任务预告

明天我们继续学习 JavaScript 中 DOM 的相关知识

