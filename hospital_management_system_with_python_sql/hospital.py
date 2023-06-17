from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hostpital:
    def __init__(self,root):
        self.root = root
        self.root.title('Hospital Management System')
        self.root.geometry('1350x750+0+0')

        self.Nameoftablets = StringVar()
        self.ref=StringVar()
        self.Dose= StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEffect = StringVar()
        self.furthurInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowtoUseMedication = StringVar()
        self.PatientId = StringVar()
        self.NhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateofBirth = StringVar()
        self.PatientAddress = StringVar()
      




        lbtitle = Label(self.root, bd=20,relief=RIDGE, text='HOSPITAL MANAGEMENT SYSTEM',
                        fg='red', bg='white', font=('times new roman',30,'bold'))
        lbtitle.pack(side=TOP, fill=X)

        ####################################### DataFrame ################################################

        DataFrame = Frame(self.root, bd=20, relief=RIDGE)
        DataFrame.place(x=0, y=110, width=1350, height=350)

        DataFrameLeft = LabelFrame(DataFrame, bd=10, padx=20, relief=RIDGE,
                                   font=('arial',12,'bold'),text='Patient Information')
        DataFrameLeft.place(x=0, y=5, width=950, height=340)

        DataFrameRight = LabelFrame(DataFrame, bd=10, padx=5, relief=RIDGE,
                                   font=('arial',12,'bold'),text='Prescription')
        DataFrameRight.place(x=960, y=5, width=350, height=340)

        ############################################ Buttons Frame ##########################################

        ButtonFrame = Frame(self.root, bd=20, relief=RIDGE)
        ButtonFrame.place(x=0, y=465, width=1350, height=70)

        ############################################ Details Frame ##########################################

        DetailsFrame = Frame(self.root, bd=20, relief=RIDGE)
        DetailsFrame.place(x=0, y=530, width=1350, height=210)

        ############################################# DataFrameLeft #######################################
        lblNameTablet = Label(DataFrameLeft, text='Name of Tablet', font=('times new roman', 12, 'bold'),
                              padx=2, pady=6)
        lblNameTablet.grid(row=0,column=0)
        comNameTablet = ttk.Combobox(DataFrameLeft, state='readonly',
                                     font=('aerial',12, 'bold'),width=25)
        comNameTablet['values'] = ('Nice','Corona Vaccine', 'Paracetamol', 'Adderall', 'Ativan','Amlodiphine')
        comNameTablet.current(0)
        comNameTablet.grid(row=0, column=1,padx=6)

        referenceNumber = Label(DataFrameLeft, text='Reference No:', font=('times new roman', 12, 'bold'),
                                padx=2, pady=6)
        referenceNumber.grid(row=1,column=0,sticky=W)
        referenceNumberEntry = Entry(DataFrameLeft,font=('times new roman', 12, 'bold'),width=26)
        referenceNumberEntry.grid(row=1,column=1)

        dose = Label(DataFrameLeft, text='Dose', font=('times new roman', 12, 'bold'),
                                padx=2, pady=6)
        dose.grid(row=2,column=0,sticky=W)
        doseEntry = Entry(DataFrameLeft,font=('times new roman', 12, 'bold'),width=26)
        doseEntry.grid(row=2,column=1)

        nooftablets = Label(DataFrameLeft, text='No. of Tablets', font=('times new roman', 12, 'bold'),
                                padx=2, pady=6)
        nooftablets.grid(row=3,column=0,sticky=W)
        nooftabletsEntry = Entry(DataFrameLeft,font=('times new roman', 12, 'bold'),width=26)
        nooftabletsEntry.grid(row=3,column=1)

        lot = Label(DataFrameLeft, text='Lot', font=('times new roman', 12, 'bold'),
                                padx=2, pady=6)
        lot.grid(row=4,column=0,sticky=W)
        lotEntry = Entry(DataFrameLeft,font=('times new roman', 12, 'bold'),width=26)
        lotEntry.grid(row=4,column=1)

        issueDate = Label(DataFrameLeft, text='Issue Date', font=('times new roman', 12, 'bold'),
                                padx=2, pady=6)
        issueDate.grid(row=5,column=0,sticky=W)
        issueDateEntry = Entry(DataFrameLeft,font=('times new roman', 12, 'bold'),width=26)
        issueDateEntry.grid(row=5,column=1)

        expDate = Label(DataFrameLeft, text='Exp Date', font=('times new roman', 12, 'bold'),
                                padx=2, pady=6)
        expDate.grid(row=6,column=0,sticky=W)
        expDateEntry = Entry(DataFrameLeft,font=('times new roman', 12, 'bold'),width=26)
        expDateEntry.grid(row=6,column=1)

        Dailydose = Label(DataFrameLeft, text='Daily Dose', font=('times new roman', 12, 'bold'),
                        padx=2, pady=6)
        Dailydose.grid(row=7,column=0,sticky=W)
        DailydoseEntry = Entry(DataFrameLeft,font=('times new roman', 12, 'bold'),width=26)
        DailydoseEntry.grid(row=7,column=1)

        sideEffect = Label(DataFrameLeft, text='Side Effect', font=('times new roman', 12, 'bold'),
                        padx=2, pady=6)
        sideEffect.grid(row=8,column=0,sticky=W)
        sideEffectEntry = Entry(DataFrameLeft,font=('times new roman', 12, 'bold'),width=26)
        sideEffectEntry.grid(row=8,column=1)

        furtherInformation = Label(DataFrameLeft, text='Furthur Information', font=('times new roman', 12, 'bold'),
                        padx=2, pady=6)
        furtherInformation.grid(row=0,column=2,sticky=W)
        furtherInformationEntry = Entry(DataFrameLeft,font=('times new roman', 12, 'bold'),width=23)
        furtherInformationEntry.grid(row=0,column=3)

        BloodPressure = Label(DataFrameLeft, text='Blood Pressure', font=('times new roman', 12, 'bold'),
                        padx=2, pady=6)
        BloodPressure.grid(row=1,column=2,sticky=W)
        BloodPressureEntry = Entry(DataFrameLeft,font=('times new roman', 12, 'bold'),width=23)
        BloodPressureEntry.grid(row=1,column=3)

        StorageAdvice = Label(DataFrameLeft, text='Storage Advice', font=('times new roman', 12, 'bold'),
                        padx=2, pady=6)
        StorageAdvice.grid(row=2,column=2,sticky=W)
        StorageAdviceEntry = Entry(DataFrameLeft,font=('times new roman', 12, 'bold'),width=23)
        StorageAdviceEntry.grid(row=2,column=3)

        Medication = Label(DataFrameLeft, text='Medication', font=('times new roman', 12, 'bold'),
                        padx=2, pady=6)
        Medication.grid(row=3,column=2,sticky=W)
        MedicationEntry = Entry(DataFrameLeft,font=('times new roman', 12, 'bold'),width=23)
        MedicationEntry.grid(row=3,column=3)

        PatientId = Label(DataFrameLeft, text='Patient ID', font=('times new roman', 12, 'bold'),
                        padx=2, pady=6)
        PatientId.grid(row=4,column=2,sticky=W)
        PatientIdEntry = Entry(DataFrameLeft,font=('times new roman', 12, 'bold'),width=23)
        PatientIdEntry.grid(row=4,column=3)

        NHSnumber = Label(DataFrameLeft, text='NHS Number', font=('times new roman', 12, 'bold'),
                        padx=2, pady=6)
        NHSnumber.grid(row=5,column=2,sticky=W)
        NHSnumberEntry = Entry(DataFrameLeft,font=('times new roman', 12, 'bold'),width=23)
        NHSnumberEntry.grid(row=5,column=3)

        PatientName = Label(DataFrameLeft, text='Patient Name', font=('times new roman', 12, 'bold'),
                        padx=2, pady=6)
        PatientName.grid(row=6,column=2,sticky=W)
        PatientNameEntry = Entry(DataFrameLeft,font=('times new roman', 12, 'bold'),width=23)
        PatientNameEntry.grid(row=6,column=3)

        dateOfBirth = Label(DataFrameLeft, text='Date Of Birth', font=('times new roman', 12, 'bold'),
                        padx=2, pady=6)
        dateOfBirth.grid(row=7,column=2,sticky=W)
        dateOfBirthEntry = Entry(DataFrameLeft,font=('times new roman', 12, 'bold'),width=23)
        dateOfBirthEntry.grid(row=7,column=3)

        PatientAddress = Label(DataFrameLeft, text='Patient Address', font=('times new roman', 12, 'bold'),
                        padx=2, pady=6)
        PatientAddress.grid(row=8,column=2,sticky=W)
        PatientAddressentry = Entry(DataFrameLeft,font=('times new roman', 12, 'bold'),width=23)
        PatientAddressentry.grid(row=8,column=3)


        ################################# DataFrameRight ##############################################

        txtPresciption = Text(DataFrameRight,font=('times new roman', 12, 'bold'),padx=2, pady=6, height=14,width=28,
                              borderwidth=2)
        txtPresciption.grid(row=0, column=0)

        #################################### Buttons #####################################################

        prescriptionbtn = Button(ButtonFrame,font=('times new roman', 12, 'bold'),width=15,text='Prescription',
                                    bg='green',fg='white')
        prescriptionbtn.grid(row=0,column=0,padx=10)

        prescriptionDatabtn = Button(ButtonFrame,font=('times new roman', 12, 'bold'),width=15,text='Prescription Data',
                                    bg='green',fg='white')
        prescriptionDatabtn.grid(row=0,column=1,padx=10)

        updatebtn = Button(ButtonFrame,font=('times new roman', 12, 'bold'),width=15,text='Update',
                                    bg='green',fg='white')
        updatebtn.grid(row=0,column=2,padx=10)

        deletebtn = Button(ButtonFrame,font=('times new roman', 12, 'bold'),width=15,text='Delete',
                                    bg='green',fg='white')
        deletebtn.grid(row=0,column=3,padx=10)

        clearbtn = Button(ButtonFrame,font=('times new roman', 12, 'bold'),width=15,text='Clear',
                                    bg='green',fg='white')
        clearbtn.grid(row=0,column=4,padx=10)

        exitbtn = Button(ButtonFrame,font=('times new roman', 12, 'bold'),width=15,text='Exit',
                                    bg='green',fg='white')
        exitbtn.grid(row=0,column=5,padx=10)

        ###################################Table ################################################
        scroll_x = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)

        hospital_table = ttk.Treeview(DetailsFrame, columns=('nameoftable','ref','dose','nooftablets','lot','issuedate',
                                                             'expdate','dailydose','storage','nhsnumber','pname','dob','address'),
                                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x = ttk.Scrollbar(command=hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=hospital_table.yview)

        hospital_table.heading('nameoftable', text='NameOfTable')
        hospital_table.heading('ref', text='RefNo.')
        hospital_table.heading('dose', text='Dose')
        hospital_table.heading('nooftablets', text='No.OfTablets')
        hospital_table.heading('lot', text='Lot')
        hospital_table.heading('issuedate', text='IssueDate')
        hospital_table.heading('expdate', text='ExpDate')
        hospital_table.heading('dailydose', text='DailyDose')
        hospital_table.heading('storage', text='Storage')
        hospital_table.heading('nhsnumber', text='NHSNumber')
        hospital_table.heading('pname', text='PatientName')
        hospital_table.heading('dob', text='DOB')
        hospital_table.heading('address', text='Address')

        hospital_table['show'] = 'headings'

        hospital_table.column('nameoftable', width=120)
        hospital_table.column('ref', width=80)
        hospital_table.column('dose', width=100)
        hospital_table.column('nooftablets', width=100)
        hospital_table.column('lot', width=100)
        hospital_table.column('issuedate', width=100)
        hospital_table.column('expdate', width=100)
        hospital_table.column('dailydose', width=100)
        hospital_table.column('storage', width=100)
        hospital_table.column('nhsnumber', width=100)
        hospital_table.column('pname', width=100)
        hospital_table.column('dob', width=100)
        hospital_table.column('address', width=100)

        

        hospital_table.pack(fill=BOTH,expand=1)




root = Tk()
obj = Hostpital(root)
root.mainloop()