# ========================
# Import libraries
# ========================
import numpy as np
import matplotlib.pyplot as plt

# ========================
# 1️⃣ إعداد المدينة بشكل تفاعلي
# ========================
# يمكنك تعديل هذه القيم
city = {
    "house1": {"area": 100, "population": 4},
    "house2": {"area": 80, "population": 3},
    "house3": {"area": 120, "population": 5}
}

# ========================
# 2️⃣ إعداد العشوائية
# ========================
np.random.seed(123)  # لضمان تكرار نفس النتائج

# ========================
# 3️⃣ إحصاءات المساحات
# ========================
areas = [info["area"] for info in city.values()]
print("متوسط المساحة:", np.mean(areas))
print("الوسيط:", np.median(areas))
print("الانحراف المعياري:", np.std(areas))

# ========================
# 4️⃣ إنشاء قائمة السكان
# ========================
people_houses = []
for house, info in city.items():
    people_houses.extend([house] * info["population"])

total_people = len(people_houses)
print("إجمالي السكان:", total_people)

# ========================
# 5️⃣ محاكاة الحركة العشوائية لكل شخص
# ========================
num_steps = 100   # عدد الخطوات لكل شخص
min_jump = 1      # أقل قفزة عند النرد 6
max_jump = 6      # أعلى قفزة عند النرد 6

all_walks = []

for person_house in people_houses:
    random_walk = [0]  # البداية من صفر
    for _ in range(num_steps):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        
        if dice <= 2:
            step = max(0, step - 1)  # خطوة للخلف، لا تقل عن صفر
        elif dice <= 5:
            step = step + 1          # خطوة للأمام
        else:
            step = step + np.random.randint(min_jump, max_jump + 1)  # قفزة عشوائية
        
        random_walk.append(step)
    all_walks.append(random_walk)

# ========================
# 6️⃣ تحويل القوائم إلى مصفوفة NumPy للرسم والتحليل
# ========================
np_aw = np.array(all_walks)         # كل صف = شخص
np_aw_t = np.transpose(np_aw)       # كل صف = خطوة معينة لكل الأشخاص

# ========================
# 7️⃣ رسم المسارات لأول 10 أشخاص
# ========================
plt.figure(figsize=(10,5))
plt.plot(np_aw_t[:, :10])
plt.xlabel("Step")
plt.ylabel("Position")
plt.title("Random Walk of 10 People in the City")
plt.show()

# ========================
# 8️⃣ رسم توزيع المواقع النهائية لكل الأشخاص
# ========================
ends = np_aw_t[-1, :]
plt.figure(figsize=(8,4))
plt.hist(ends, bins=20, color='skyblue', edgecolor='black')
plt.xlabel("Final Position")
plt.ylabel("Number of People")
plt.title("Distribution of Final Positions of All People")
plt.show()

# ========================
# 9️⃣ ملخص نصي لكل بيت
# ========================
for house, info in city.items():
    print(f"{house} population: {info['population']}, area: {info['area']}")
print(f"Total people: {total_people}")
print(f"Average final position: {np.mean(ends):.2f}")
print(f"Max final position: {np.max(ends)}")
