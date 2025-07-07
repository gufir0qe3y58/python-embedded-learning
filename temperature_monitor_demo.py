import time
import platform
import csv
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
from temperature_sensor_simulator import TemperatureSensor

def set_chinese_font():
    """根据操作系统设置合适的中文字体。"""
    system = platform.system()
    if system == 'Darwin':
        plt.rcParams['font.sans-serif'] = ['PingFang SC']
    elif system == 'Windows':
        plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    else:
        plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei']
    plt.rcParams['axes.unicode_minus'] = False
    print(f"当前操作系统: {system}, 已设置中文字体。")

def run_monitor(duration_seconds=10, log_file="temperature_log.csv"):
    """
    运行温度监控，绘制图表，并将数据记录到CSV文件。
    :param duration_seconds: 监控持续的总秒数。
    :param log_file: 保存数据的文件名。
    """
    sensor = TemperatureSensor(base_temp=28.0, fluctuation=0.8)
    
    timestamps = []
    temperatures = []
    
    print(f"开始监控温度，持续 {duration_seconds} 秒...")
    print(f"数据将记录到: {log_file}")

    # 使用 'w' (write) 模式打开文件，newline='' 是csv模块推荐的用法，防止空行
    with open(log_file, 'w', newline='', encoding='utf-8') as f:
        # 创建一个csv写入器
        writer = csv.writer(f)
        # 写入表头
        writer.writerow(['timestamp', 'temperature'])
        
        start_time = time.time()
        while time.time() - start_time < duration_seconds:
            temp = sensor.read_temperature()
            current_time = time.time() - start_time
            
            timestamps.append(current_time)
            temperatures.append(temp)
            
            # 将新数据写入CSV文件
            writer.writerow([round(current_time, 2), temp])
            
            print(f"时间: {current_time:.2f}s, 温度: {temp}°C (已记录)")
            time.sleep(0.5)

    # --- 数据可视化 ---
    set_chinese_font()
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, temperatures, marker='o', linestyle='-')
    plt.title("实时温度监控")
    plt.xlabel("时间 (秒)")
    plt.ylabel("温度 (°C)")
    plt.grid(True)
    print("数据采集完成，正在生成图表...")
    plt.show()
    print("图表已关闭。")

if __name__ == "__main__":
    run_monitor()