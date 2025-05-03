Gallon = 3.785411784  # 리터
Mile = 1.609344  # 키로미터

gallonPerMile = float(input())

hundredKmPerLiter = 100 / (gallonPerMile * (Mile / Gallon))

print(f"{hundredKmPerLiter:6f}")
