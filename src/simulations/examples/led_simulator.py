import time

class LED:
    """模拟一个连接到GPIO的LED"""
    def __init__(self, pin):
        self.pin = pin
        self.state = False  # False代表LED熄灭, True代表LED点亮
        print(f"模拟：LED在引脚 {self.pin} 上初始化完成。当前状态：熄灭")
    
    def on(self):
        """打开LED"""
        if not self.state:
            self.state = True
            print(f"模拟：LED在引脚 {self.pin} 上点亮 (ON)")
    
    def off(self):
        """关闭LED"""
        if self.state:
            self.state = False
            print(f"模拟：LED在引脚 {self.pin} 上熄灭 (OFF)")
    
    def toggle(self):
        """切换LED状态"""
        self.state = not self.state
        state_str = "点亮 (ON)" if self.state else "熄灭 (OFF)"
        print(f"模拟：LED在引脚 {self.pin} 上切换到 {state_str}")
    
    def blink(self, times=5, interval=0.5):
        """
        使LED闪烁指定次数。
        :param times: 闪烁次数
        :param interval: 每次亮/灭的间隔时间（秒）
        """
        print(f"模拟：LED在引脚 {self.pin} 上开始闪烁 {times} 次，间隔 {interval} 秒")
        original_state = self.state # 记录原始状态
        
        if self.state: # 如果当前是亮的
            self.off() # 先熄灭
            time.sleep(interval / 2) # 等待半个间隔，避免立即又亮起显得太快

        for i in range(times):
            self.on()
            time.sleep(interval)
            self.off()
            if i < times - 1: # 最后一次熄灭后不再等待
                time.sleep(interval)
        
        print(f"模拟：LED在引脚 {self.pin} 上闪烁完成。")
        
        # 恢复原始状态 (可选，根据实际需求决定是否恢复)
        # if original_state:
        #    if not self.state: self.on() 
        # else:
        #    if self.state: self.off()

# --- 模块自测试代码 ---
if __name__ == "__main__":
    print("--- LED 模拟器模块测试 ---")
    
    my_led = LED(pin="GPIO17") # 创建一个模拟LED
    
    print("\n[测试] 点亮:")
    my_led.on()
    time.sleep(1)
    
    print("\n[测试] 熄灭:")
    my_led.off()
    time.sleep(1)
    
    print("\n[测试] 切换 (熄灭 -> 点亮):")
    my_led.toggle() 
    time.sleep(1)
    print("[测试] 切换 (点亮 -> 熄灭):")
    my_led.toggle() 
    time.sleep(1)
    
    print("\n[测试] 闪烁 (默认5次，间隔0.5秒，LED初始为灭):")
    my_led.blink()
    
    print("\n[测试] 点亮LED为后续测试做准备:")
    my_led.on() # 先点亮
    time.sleep(0.5)
    print(f"LED当前状态: {'点亮' if my_led.state else '熄灭'}")

    print("\n[测试] 闪烁 (3次，间隔0.2秒，LED初始为亮):")
    my_led.blink(times=3, interval=0.2)
    print(f"闪烁后LED状态: {'点亮' if my_led.state else '熄灭'}") # 闪烁后应该是灭的

    print("\n--- LED 模拟器模块测试结束 ---")
