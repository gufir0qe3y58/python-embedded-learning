import csv
import platform
import matplotlib.pyplot as plt

def set_chinese_font():
    """根据操作系统设置合适的中文字体。"""
    system = platform.system()
    if system == 'Darwin':
        plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'STHeiti']

    elif system == 'Windows':
        plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    else:
        plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei']
    plt.rcParams['axes.unicode_minus'] = False

def analyze_log(log_file="temperature_log.csv"):
    """
    读取并分析温度日志文件，然后绘制图表。
    """
    print(f"正在分析日志文件: {log_file}")
    timestamps = []
    temperatures = []

    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader) # 读取并跳过表头
            print(f"文件表头: {header}")

            for row in reader:
                # **修正点在这里！** 将字符串转换为浮点数
                timestamps.append(float(row[0]))
                temperatures.append(float(row[1]))
    
    except FileNotFoundError:
        print(f"错误: 日志文件 '{log_file}' 未找到。")
        print("请先运行 'temperature_monitor_demo.py' 来生成日志文件。")
        return # 提前退出函数
    except ValueError:
        print(f"错误: 文件 '{log_file}' 中的数据格式不正确。请确保都是数字。")
        return
    except Exception as e:
        print(f"发生未知错误: {e}")
        return

    # --- 数据可视化 ---
    set_chinese_font()
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, temperatures, marker='.', linestyle='--')
    plt.title("历史温度数据回放")
    plt.xlabel("时间 (秒)")
    plt.ylabel("温度 (°C)")
    plt.grid(True)
    print("数据分析完成，正在生成图表...")
    plt.show()

if __name__ == "__main__":
    analyze_log()