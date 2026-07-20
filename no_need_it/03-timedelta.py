from datetime import datetime, timedelta

fecha1 = datetime(2026, 7, 4)
fecha2 = datetime(2026, 4, 7)

delta = fecha2 - fecha1
print(delta)

print("dias", delta.days)
