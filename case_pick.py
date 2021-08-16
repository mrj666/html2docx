
import re
import xlrd

case_data = 'auto_test_list'

table = xlrd.open_workbook(case_data)  # read excel value
sutable = table.sheet_by_name('SU')

mcs_list = [0, 1, 9]
dcm_list = [0, 1]
he_list = [0, 1, 2]
gi_list = [0, 1, 3]

mcs_col = 0  # line A means 0
dcm_col = 1
he_col = 2
gi_col = 3

table_lines = 200
for mcs in mcs_list:
    for dcm in dcm_list:
        for he in he_list:
            for gi in gi_list:
                for line in range(0, table_lines):
                    tmp_mcs = sutable.cell_value(table_lines, mcs_col)
                    if str(mcs) == tmp_mcs:
                        tmp_dcm = sutable.cell_value(table_lines, dcm_col)
                        if str(dcm) == tmp_dcm:
                            tmp_he = sutable.cell_value(table_lines, he_col)
                            if str(he) == tmp_he:
                                tmp_gi = sutable.cell_value(table_lines, gi_col)
                                if str(gi) == tmp_gi:
                                    print(str(mcs) + str(dcm) + str(he) + str(gi) + '\tin line: ' + table_lines)
                                    continue
