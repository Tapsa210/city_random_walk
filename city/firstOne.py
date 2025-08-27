import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

# بيانات المنازل
city = {
    "house1": {"area": 100, "population": 4},
    "house2": {"area": 80, "population": 3},
    "house3": {"area": 120, "population": 5}
}

# استخراج المساحات
areas = [city[h]["area"] for h in city]

# إحصائيات
print("متوسط المساحة:", np.mean(areas))
print("الوسيط:", np.median(areas))
print("الانحراف المعياري:", np.std(areas))

# المشي العشوائي
random_walk = [0]

for i in range(100):
    step = random_walk[-1]   # آخر موقع
    dice = np.random.randint(1, 7)  # نرد

    if dice <= 3:
        step = max(0, step - 1)  # للخلف
    elif dice <= 5:
        step = step + 1          # للأمام
    else:
        step = step + np.random.randint(1, 7)  # قفزة عشوائية

    random_walk.append(step)

# نطبع جزء من المسار
print(random_walk[:20])  # أول 20 خطوة

# نرسم المسار
plt.plot(random_walk)
plt.title("Random Walk Simulation")
plt.xlabel("Number of Steps")
plt.ylabel("Position")
plt.show()




