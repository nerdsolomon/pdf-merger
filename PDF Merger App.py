from tkinter import *
from tkinter import filedialog,messagebox
import PyPDF3
page = Tk()
page.title('PDF Merger')

def add():
    files = filedialog.askopenfilename(initialdir='/storage/emulated/0/documents', title='Files', filetypes=(('PDF Files', '*.pdf'),))
    entry_list.insert(END,files)

def action():
    pdfWriter = PyPDF3.PdfFileWriter()

    items = entry_list.get(0, END)
    for item in items:
    	pdfFile = open(item, 'rb')
    	pdfReader = PyPDF3.PdfFileReader(pdfFile)
    	
    	for pageNum in range(pdfReader.numPages):
    		pageObj = pdfReader.getPage(pageNum)
    		pdfWriter.addPage(pageObj)
    	
    new = new_file.get() + '.pdf'
    pdfOutputFile = open(new, 'wb')
    pdfWriter.write(pdfOutputFile)
    	
    pdfOutputFile.close()
    pdfFile.close()
    		
    messagebox.showinfo('PDF Merger','Files Merged\nSuccessfully')

Label(page,text='PDF MERGER',font=('arial',10, 'bold')).grid(row=0,columnspan=3)

entry_list = Listbox(page,width=38,height=5)
entry_list.grid(row=1,columnspan=3)

Button(page,text='Browse Files',font=('arial',6),command=add).grid(row=2, columnspan=3,pady=10,ipadx=240)

new_file = Entry(page)
new_file.grid(row=4,columnspan=2, column=1,sticky='e')
Label(page,text='New File Name : ',font=('arial',7)).grid(row=4,columnspan=2,sticky='w',pady=10)

Button(page,text='Merge',font=('arial',6),command=action).grid(row=5,columnspan=3,pady=10,ipadx=270)

page.mainloop()	