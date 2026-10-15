'''CuteCat CuteFox'''
def main():
    '''CuteCat CuteFox'''
    n = int(input())
    cats = {}
    foxes = {}

    for _ in range(n):
        line = input()
        if not line or ":" not in line:
            continue

        key, value = line.split(":", 1)
        name = key.strip(" '\"{}")
        code = value.strip(" '\"{}")

        # เก็บข้อมูลโดยใช้ (เลขรหัสแบบ int, รหัสเดิม) เป็น Key ใน Dict
        if "Cat" in code:
            num = int(code.replace("Cat", ""))
            cats[(num, code)] = name
        elif "Fox" in code:
            num = int(code.replace("Fox", ""))
            foxes[(num, code)] = name

    # ตรวจสอบ Default (เช็คจากค่า code ในคีย์ของ Dict)
    if not any(code == "Cat01" for _, code in cats):
        cats[(1, "Cat01")] = "Garfield"
    if not any(code == "Fox01" for _, code in foxes):
        foxes[(1, "Fox01")] = "Fubuki"

    print(f"Cat : {len(cats)}")
    print(f"Fox : {len(foxes)}")

    # Python จะเรียง Tuple (num, code) ตาม num ก่อนโดยอัตโนมัติ ไม่ต้องใช้ key
    for num, code in sorted(cats):
        print(f"{cats[(num, code)]} : {code}")

    for num, code in sorted(foxes):
        print(f"{foxes[(num, code)]} : {code}")

main()
