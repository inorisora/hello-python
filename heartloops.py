import sys
import numpy as np
import matplotlib.pyplot as plt   #此部分为调用工具，同时简化调用名称

print("Interpreter:",sys.executable)
print("Numpy:",np.__version__)    #这一部分给开发者看，告知interpreter调用的位置，和numpy这个软件的版本

n=0
while n<3:
 t = np.linspace(0,2 * np.pi,600)
 x = 16 * np.sin(t)**3+50*n
 y = 13 * np.cos(t)-5 * np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t) #此部分是构建t的有关x，y参数方程
 plt.plot(x,y,color="pink")   #对线段x，y的颜色修改，不添加就会是默认状态
 n = n + 1
plt.title("to shenyuan my love,three") # 生成图片内部的标题名字
plt.savefig("To_shenyuan,three.png",dpi=280) #保存时候文件的名字，与分辨率设置
print("saved To_shenyuan.png - you success!!") #最后终端输出提示信息，表示文件成功生成