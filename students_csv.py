
import pandas as pd
import json

# 1. 读取CSV
df = pd.read_csv("students.csv")

# 2. 统计
total = len(df)
by_country = df['country'].value_counts().to_dict()
completed = len(df[df['bet_status'] == 'completed'])
rate = round(completed / total * 100, 1)

# 3. 打印看看
print(f"总人数: {total}")
print(f"各国家人数: {by_country}")
print(f"对赌完成率: {rate}%")

# 4. 保存成JSON
report = {
    "total": total,
    "by_country": by_country,
    "completion_rate": f"{rate}%"
}

with open("report.json", "w") as f:
    json.dump(report, f, indent=4)

print("✅ report.json 已生成！")