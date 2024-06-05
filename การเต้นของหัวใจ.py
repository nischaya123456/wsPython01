# โจทย์ 1

#รับค่าอายุ
age = int(input("อายุ: "))

# คำนวนอัตตราเต้นของหัวใจสูงสุด (mhr)
mhr = 220 - age

# คำนวนขอบเขตของ zone 2
zone2min = 0.60 * mhr
zone2mix = 0.70 * mhr

# แสดงผลลัพธ์
print("ค่า mhr :", mhr)
print("อัตตราเต้นของหัวใจสูงสุดที่เหมาะสม")
print("ค่าต่ำสุดของ zone 2:", zone2min)
print("ค่าสูงสุดของ zone 2:", zone2mix)
