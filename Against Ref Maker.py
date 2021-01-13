from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog
from datetime import date
from lxml import etree
from lxml.builder import E
import csv
import codecs
import clipboard
import sys, os

if getattr(sys, 'frozen', False): # we are running in a bundle
    bundle_dir = sys._MEIPASS # This is where the files are unpacked to
else: # normal Python environment
    bundle_dir = os.path.dirname(os.path.abspath(__file__))

window=Tk()
window.title('Against Ref Maker')
photo = "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"
img = PhotoImage(data=photo)
window.tk.call('wm', 'iconphoto', window._w, img)
window.resizable(0,0)

var = StringVar()
var.set('No File Selected')

def selectFileCallback():
    file_path = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("Text files", "*.txt"),("all files", "*.*")))
    if file_path == '':
        file_path = 'No File Selected'
    var.set(file_path)
    print(file_path)

def xmlMake():
    companyName = cb.get()
    paymentName = pb.get()
    dateInp = dateEntry.get()

    dates = []
    amounts = []
    refs = []

    csv_reader = csv.reader(codecs.open(var.get(), 'rU', 'utf-16'))
    count = 0
    for row in csv_reader:
        if count == 0:
            dates.append(row[0])
            amounts.append(float(row[6]))
        if count == 1:
            pass
        if count == 2:
            pass
        if count == 3:
            refs.append(row[2])
        if count == 4:
            pass
        count += 1
        if count == 5:
            count = 0
    total = round(sum(amounts),2)

    tree = etree.parse(bundle_dir+"\\text.txt")
    root = tree.getroot()
    body = root.find('BODY')
    importData = body.find('IMPORTDATA')
    requestData = importData.find('REQUESTDATA')
    tallyMessage = requestData.find('TALLYMESSAGE')
    voucher = tallyMessage.find('VOUCHER')
    partyLedgerName = voucher.find('PARTYLEDGERNAME')
    if companyName != 'TOPSTAR TRADING PTE LTD':
        partyLedgerName.text = companyName
    date = voucher.find('DATE')
    date1 = voucher.find('EFFECTIVEDATE')
    date.text = str(dateInp)
    date1.text = str(dateInp)
    ledgerEntry = voucher.findall('ALLLEDGERENTRIES.LIST')

    for element in ledgerEntry:
        ledgerName = element.find('LEDGERNAME')
        name = ledgerName.text
        if name == 'TOPSTAR TRADING PTE LTD':
            TSamount = element.find('AMOUNT')
            TSamount.text = "-" + str(total)
            for i in range(len(dates)):
                new  = etree.tostring(E("BILLALLOCATIONS.LIST", E.NAME(refs[i]), E.BILLTYPE("Agst Ref"),E.AMOUNT("-"+str(amounts[i]))))
                newel = etree.fromstring(new)
                element.append(newel)
            if companyName != 'TOPSTAR TRADING PTE LTD':
                ledgerName.text = companyName
        if name == 'UOB BANK':
            element.find('AMOUNT').text = str(total)
            if paymentName != 'UOB BANK':
                ledgerName.text = paymentName


    tree.write("AgainstRef.xml")
    clipboard.copy(os.getcwd() + "\AgainstRef.xml" )

    doneLabel = Label(window, text = "Done. Path to import file copied!")
    doneLabel.grid(row = 9, column = 0, pady = (0,10))

companyLabel = Label(window, text = "Select Company:")
companyData=("TOPSTAR TRADING PTE LTD", "AL ANSAR FOOD PRODUCTS PTE LTD", "ONE OCEAN FOOD PTE LTD", "GRAND PACIFIC TRADING", "UNITED GLOBAL MARKETING PTE LTD", "WEI LEE POLYTHENE", "TOWSENLY FOOD ENTERPRISE")
cb = Combobox(window, values=companyData, width = 35)
cb.current(0)

paymentLabel = Label(window, text = "Select Payment Method:")
paymentData=("UOB BANK", "DBS BANK", "Ocbc Bank", "CASH")
pb = Combobox(window, values=paymentData, width = 35)
pb.current(0)

selectB = Button(window, text ="Select File", command = selectFileCallback)

pathLabel = Label(window, textvariable = var)

makeB = Button(window, text ="Make XML", command = xmlMake)

dateLabel =Label(window, text = "Payment Entry Date (yyyymmdd):")
dateEntry = Entry(window, width = 20, justify='center')
dateEntry.insert(END, date.today().strftime('%Y%m%d'))

paymentLabel.grid(row=0, column=0, padx = (50,50), pady = (10,0))
pb.grid(row=1, column=0)
companyLabel.grid(row=2, column=0, padx = (50,50), pady = (10,0))
cb.grid(row=3, column=0)
dateLabel.grid(row=4, column=0, padx = (50,50), pady = (15,0))
dateEntry.grid(row=5, column=0, padx = (50,50), pady = (0,20))
selectB.grid(row=6, column=0)
pathLabel.grid(row=7, column=0, padx = (10,10), pady=(0,20))
makeB.grid(row=8, column=0, pady = (0,10))

window.mainloop()
