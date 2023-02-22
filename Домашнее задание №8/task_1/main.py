import csv
import re


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = ['Изготовитель системы', 'Название ОС', 'Код продукта',
                 'Тип системы']
    for i in range(3):
        with open(f"info_{i + 1}.txt") as info:
            data = info.read()
            os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
            os_name_reg = re.compile(r'Название ОС:\s*\S*\s*\S*\s*\S*')
            os_code_reg = re.compile(r'Код продукта:\s*\S*')
            os_type_reg = re.compile(r'Тип системы:\s*\S*')
            os_name = f'{os_name_reg.findall(data)[0].split()[2]} ' \
                      f'{os_name_reg.findall(data)[0].split()[3]} ' \
                      f'{os_name_reg.findall(data)[0].split()[4]}'
            os_prod = os_prod_reg.findall(data)[0].split()[2]
            os_code = os_code_reg.findall(data)[0].split()[2]
            os_type = os_type_reg.findall(data)[0].split()[2]
            os_prod_list.append(os_prod)
            os_name_list.append(os_name)
            os_code_list.append(os_code)
            os_type_list.append(os_type)

            with open(f"main_data_{i + 1}.txt", 'w', encoding='utf-8') as obj:
                data_list = [os_prod, os_name,
                             os_code, os_type]
                obj.writelines(data_list)

    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта',
                  'Тип системы'], os_prod_list, os_name_list, os_code_list,
                 os_type_list]
    return main_data


def write_to_csv():
    data = get_data()
    with open("data_report.csv", 'w', encoding='utf-8') as final_file:
        final_file_wr = csv.writer(final_file)
        for row in data:
            final_file_wr.writerow(row)


write_to_csv()
