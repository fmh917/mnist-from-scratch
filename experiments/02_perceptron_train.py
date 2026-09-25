import numpy as np
#输入
x=1
#目标值
t=1
#初始参数
w=-0.2
b=0
#学习率
lr=0.1
#-----训练-----
for step in range(10):
    #前向传播
    y=w*x+b
    #计算损失
    loss=0.5*(y-t)**2
    #反向传播
    grad_y=y-t
    grad_w=grad_y*x
    grad_b=grad_y
    #更新参数
    w=w-lr*grad_w
    b=b-lr*grad_b

    print(f"Step: {step}, Loss: {loss:.4f}, w: {w:.4f}, b: {b:.4f}")

    