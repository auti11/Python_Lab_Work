data_dic = {
    'V': 10,
    'VI': 10,
    'VII': 40,
    'VIII': 20,
    'IX': 70,
    'X': 80,
    'XI': 40,
    'XII': 20
}
frequency_dic = {}
for key in data_dic:
    value = data_dic[key]
    if value in frequency_dic:
        frequency_dic[value] += 1
    else:
        frequency_dic[value] = 1
print(frequency_dic)