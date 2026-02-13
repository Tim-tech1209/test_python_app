def temperature_converter():
    """摄氏度转华氏度"""
    print("=== 温度转换器 ===")
    
    # 获取用户输入
    celsius = float(input("请输入摄氏度温度: "))
    
    # 转换为华氏度
    fahrenheit = celsius * 9/5 + 32
    
    # 格式化输出，保留2位小数
    print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")

# 运行程序
if __name__ == "__main__":
    temperature_converter()
