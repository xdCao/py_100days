# py_100days
[原项目地址](https://github.com/jackfrued/Python-100-Days)


## day10 pygame
简单的小游戏开发， 面向对象

[pygame](https://www.pygame.org/news) 

3d游戏可以使用 Panda3D


## day11 文件读写
### 操作模式
* 'r'	读取 （默认）
* 'w'	写入（会先截断之前的内容）
* 'x'	写入，如果文件已经存在会产生异常
* 'a'	追加，将内容写入到已有文件的末尾
* 'b'	二进制模式
* 't'	文本模式（默认）
* '+'	更新（既可以读又可以写）

### json
* dump: 对象 -> json -> file  将对象保存到json文件
* dumps: 对象 -> json  将对象保存为json字符串
* load: 文件 -> json -> 对象  从文件中加载json对象
* loads: json -> 对象  从字符串加载出对象

## day12 正则
![img.png](img.png)
![img_1.png](img_1.png)
![img_2.png](img_2.png)

python通过re模块提供正则的支持，核心函数如下：
![img_3.png](img_3.png)