import sql_functions as sqlf
import numpy as np
import csv_functions as csvf

the_data = np.array([[45658, 'gehkj ', -1234.56], [34, 'ytb', 46.45]])

the_data2 = np.array([45658, 'geh, kj ', -1234.56])

the_data3 = np.array([])

the_data4 = np.array([[466, 'm,cv', -934.09], [34, 'ytb', 4534], [65, 'rg']])

'''try:
    print(sqlf.append_row('dev_test', 'test_table', the_data2))
except Exception as e:
    print(e)'''

'''try:
    print(sqlf.clear_data('dev_test', 'test_table'))
except Exception as e:
    print(e)'''

try:
    print(sqlf.save_data('dev_test', 'test_table', the_data))
except Exception as e:
    print(e)

print(sqlf.get_data('dev_test', 'test_table'))

filename = 'test.csv'
row = [0, 1, 'ds,d', 3, 4, -1, 5, 6, 7, 8, 9]
row2 = [[0, 1, 'ds,d ', 3, 4, -1, 5, 6, 7, 8, 9],[2, 4]]
row3 = [34, 'dfg, g ', -45.56]
row4 = [3, 4, 5]

'''try:
    csvf.append_row(filename, row4)
except Exception as e:
    print(e)'''

#print(csvf.clear_data(filename))

'''try:
    csvf.save_data(filename, the_data)
except Exception as e:
    print(e)'''

#print(csvf.get_data(filename))
