import numpy as np

def step_function(x):
    """阶跃函数"""
    return np.where(x >= 0, 1, 0)

def perceptron(x,w,b):
    """感知机"""
    z=np.dot(x,w)+b  #点积计算加权和
    y=step_function(z)
    return y
#权重初始化
w=np.array([0.5,0.5])
#偏置初始化
b=-0.7
#AND逻辑门输入
inputs=[
    np.array([0,0]),
    np.array([0,1]),
    np.array([1,0]),
    np.array([1,1])
]

for x in inputs:
    y=perceptron(x,w,b)
    print(f"Input: {x}, Output: {y}")