R1 = float(input("Радіус першої планети:"))
T1 = float(input("Період обертання першої планети:"))
R2 = float(input("Радіус другої планети:"))
T2 = ((T1*T1*R2*R2*R2)/(R1*R1*R1))**0.5
print(T2)
