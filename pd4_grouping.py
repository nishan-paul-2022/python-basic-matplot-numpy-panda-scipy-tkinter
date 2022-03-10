import pandas as pd
import numpy as np


def fst():
    data = {'Name': ['Jai', 'Anuj', 'Jai', 'Princi', 'Gaurav', 'Anuj', 'Princi', 'Abhi'],
            'Age': [27, 24, 22, 32, 33, 36, 27, 32],
            'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj', 'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],
            'Qualification': ['Msc', 'MA', 'MCA', 'Phd', 'B.Tech', 'B.com', 'Msc', 'MA'],
            'Score': [23, 34, 35, 45, 47, 50, 52, 53]}

    df = pd.DataFrame(data)

    for key, value in df.iteritems():
        print(key, '\n', value, end='\n\n')

    for i in df.itertuples():
        print(i)

    name = df.groupby('Name')
    sc = lambda x: (x - x.mean()) / x.std() * 10

    grp = name.groups
    grp2 = df.groupby(['Name', 'Qualification']).groups
    jai = name.get_group('Jai')
    sm = df['Age'].groupby(df['Name']).sum()
    mul = name.agg([np.sum, np.mean, np.std])
    score = name.transform(sc)
    fil = name.filter(lambda x: len(x) <= 1)

    print('\n\nname.groups\n', grp)
    print('\n\ndf.groupby(["Name", "Qualification"]).groups\n', grp2)
    print('\n\nname.get_group("Jai")\n', jai)
    print('\n\ndf["Age"].groupby(df["Name"]).sum()\n', sm)
    print('\n\nname.agg([np.sum, np.mean, np.std])\n', mul)
    print('\n\nname.transform(sc)\n', score)
    print('\n\nname.filter(lambda x: len(x) <= 1)\n', fil)


def sec():
    dict = {
        'ID': [1, 2, 3],
        'Movies': ['The Godfather', 'Fight Club', 'Casablanca'],
        'Week_1_Viewers': [30, 30, 40],
        'Week_2_Viewers': [60, 40, 80],
        'Week_3_Viewers': [40, 20, 20]}

    df = pd.DataFrame(dict)
    print(df, end='\n\n')

    groupby_dict = {'Week_1_Viewers': 'Total_Viewers',
                    'Week_2_Viewers': 'Total_Viewers',
                    'Week_3_Viewers': 'Total_Viewers',
                    'Movies': 'Movies'}

    df = df.set_index('ID')
    df = df.groupby(groupby_dict, axis=1).sum()
    print(df, end='\n\n')


fst()
sec()

# https://www.geeksforgeeks.org/pandas-groupby/
# https://www.geeksforgeeks.org/grouping-rows-in-pandas/
# https://www.geeksforgeeks.org/combining-multiple-columns-in-pandas-groupby-with-dictionary/
