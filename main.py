minutes =int(input("введите количество минут: "))
hours = minutes // 60
remaining_minutes = minutes % 60
print(f"{minutes} минут - это {hours} часов и {remaining_minutes} минут.")
