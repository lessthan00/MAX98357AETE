from decimal import Decimal, getcontext

def calculate_pull_up_resistance(
    pull_down_resistance: Decimal, 
    reference_voltage: Decimal, 
    output_voltage: Decimal, 
    precision: int = 6
) -> Decimal:
    """
    计算上拉电阻 RH 的值，基于分压电路公式: RH = (Vref * RL / Vo) - RL
    
    参数:
        pull_down_resistance (Decimal): 下拉电阻 RL (单位: 欧姆)
        reference_voltage (Decimal): 上拉电压 Vref (单位: 伏特)
        output_voltage (Decimal): 分压结果 Vo (单位: 伏特)
        precision (int): 计算结果的小数精度位数 (默认: 6)
        
    返回:
        Decimal: 上拉电阻 RH 的值 (单位: 欧姆)
        
    异常:
        ZeroDivisionError: 当 output_voltage 为零时引发
        ValueError: 当任何输入参数为负数时引发
    """
    # 设置计算精度
    getcontext().prec = precision
    
    # 验证输入参数非负
    if any(val < Decimal('0') for val in [pull_down_resistance, reference_voltage, output_voltage]):
        raise ValueError("所有输入参数必须为非负数")
    
    # 检查除数不为零
    if output_voltage == Decimal('0'):
        raise ZeroDivisionError("输出电压 Vo 不能为零")
    
    # 执行精确计算
    rh = (reference_voltage * pull_down_resistance / output_voltage) - pull_down_resistance
    
    # 确保结果非负
    return rh if rh >= Decimal('0') else Decimal('0')

# 示例用法
if __name__ == "__main__":
    try:
        RL = Decimal('1e6')  # 100kΩ 下拉电阻
        Vref = Decimal('3.3')  # 3.3V 上拉电压
        Vo = Decimal('1')   # 1.65V 分压输出
        
        RH = calculate_pull_up_resistance(
            pull_down_resistance=RL,
            reference_voltage=Vref,
            output_voltage=Vo
        )
        
        print(f"计算得到的上拉电阻 RH 值为: {RH.normalize()} 欧姆")
        
    except Exception as e:
        print(f"计算过程中发生错误: {str(e)}")