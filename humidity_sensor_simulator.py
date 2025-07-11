import random
import time

class HumiditySensor:
    """一个模拟湿度的传感器类。"""

    def __init__(self, min_humidity=30.0, max_humidity=90.0):
        """
        初始化湿度传感器。
        :param min_humidity: 允许的最低湿度值。
        :param max_humidity: 允许的最高湿度值。
        """
        self.min_humidity = min_humidity
        self.max_humidity = max_humidity
        # 初始湿度设定在范围的中间
        self.current_humidity = (min_humidity + max_humidity) / 2

    def get_current_reading(self):
        """
        模拟获取一次湿度读数。
        湿度会在当前值附近随机小幅波动。
        """
        # 产生一个 -1.5 到 +1.5 之间的随机波动
        fluctuation = random.uniform(-1.5, 1.5)
        self.current_humidity += fluctuation

        # 确保湿度值不会超出设定的范围
        if self.current_humidity < self.min_humidity:
            self.current_humidity = self.min_humidity
        elif self.current_humidity > self.max_humidity:
            self.current_humidity = self.max_humidity

        return self.current_humidity

# --- 模块自测试代码 ---
if __name__ == "__main__":
    print("--- 湿度传感器模块自测试 ---")
    # 创建一个传感器实例
    humidity_sensor = HumiditySensor()
    print(f"传感器已创建，范围: {humidity_sensor.min_humidity}% - {humidity_sensor.max_humidity}%")
    print("开始模拟读取10次数据...")

    try:
        for i in range(10):
            reading = humidity_sensor.get_current_reading()
            # 使用 :.2f 格式化输出，保留两位小数
            print(f"第 {i+1} 次读数: {reading:.2f}%")
            # 模拟每秒读取一次
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n测试被用户中断。")
    
    print("\n--- 自测试结束 ---")