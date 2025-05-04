Gallon = 3.785411784  # 리터
Mile = 1.609344  # 키로미터

milePerGallon = float(input())

huneredKmPerLiter = 100 / (milePerGallon * (Mile / Gallon))

print(f"{huneredKmPerLiter:6f}")
