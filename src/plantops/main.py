"""解析设备温度并返回可序列化记录。"""

import json
import math
import re


def parse_reading(text):
    """将 DEV-01:78.5 转为字典，显式拒绝无效编号和非有限温度。"""
    device_id, raw_value = text.strip().split(":", maxsplit=1)
    if not re.fullmatch(r"DEV-\d{2}", device_id):
        raise ValueError("设备编号应为 DEV-加两位数字")
    value = float(raw_value)
    if not math.isfinite(value):
        raise ValueError("温度必须有限")
    return {"device_id": device_id, "temperature": value, "unit": "°C"}


def main():
    """执行一次最小业务闭环。"""
    reading = parse_reading("DEV-01:78.5")
    print(json.dumps(reading, ensure_ascii=False))


if __name__ == "__main__":
    main()
