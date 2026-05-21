import json

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def save_config(config):
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)

def show_config(config):
    print("\n当前设置：")
    for key, value in config.items():
        print(f"  {key}: {value}")

def validate(key, value):
    if key == "font_size":
        value = int(value)
        if value < 8 or value > 32:
            print("❌ 字体大小必须在 8-32 之间！")
            return None
    
    elif key == "theme":
        if value not in ["dark", "light"]:
            print("❌ 主题只能是 dark 或 light！")
            return None
    
    elif key == "language":
        if value not in ["zh", "en"]:
            print("❌ 语言只能是 zh 或 en！")
            return None
    
    return value

def main():
    config = load_config()
    while True:
        show_config(config)
        
        print("\n1. 修改主题 (theme)")
        print("2. 修改语言 (language)")
        print("3. 修改字体大小 (font_size)")
        print("4. 退出")
            
        choice = input("\n请选择 (1-4): ")


        if choice == "1":
            key = "theme"
        elif choice == "2":
            key = "language"
        elif choice == "3":
            key = "font_size"
        elif choice == "4":
            print("👋 退出！")
            break
        else:
            print("❌ 请输入 1-4！")
            continue

        value = input("新的值是？")
        value = validate(key, value)

        if value is not None:
            config[key] = value
            save_config(config)
            print(f"✅ {key} 已更新为 {value}！")

if __name__ == "__main__":
    main()