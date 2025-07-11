import time
import matplotlib
import matplotlib.pyplot as plt
import platform

# 导入我们自己编写的两个传感器模块
from temperature_sensor_simulator import TemperatureSensor
from humidity_sensor_simulator import HumiditySensor

# --- Matplotlib 全局配置 ---

# 1. 后端配置
try:
    matplotlib.use('TkAgg')
except ImportError:
    print("警告：TkAgg 后端不可用，将使用默认后端。")

# 2. 中文字体配置
try:
    if platform.system() == 'Darwin':
        plt.rcParams['font.sans-serif'] = ['Heiti TC']
    elif platform.system() == 'Windows':
        plt.rcParams['font.sans-serif'] = ['SimHei']
    else:
        plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']
    
    plt.rcParams['axes.unicode_minus'] = False
    print(f"字体配置成功，已尝试设置中文字体为: {plt.rcParams['font.sans-serif']}")
except Exception as e:
    print(f"警告：设置中文字体失败。错误: {e}")

# --- 初始化 ---
print("--- 多传感器监控平台启动 ---")

temp_sensor = TemperatureSensor()
hum_sensor = HumiditySensor()
print("温度和湿度传感器已创建。")

timestamps = []
temperatures = []
humidities = []

# --- 动态图表设置 ---
plt.ion() 
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.set_xlabel("时间 (秒)")
ax1.set_ylabel("温度 (°C)", color='tab:red')
ax1.tick_params(axis='y', labelcolor='tab:red')
# 注意这里的 label='温度'，这是图例的来源
line_temp, = ax1.plot(timestamps, temperatures, 'r-', label='温度')

ax2 = ax1.twinx()
ax2.set_ylabel("湿度 (%)", color='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:blue')
# 注意这里的 label='湿度'
line_hum, = ax2.plot(timestamps, humidities, 'b-', label='湿度')

plt.title("实时温湿度监控")
fig.tight_layout()

# --- 【核心修改】合并双Y轴图例的健壮方法 ---
# 1. 分别从两个轴获取它们的 "handles" (线条对象) 和 "labels" (标签文本)
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()

# 2. 将两组 handles 和 labels 合并，并让 ax1 统一创建一个图例
#    loc='upper right' 明确指定图例显示在右上角
ax1.legend(h1 + h2, l1 + l2, loc='upper right')

print("图表已初始化。按 Ctrl+C 停止程序。")

# --- 主循环：实时数据采集与绘图 ---
start_time = time.time()
try:
    while True:
        current_temp = temp_sensor.get_current_reading()
        current_hum = hum_sensor.get_current_reading()
        
        current_time = time.time() - start_time
        
        timestamps.append(current_time)
        temperatures.append(current_temp)
        humidities.append(current_hum)
        
        line_temp.set_data(timestamps, temperatures)
        line_hum.set_data(timestamps, humidities)
        
        ax1.relim()
        ax1.autoscale_view()
        ax2.relim()
        ax2.autoscale_view()
        
        plt.draw()
        plt.pause(1)

except KeyboardInterrupt:
    print("\n程序被用户中断。正在关闭监控平台...")
finally:
    plt.ioff()
    print("监控平台已关闭。")
    plt.show()