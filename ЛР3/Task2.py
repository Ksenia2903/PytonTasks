# TODO Напишите функцию find_common_participants
def find_common_participants (str_1, str_2, smb='|'):
    list_1 =str_1.split(smb)
    list_2 = str_2.split(smb)
    return list(set(list_1)&(set(list_2)))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common = find_common_participants(participants_first_group, participants_second_group, '|')
common.sort()
print(common)