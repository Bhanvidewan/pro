import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred=credentials.Certificate('prosc-87c7d-firebase-adminsdk-ar1cv-7352968967.json')

firebase_admin.initialize_app(cred)


db=firestore.client()

import xlrd
loc = (r'info.xlsx')
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

for i in range(sheet.ncols):
    if sheet.col_values(i)[0]=="Employee Name":
        users = sheet.col_values(i)[1:]
    elif sheet.col_values(i)[0]== "users_Login Id":
        users_login_id = sheet.col_values(i)[1:]
    elif sheet.col_values(i)[0]== "employee_mobile":
        employee_mobile = list(map(int, sheet.col_values(i)[1:]))
    elif sheet.col_values(i)[0]== "Department":
        department = sheet.col_values(i)[1:]
    elif sheet.col_values(i)[0]== "Project_id":
        proid = sheet.col_values(i)[1:]


for user in range(len(users)):
  x=user+1
  doc_ref = db.collection(u'users').document(str(x))
  doc_ref.set({
    u'Employee_Name': users[user],
    u'Employee_Id': x,
    u'Employee_PhoneNo': employee_mobile[user],
    u'Department': u'CSE',
    u'EmailID': users_login_id[user],
      u'emailnotifications':u'false',
    u'Project_Id':  proid[user],
    })


sheet2 = wb.sheet_by_index(1)

for i in range(sheet2.ncols):
    if sheet2.col_values(i)[0]=="Project_Id":
        Id = sheet2.col_values(i)[1:]
    elif sheet2.col_values(i)[0]== "Project_Name":
        namep = sheet2.col_values(i)[1:]
    elif sheet2.col_values(i)[0]== "Description":
        desc = sheet2.col_values(i)[1:]
    elif sheet2.col_values(i)[0]== "Status":
        status = sheet2.col_values(i)[1:]


for proj in range(len(namep)):
  doc_ref1 = db.collection(u'projects').document(namep[proj])
  doc_ref1.set({
    u'Project_Name': namep[proj],
    u'Project_Id': Id[proj],
    u'Description': desc[proj],
    u'Status': status[proj],
    })


