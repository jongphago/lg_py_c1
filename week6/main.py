light = "green"

# condition = light == "green"
# print(type(condition))
# print(condition)

if light == "green":
    print(f"light: {light}")
    print("건너세요.")
    pass

elif light == "yellow":
    print(f"light: {light}")
    print("건너지 마세요.")

elif light == "purple":
    print(f"light: {light}")
    print("건너지 마세요.")

else:
    print(f"light: {light}")
    print("건너지 마세요.")

print("함수 종료")
