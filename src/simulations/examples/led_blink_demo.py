import time  # 这一行是需要的，因为你的 main 函数中用到了 time.sleep()
import sys
import os

# 获取项目根目录并添加到Python路径
current_file_path = os.path.abspath(__file__)  # 当前文件的完整路径
examples_dir = os.path.dirname(current_file_path)  # examples目录
simulations_dir = os.path.dirname(examples_dir)  # simulations目录
src_dir = os.path.dirname(simulations_dir)  # src目录
project_root = os.path.dirname(src_dir)  # 项目根目录
sys.path.append(project_root)  # 将项目根目录添加到Python路径

# 现在可以正常导入了
from src.simulations.examples.led_simulator import LED  # 这一行是导入 LED 类的关键

def main():
    """演示LED闪烁的主函数"""
    print("---- LED 闪烁演示程序启动 ----")

    try:
        # 创建模拟的LED对象，假设连接到GPIO引脚17
        # 你的 LED 类构造函数接受 pin 参数
        led = LED(pin=17) 
        
        # 初始化状态打印，使用 led.state
        print(f"模拟：LED在引脚 {led.pin} 上初始化完成。当前状态：{'点亮' if led.state else '熄灭'}\n")

        print("[测试] 点亮:")
        led.on()
        time.sleep(0.5) # 稍作停留以便观察

        print("\n[测试] 熄灭:")
        led.off()
        time.sleep(0.5)

        print("\n[测试] 切换 (熄灭 -> 点亮):")
        led.toggle() # 应该点亮
        time.sleep(0.5)

        print("\n[测试] 切换 (点亮 -> 熄灭):")
        led.toggle() # 应该熄灭
        time.sleep(0.5)

        print("\n[测试] 闪烁 (默认5次，间隔0.5秒，LED初始为灭):")
        # 你的 LED 类 blink 方法默认 times=5, interval=0.5
        led.blink() 
        # 注意：你的 blink 方法在闪烁结束后，LED 会是熄灭状态。
        # 如果需要等待闪烁动画在终端完全打完，可以加一个短暂的 sleep
        # time.sleep(0.1) # 可选，确保所有打印完成

        print("\n[测试] 点亮LED为后续测试做准备:")
        led.on()
        # 状态打印，使用 led.state
        print(f"LED当前状态: {'点亮' if led.state else '熄灭'}\n")
        time.sleep(0.5)

        print("[测试] 闪烁 (3次，间隔0.2秒，LED初始为亮):")
        led.blink(times=3, interval=0.2)
        # 状态打印，使用 led.state
        # 你的 blink 方法在闪烁结束后，LED 会是熄灭状态。
        print(f"闪烁后LED状态: {'点亮' if led.state else '熄灭'}\n")

    except NameError:
        # 这个错误通常是因为 LED 类没有被成功导入，或者在调用 LED() 之前就出错了
        print("错误：无法创建或使用 LED 对象。可能的原因：")
        print("1. 'from src.simulations.examples.led_simulator import LED' 导入失败。")
        print("   请检查 led_simulator.py 文件是否存在于正确的路径，以及所有 __init__.py 文件是否已创建。")
        print("2. LED 类在 led_simulator.py 中可能未定义或名称不匹配。")
    except AttributeError as e:
        print(f"错误：调用LED对象方法时出错: {e}。请检查LED类中是否有对应的方法。")
    except TypeError as e:
        print(f"错误：调用LED对象方法时参数不匹配: {e}。请检查方法定义和调用。")
    except Exception as e:
        print(f"发生未知错误: {e}")

    print("\n---- LED 闪烁演示程序结束 ----")

if __name__ == "__main__":
    main()
