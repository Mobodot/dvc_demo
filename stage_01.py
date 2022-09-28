STAGE_NAME = "one"

line = f'This is coming from stage: {STAGE_NAME}'

with open("one.txt", "w") as f:
    f.write(line)
    
print(f"This is coming from stage: {STAGE_NAME}")
