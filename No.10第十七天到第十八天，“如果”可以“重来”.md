作业提交截止时间：09-01

# 第十七天到第十八天，“如果”可以“重来”

## 课程目标

今天将继续学习 JavaScript 的一些基本知识，比如if如果判断，for循环等

## 任务描述

### 阅读

  * [W3School](http://www.w3school.com.cn/js/js_if_else.asp) 从if-else看到异常
  * [MDN](https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/First_steps/Variables) 阅读完JavaScript第一步及JavaScript基础要件

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
    

基于上一个任务中，关于加减乘除的任务，加上对于特殊情况的判断，比如判断两个输入框是否都是正常输入了数字类型的内容，比如除法的时候除数是否为0，当判断到输入有异常的时候，把错误信息提示到Console中。

### 编码

阅读
[通过除2取余的方法来把十进制整数转化为二进制](https://baike.baidu.com/item/%E5%8D%81%E8%BF%9B%E5%88%B6%E8%BD%AC%E4%BA%8C%E8%BF%9B%E5%88%B6/393189?fr=aladdin)，然后做一个小练习，基于下面代码，完成该转化算法，并实现页面交互

### 编码

    
    
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">    
        <title>IFE ECMAScript</title>
    </head>
    <body>        
        <input id="dec-number" type="number" placeholder="输入一个十进制非负整数">
        <button id="trans-btn">转化为二进制</button>
        <p id="result">运算结果</p>
        <script>
    
    function dec2bin(decNumber) {
        // 在这里实现你的转化方法，注意需要判断输入必须为一个非负整数
    }
    
    // 实现党点击转化按钮时，将输入的十进制数字转化为二进制，并显示在result的p标签内
    // Some coding
    
        </script>
    </body>
    </html>
    

需求说明

  * 实现党点击转化按钮时，将输入的十进制数字转化为二进制，并显示在result的p标签内

### 编码

基于上一个任务，继续完成更多需求

    
    
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">    
        <title>IFE ECMAScript</title>
    </head>
    <body>        
        <input id="dec-number" type="number" placeholder="输入一个十进制非负整数">
        <input id="bin-bit" type="number" placeholder="输入转化后二进制数字位数">
        <button id="trans-btn">转化为二进制</button>
        <p id="result">运算结果</p>
        <script>
    
    function dec2bin(decNumber) {
        // 在这里实现你的转化方法，注意需要判断输入必须为一个非负整数
        // 这里是上一个任务的实现
    }
    
    // 实现党点击转化按钮时，将输入的十进制数字转化为二进制，并显示在result的p标签内
    // 新的需求是，转化显示后的二进制数为bin-bit中输入的数字宽度，例如
    // dec-number为5，bin-bit为5，则转化后数字为00101
    // 如果bin-bit小于转化后的二进制本身位数，则使用原本的位数，如dec-number为5，bin-bit为2，依然输出101，但同时在console中报个错
    // Some coding
    
        </script>
    </body>
    </html>
    

需求说明

  * 新的需求是，转化显示后的二进制数为bin-bit中输入的数字宽度，例如
  * dec-number为5，bin-bit为5，则转化后数字为00101
  * 如果bin-bit小于转化后的二进制本身位数，则使用原本的位数，如dec-number为5，bin-bit为2，依然输出101，但同时在console中报个错

### 编码

3的小游戏，练习使用循环和条件语句，实现如下需求：

  * 从1到100，以此在console输出各数字，但是，当数字为3的倍数或者含有3的时候，输出“PA”
  * 比如：1,2,PA,4,5,PA,……,11,PA,PA,14,PA……

### 编码

小练习，练习使用循环实现一个九九乘法表

  * 第一步，最低要求：在Console中按行输出 n * m = t
  * 然后，尝试在网页中，使用table来实现一个九九乘法表

### 编码

今天最后一个练习，在你的简历中，实现一个，当用户访问页面的时候，根据当前时间，在页面中输出不同的问候语。

比如早上的时候，输出早上好，晚上的时候是晚上好。

### 编码

三天的练习，你应该能够掌握JavaScript基本的语法，如果有余力，你不妨去 [LeetCode](https://leetcode-cn.com/)
使用 JavaScript 来做更多的练习。

### 提交

把你今天觉得做得最好的代码放在Github后进行提交

### 总结

依然把今天的学习用时，收获，问题进行记录

### 下一个任务预告

明天我们将学习 JavaScript 中 DOM 的相关知识

