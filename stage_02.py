STAGE_NAME = "two"

line = f"This is coming from stage: {STAGE_NAME}"

with open("two.txt", "w") as f:
    f.write(line)
    
with open("one.txt", "r") as f:
    contents = f.read()
    
print(f"contents contains: [{contents}]")