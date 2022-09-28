STAGE_NAME = "three"

line = f"This is coming from stage: {STAGE_NAME}"

with open("one.txt", "r") as f:
    contents1 = f.read()
    
with open("two.txt", "r") as f:
    contents2 = f.read()

with open("three.txt", "w") as f:
    f.write(line)
    
print(line)