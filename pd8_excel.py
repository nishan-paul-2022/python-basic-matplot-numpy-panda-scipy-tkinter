import pandas as pd


def fst():
    df = pd.DataFrame({'Data': ['Geeks', 'For', 'geeks', 'is', 'portal', 'for', 'geeks']})
    writer = pd.ExcelWriter('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/pd8_single.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()


def sec():
    df1 = pd.DataFrame({'Data': [11, 12, 13, 14]})
    df2 = pd.DataFrame({'Data': [21, 22, 23, 24]})
    df3 = pd.DataFrame({'Data': [31, 32, 33, 34]})

    writer = pd.ExcelWriter('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/pd8_multisheet.xlsx', engine='xlsxwriter')

    # Write each dataframe to a different worksheet.
    df1.to_excel(writer, sheet_name='Sheet1')
    df2.to_excel(writer, sheet_name='Sheet2')
    df3.to_excel(writer, sheet_name='Sheet3')
    writer.save()


def thrd():
    df1 = pd.DataFrame({'Data': [11, 12, 13, 14]})
    df2 = pd.DataFrame({'Data': [21, 22, 23, 24]})
    df3 = pd.DataFrame({'Data': [31, 32, 33, 34]})
    df4 = pd.DataFrame({'Data': [41, 42, 43, 44]})

    writer = pd.ExcelWriter('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/pd8_multiple.xlsx', engine='xlsxwriter')

    # write and Positioning the dataframes in the worksheet (default position, cell A1)
    df1.to_excel(writer, sheet_name='Sheet1')
    df2.to_excel(writer, sheet_name='Sheet1', startcol=3)
    df3.to_excel(writer, sheet_name='Sheet1', startrow=6)
    df4.to_excel(writer, sheet_name='Sheet1', startrow=7, startcol=4, header=False, index=False)  # It is also possible to write the dataframe without the header and index.
    writer.save()


def forth():
    dataframe = pd.DataFrame({
        'Marks (Out of 50)': [30, 40, 45, 15, 8, 5, 35],
        'Percentage': [.6, .8, .9, .3, .16, .1, .7], })

    writer_object = pd.ExcelWriter('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/pd8_column.xlsx', engine='xlsxwriter')
    dataframe.to_excel(writer_object, sheet_name='Sheet1')
    workbook_object = writer_object.book
    worksheet_object = writer_object.sheets['Sheet1']
    format_object1 = workbook_object.add_format({'num_format': '# 0.00'})
    format_object2 = workbook_object.add_format({'num_format': '0 %'})
    worksheet_object.set_column('B:B', 20, format_object1)
    worksheet_object.set_column('C:C', 15, format_object2)
    writer_object.save()


def fifth():
    dataframe = pd.DataFrame({
        'Subject': ['Math', 'Physics', 'Computer', 'Hindi', 'English', 'chemistry'],
        'Mid Exam Score': [95, 78, 80, 80, 60, 95],
        'End Exam Score': [90, 67, 78, 70, 63, 90]
    })

    writer_object = pd.ExcelWriter('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/pd8_line_chart.xlsx', engine='xlsxwriter')
    dataframe.to_excel(writer_object, sheet_name='Sheet1')
    workbook_object = writer_object.book
    worksheet_object = writer_object.sheets['Sheet1']
    worksheet_object.set_column('B:C', 20)
    chart_object = workbook_object.add_chart({'type': 'line'})

    chart_object.add_series({
        'name': ['Sheet1', 0, 2],
        'categories': ['Sheet1', 1, 3, 6, 3],
        'values': ['Sheet1', 1, 2, 6, 2],
    })

    chart_object.add_series({
        'name': ['Sheet1', 0, 1],
        'categories': ['Sheet1', 1, 3, 6, 3],
        'values': ['Sheet1', 1, 1, 6, 1],
    })

    chart_object.set_title({'name': 'Exam Score Distribution'})
    chart_object.set_x_axis({'name': 'Subjects'})
    chart_object.set_y_axis({'name': 'Marks'})
    worksheet_object.insert_chart('E2', chart_object, {'x_offset': 20, 'y_offset': 5})
    writer_object.save()


def sixth():
    dataframe = pd.DataFrame({
        'Subject': ['Math', 'Physics', 'Computer', 'Hindi', 'English', 'chemistry'],
        'Mid Exam Score': [90, 78, 60, 80, 60, 90],
        'End Exam Score': [45, 39, 30, 40, 30, 60]})

    writer_object = pd.ExcelWriter('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/pd8_column_chart.xlsx', engine='xlsxwriter')  # Create a Pandas Excel writer object using XlsxWriter as the engine.
    dataframe.to_excel(writer_object, sheet_name='Sheet1')  # Write a dataframe to the worksheet.
    workbook_object = writer_object.book  # Create xlsxwriter workbook object .
    worksheet_object = writer_object.sheets['Sheet1']  # Create xlsxwriter worksheet object
    worksheet_object.set_column('B:C', 20)  # set width of the B and C column

    chart_object = workbook_object.add_chart({'type': 'column'})  # Create a chart object that can be added to a worksheet using add_chart() method.

    # Add a data series to a chart using add_series method.

    # Configure the first series | syntax to define ranges is: [sheetname, first_row, first_col, last_row, last_col].
    chart_object.add_series({
        'name': ['Sheet1', 0, 2],
        'categories': ['Sheet1', 1, 3, 6, 3],
        'values': ['Sheet1', 1, 2, 6, 2],
    })

    # Configure a second series
    chart_object.add_series({
        'name': ['Sheet1', 0, 1],
        'categories': ['Sheet1', 1, 3, 6, 3],
        'values': ['Sheet1', 1, 1, 6, 1],
    })

    chart_object.set_title({'name': 'Exam Score Distribution'})  # Add a chart title.
    chart_object.set_x_axis({'name': 'Subjects'})  # Add x-axis label
    chart_object.set_y_axis({'name': 'Marks'})  # Add y-axis label
    worksheet_object.insert_chart('E2', chart_object, {'x_offset': 20, 'y_offset': 5})  # add chart to the worksheet with given offset values at the top-left corner of a chart is anchored to cell E2
    writer_object.save()  # Close the Pandas Excel writer object and output the Excel E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter.


def read_xl():
    df = pd.read_excel('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/pd8_multisheet.xlsx', sheet_name=[0, 1])
    print(df, end='\n\n')
    df = pd.read_excel('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/pd8_multisheet.xlsx')
    print(df, end='\n\n')


fst()
sec()
thrd()
forth()
fifth()
sixth()
read_xl()

# https://www.geeksforgeeks.org/python-working-with-pandas-and-xlsxwriter-set-1/
# https://www.geeksforgeeks.org/python-working-with-pandas-and-xlsxwriter-set-2/
# https://www.geeksforgeeks.org/python-working-with-pandas-and-xlsxwriter-set-3/
# https://www.geeksforgeeks.org/creating-a-dataframe-using-excel-files/