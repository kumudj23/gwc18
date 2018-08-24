import medal_of_honor
import matplotlib.pyplot as plt
import numpy as np
exclude = -1
list_of_years = []
check = []

list_of_awardee = medal_of_honor.get_awardees()

for i in range(len(list_of_awardee)):
    answer = list_of_awardee[i]["awarded"]["date"]["year"]
    if answer == exclude or answer < 1800:
        continue
    else:
        list_of_years.append(answer)



#print (check)

fig = plt.figure()

x_labels = ['Mexican American(1846-48)', 'Civil War 1861-65', 'spanish-american (1898)', 'WW1 (1914-1918)', 'WW2 (1939-45)', 'Korean war (1950-53)', 'Vietnam War (1959-75)', 'Gulf War(1990-91)']
x = len(x_labels)
#
y_labels = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
y = len(y_labels)


width = 1.5
plt.bar(x_labels, y_labels, color = "violet")


plt.ylabel('number of medals awarded')
plt.title('number of medals awarded by war period (after civil war)')
plt.xticks(range(8), x_labels, color = "black")
plt.yticks(range(16), y_labels, color = "black")

#plt.legend((p1[0], p2[0]), ('Men', 'Women'))

# for year in list_of_years:
#     if year <1848:
#

plt.show()
