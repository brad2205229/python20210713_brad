# 請印出 employee 的所有資料(含欄位名稱)
import sqlite3
conn = sqlite3.connect('emp.db')
cursor = conn.cursor()

# 查詢 Table META-INFO
cursor.execute('PRAGMA TABLE_INFO({})'.format('employees'))
headers = cursor.fetchall()
names = [header[1] for header in headers]
# 列出欄位名稱
for name in names:
    print(name, end='\t')

print('\n------------------------------------------------------------------')

# 多筆查詢 sql 語句
sql = 'SELECT  emp_id, dept_id, emp_name, emp_salary, create_date FROM employees'
cursor.execute(sql)
emps = cursor.fetchall()
for emp in emps:
    print('%-7d\t%-7d\t%-8s\t%-10d\t%s' % (emp[0], emp[1], emp[2], emp[3], emp[4]))
print('------------------------------------------------------------------')