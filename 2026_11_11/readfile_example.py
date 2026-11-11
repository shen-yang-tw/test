from pathlib import Path


folder = Path(__file__).parent
sample_path = folder / "sample.txt"
output_path = folder / "output.txt"

with open(sample_path, "r", encoding="utf-8") as file:
    content = file.read()

print("讀取到的內容：")
print(content)

with open(output_path, "w", encoding="utf-8") as file:
    file.write("這是新寫入的第一行。\n")

with open(output_path, "a", encoding="utf-8") as file:
    file.write("這一行是追加上去的。\n")

print(f"已將寫入與追加的示範結果存到：{output_path}")
