# Claude Camp W3 Projects

## 项目概览

本仓库包含 3 个 Python 练习项目，涵盖数据分析、文件读写、字符串处理与单元测试。每个项目都在独立的 Git 分支上开发，完成后合并回 main 分支。

---

## Git 分支结构

```
main
├── project-1-csv-analyzer
├── project-2-json-config
└── project-3-string-utils
```

---

## 项目 1：CSV 学员数据分析器

### 功能
- 读取学员 CSV 文件（含姓名、邮箱、加入日期、国家、对赌状态）
- 统计总人数、各国家人数、对赌完成率
- 把统计结果保存为 `report.json`
- 使用 Pandas 实现，不用手写 for 循环

### 文件
- `students_csv.py` - 主程序
- `students.csv` - 学员假数据（20行）
- `report.json` - 统计结果输出

### 运行方式
```bash
pip install pandas
python students_csv.py
```

### 输出示例
```
总人数: 20
各国家人数: {'Singapore': 6, 'Australia': 5, 'China': 5, 'Malaysia': 4}
对赌完成率: 60.0%
✅ report.json 已生成！
```

### 开发思路
- 用 `pd.read_csv()` 一行读取整个 CSV，不需要手动解析
- `len(df)` 统计总人数，标题行不算在内
- `df['country'].value_counts().to_dict()` 统计各国人数，`.to_dict()` 是因为 JSON 不认识 Pandas 的 Series 格式，需要先转成字典
- `df[df['bet_status'] == 'completed']` 筛选出完成的学员，外层 `df[]` 根据 True/False 列表过滤行

---

## 项目 2：JSON 配置文件读写器

### 功能
- 读取 `config.json` 显示当前设置
- 数字菜单让用户选择修改哪个设置
- 数据验证：
  - 主题只能是 `dark` 或 `light`
  - 语言只能是 `zh` 或 `en`
  - 字体大小必须在 8-32 之间
- 修改后保存回 `config.json`
- `while True` 循环，可以连续修改直到输入 4 退出

### 文件
- `config_editor.py` - 主程序
- `config.json` - 配置文件

### 运行方式
```bash
python config_editor.py
```

### 操作示例
```
当前设置：
  theme: dark
  language: zh
  font_size: 14

1. 修改主题 (theme)
2. 修改语言 (language)
3. 修改字体大小 (font_size)
4. 退出

请选择 (1-4): 1
新的值是？light
✅ theme 已更新为 light！
```

### 开发思路
- 用 `def` 把每个功能分开：`load_config()`、`save_config()`、`show_config()`、`validate()`，让代码结构清晰
- `validate()` 返回 `None` 表示验证失败，返回值表示验证通过，`main()` 根据是否 `None` 决定要不要保存
- `while True` 配合 `break`（退出）和 `continue`（重新选择），实现连续操作
- `if __name__ == "__main__"` 确保只有直接运行才执行 `main()`，被其他文件 import 时不会自动运行

---

## 项目 3：带单元测试的字符串工具库

### 功能

#### `reverse_words(s)` - 反转单词顺序
- 支持标点符号单独分离（使用正则表达式）
- `"hello world"` → `"world hello"`
- `"world hello!!!"` → `"!!! hello world"`

#### `count_vowels(s)` - 统计元音字母数量
- 支持大小写
- `"hello"` → `2`
- `"APPLE"` → `2`

#### `is_palindrome(s)` - 判断是否回文
- 忽略空格和大小写
- `"racecar"` → `True`
- `"race car"` → `True`
- `"hello"` → `False`

### 文件
- `string_utils.py` - 工具函数
- `test_string_utils.py` - 单元测试（11个测试用例）

### 运行方式
```bash
python string_utils.py
```

### 测试方式
```bash
pip install pytest
python -m pytest test_string_utils.py
```

### 测试结果
```
collected 11 items
11 passed in 0.02s
```

### 开发思路
- `reverse_words` 最初用 `split()` 按空格切割，但标点会跟着单词走（`"hello!!!"` 不会分开）。后来改用正则表达式 `re.findall(r"[a-zA-Z]+|[^a-zA-Z\s]+", s)`，把单词和标点分别找出来，空格忽略
- `count_vowels` 用 `for` 循环遍历每个字母，判断是否在 `"aeiouAEIOU"` 里
- `is_palindrome` 先用 `.replace(" ", "")` 删掉空格，`.lower()` 统一小写，再用 `s == s[::-1]` 判断正反是否一样，直接 `return` 比较结果，不需要额外 `if`
- 测试文件用 `assert` 断言，pytest 自动找所有 `test_` 开头的函数运行

---

## 环境要求
- Python 3.x
- pandas (`pip install pandas`)
- pytest (`pip install pytest`)
