import time
import numpy as np

class TemperatureSensor:
    """一个模拟温度传感器的类。"""

    def __init__(self, base_temp=25.0, fluctuation=0.5):
        """
        初始化传感器。
        :param base_temp: 传感器的基础温度（环境温度）。
        :param fluctuation: 温度波动的最大幅度。
        """
        self.base_temp = base_temp
        self.fluctuation = fluctuation
        print(f"温度传感器已初始化，基础温度: {self.base_temp}°C")

    def read_temperature(self):
        """
        读取一次温度数据。
        通过在基础温度上增加一个正态分布的随机噪声来模拟真实读数。
        """
        noise = np.random.randn() * self.fluctuation
        current_temp = self.base_temp + noise
        return round(current_temp, 2)

if __name__ == "__main__":
    print("--- 开始模块自测试 ---")
    sensor = TemperatureSensor(base_temp=22.5, fluctuation=0.2)
    
    print("将在5秒内，每秒读取一次温度：")
    for i in range(5):
        temp = sensor.read_temperature()
        print(f"第 {i+1} 次读数: {temp}°C")
        time.sleep(1)
    
    print("--- 模块自测试结束 ---")