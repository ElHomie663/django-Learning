from datetime import datetime

fecha = datetime(2026, 7, 4)
fecha2 = datetime(2026, 4, 7, 12, 30, 45)


fechastr = datetime.strptime("2026-07-04", "%Y-%m-%d")

print(fechastr.strftime("%Y-%m-%d"))
print(fecha > fecha2)

print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.hour,
)
