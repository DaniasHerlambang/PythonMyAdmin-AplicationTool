"""
Name             : Python My Admin
Created By       : Rahmandani Herlambang (Danias)
License          : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
Documentation    : https://github.com/DaniasHerlambang13/Python-My-Admin
Thanks to        : Python Tkinter - Mexico Tech - Newbie - Summon Agus 
"""
from Tkinter import *
import MySQLdb
from tkMessageBox  import*
import tkMessageBox as pesan
import ttk


class Data(Frame):
    
    def __init__(self,parent):
        Frame.__init__(self, parent)
        self.induk = parent
##        self.induk.resizable(False, False)
        self.initUI()
        self.OKE.bind("<Return>",self.oke)
     
    def initUI(self):
        
        self.induk.title("PythonMyAdmin")
        # atur ukuran window
        # menempatkan window di tengah layar PC/Laptop
        lebar =900
        tinggi = 650
 
        # ************************* penggunaan fungsi winfo_screenwidth()
        setTengahX = (self.induk.winfo_screenwidth()-lebar)//2
        # ************************* penggunaan fungsi winfo_screenheight()
        setTengahY = (self.induk.winfo_screenheight()-tinggi)//2
 
        self.induk.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
        # **************************************************************** 
        
        mainFrame = Frame(self.induk,bg='#252525' ,relief=FLAT,bd=5)
        mainFrame.pack(fill=BOTH, expand=YES)
        self.main = mainFrame
        
        self.harder = Label (mainFrame,width=10,bg='#000000')
        self.harder.pack(side=TOP,fill=BOTH)
#-------------------------------------
        self.badanatas = Frame(mainFrame,bg='#212121')
        self.badanatas.pack(side=TOP,fill=BOTH)
        
        self.atas = LabelFrame(self.badanatas,text='Koneksi Database',bg='#212121',fg='#e1f5fe')
        self.atas.pack(side=TOP,fill=BOTH,pady=2,padx=2)
        
        self.kiri = Frame(self.atas,bg='#212121')
        self.kiri.pack(side=LEFT)

        self.kanan = Frame(self.atas,bg='#212121')
        self.kanan.pack(side=LEFT)
        
        self.atas1 = Frame(self.kiri,bg='#212121')
        self.atas1.pack(side=TOP,fill=BOTH,pady=1,padx=2)

        self.atas2 = Frame(self.kiri,bg='#212121')
        self.atas2.pack(side=TOP,fill=BOTH,pady=1,padx=2)

        self.user = Label (self.atas1, text='User          :',width=10,bg='#212121',fg='#e1f5fe')
        self.user.pack(side=LEFT,pady=1,padx=2)

        self.E_user = Entry (self.atas1, width=20,bg='#18ffff',fg='#000000')
        self.E_user.pack(side=LEFT,pady=1,padx=2)

        self.passw = Label (self.atas2, text='Password   :',width=10,bg='#212121',fg='#e1f5fe')
        self.passw.pack(side=LEFT,pady=1,padx=2)

        
        self.E_passw = Entry (self.atas2, width=20,bg='#18ffff',fg='#000000',show='*')
        self.E_passw.pack(side=LEFT,pady=1,padx=2)

        self.OKE = Button(self.kanan,text='OKE',bg='#1a237e',fg='#e1f5fe',command=self.oke,height=2,relief=RAISED,bd=2)
        self.OKE.pack(side=LEFT,pady=1,padx=2)

        self.gmb = PhotoImage(file='ll.gif')
        self.UMS = Label(self.atas,bg='#212121',fg='#e1f5fe',image=self.gmb)
        self.UMS.pack(side=RIGHT,padx=25)
        
#------------------------------------        
#------------------------------------
        
        self.menu = Frame(mainFrame,bg='#353535',relief=GROOVE,bd=2)
        self.menu.pack(side=LEFT,pady=2,padx=2,fill=BOTH)
        
        self.menu1 = LabelFrame(self.menu,text='Lihat Database',bg='#353535',fg='#e1f5fe')
        self.menu1.pack(side=TOP,pady=5,padx=5)

        self.fmenu1 = Frame(self.menu1,bg='#353535')
        self.fmenu1.pack(side=TOP,pady=5,padx=5)

        self.showdata = Button (self.fmenu1,text='Lihat database saya',bg='#004d40',fg='#e1f5fe',state=DISABLED,
                                command=self.lihat_database,relief=GROOVE,bd=5)
        self.showdata.pack(side=TOP,fill=BOTH,pady=2,padx=2)

        self.listdata = Listbox (self.fmenu1,fg='#000000',bg='#18ffff')
        self.listdata.pack(side=LEFT,fill=BOTH,pady=2,padx=2)
        s=ttk.Style()
        s.theme_use('classic')
        s.configure('TScrollbar', background='#3e2723')
        scrollbar = ttk.Scrollbar(self.fmenu1, orient=VERTICAL,
                                command=self.listdata.yview,cursor='hand2')
        scrollbar.pack(side=RIGHT, fill=Y)
        self.listdata.config(yscrollcommand=scrollbar.set)
        
#------------------------------------
        self.menu2 = LabelFrame(self.menu,text='Lihat Tabel',bg='#353535',fg='#e1f5fe')
        self.menu2.pack(side=LEFT,pady=5,padx=5)

        self.fmenu2 = Frame(self.menu2,bg='#353535')
        self.fmenu2.pack(side=TOP,pady=5,padx=5)

        self.showtable = Button (self.fmenu2,text='Lihat table ',bg='#004d40',fg='#e1f5fe',state=DISABLED,
                                command=self.lihat_table,relief=GROOVE,bd=5)
        self.showtable.pack(side=TOP,fill=BOTH,pady=2,padx=2)

        self.listtable = Listbox (self.fmenu2,fg='#000000',bg='#18ffff')
        self.listtable.pack(side=LEFT,fill=BOTH,pady=2,padx=2)
        s=ttk.Style()
        s.theme_use('classic')
        s.configure('TScrollbar', background='#3e2723')
        scrollbar = ttk.Scrollbar(self.fmenu2, orient=VERTICAL,
                                command=self.listtable.yview,cursor='hand2')
        scrollbar.pack(side=RIGHT, fill=Y)
        self.listtable.config(yscrollcommand=scrollbar.set)
        
#------------------------------------        
#------------------------------------
        
        self.menuTombol = Frame(mainFrame,bg='#353535',relief=GROOVE,bd=2)
        self.menuTombol.pack(side=TOP,fill=BOTH,pady=2,padx=2,expand=YES)
        
        self.F_tombol = LabelFrame(self.menuTombol,text='Menu Table',bg='#353535',fg='#e1f5fe')
        self.F_tombol.pack(side=BOTTOM,fill=BOTH,pady=2,padx=2)

        self.isi_tombol = Frame(self.F_tombol,bg='#353535')
        self.isi_tombol.pack(side=BOTTOM,fill=BOTH,pady=2,padx=2)

        self.create = Button (self.isi_tombol,text='Add',bg='#004d40',fg='#e1f5fe',state=DISABLED,
                                command=self.add,relief=GROOVE,bd=5)
        self.create.pack(side=LEFT,pady=2,padx=2)

        self.update = Button (self.isi_tombol,text='Edit',bg='#004d40',fg='#e1f5fe',state=DISABLED,
                                command=self.update,relief=GROOVE,bd=5)
        self.update.pack(side=LEFT,pady=2,padx=2)

        self.drop = Button (self.isi_tombol,text='Delete',bg='#004d40',fg='#e1f5fe',state=DISABLED,
                                command=self.delete,relief=GROOVE,bd=5)
        self.drop.pack(side=LEFT,pady=2,padx=2)
        
        self.gmbr = PhotoImage(file='py.gif')
        self.Python = Button(self.isi_tombol,bg='#353535',fg='#e1f5fe',text='about',compound='left',image=self.gmbr,relief=FLAT,
                             command=self.about)
        self.Python.pack(side=RIGHT,padx=5)
                
#------------------------------------        
#------------------------------------
    def pesan(self):
        pesan.showinfo('PythonMydmin','masih dalam perbaikan')
        
    def entry_kosong(self):
        self.E_user.delete(0,END)
        self.E_passw.delete(0,END)
        
    def table_kosong(self):
        self.listtable.delete(0,END)
        
    def oke (self,Event=None):
        self.user=self.E_user.get()
        self.password=self.E_passw.get()

        try:
            self.db = MySQLdb.connect("localhost",port=3306, user=self.user, passwd=self.password)#, db="perbankan" )
            self.cursor = self.db.cursor()
            self.showdata.configure(state=NORMAL)
            print 'sukses'
            self.OKE.configure(text='CONNECT')
            pesan.showinfo('PythonMydmin','Anda sudah terhubung dengan database')
            self.E_user.configure(state=DISABLED)
            self.E_passw.configure(state=DISABLED)
            self.OKE.configure(text='DISCONNECT',command=self.disconnect)
            
        except MySQLdb.OperationalError:
            print 'salah'
            self.OKE.configure(text='DISCONNECT')
            pesan.showwarning('PythonMydmin','Upss , User atau Password salah!!!')
            self.OKE.configure(text='OKE')
            
        self.entry_kosong()

    def disconnect(self):
        self.E_user.configure(state=NORMAL)
        self.E_passw.configure(state=NORMAL)
        self.E_user.delete(0,END)
        self.E_passw.delete(0,END)
        self.listdata.delete(0,END)
        self.listtable.delete(0,END)
        self.showdata.configure(state=DISABLED)
        self.showtable.configure(state=DISABLED)
        self.update_trv()
        self.create.configure(state=DISABLED)
        self.update.configure(state=DISABLED)
        self.drop.configure(state=DISABLED)
        self.OKE.configure(text='OKE',command=self.oke)
        return self.db.close()

#--------------------------------------------------------------------
            
    def lihat_database (self):
        self.listdata.delete(0, END)
        self.cursor.execute("show databases") # select the database        
        tables = self.cursor.fetchall()
        for (x,) in self.cursor:
            self.listdata.insert(END, x)
            
        self.listdata.bind('<ButtonRelease-1>', self.aktif)
         
    def aktif(self,Event=None):
        self.fokus_database=str (self.listdata.get(self.listdata.curselection()))
        self.showtable.configure(state=NORMAL)
        self.table_kosong()
        
        print self.fokus_database
        self.showtable.configure(text=self.fokus_database)
               
    def lihat_table (self):
        self.create.configure(state=DISABLED)
        self.update.configure(state=DISABLED)
        self.drop.configure(state=DISABLED)
        self.table_kosong()
        self.listtable.configure(state=NORMAL)
        fokus=self.fokus_database
        print fokus
        self.cursor.execute("use "+fokus) # use table
        self.cursor.execute("show tables") # select the table

        tables = self.cursor.fetchall()
        for (table_name,) in self.cursor:
            print(table_name)        
            self.listtable.insert(END, table_name)

        self.listtable.bind('<ButtonRelease-1>', self.aktif_table)
        self.showtable.configure(command=self.lihat_table2)

    def lihat_table2 (self):
        self.create.configure(state=DISABLED)
        self.update.configure(state=DISABLED)
        self.drop.configure(state=DISABLED)
        self.table_kosong()
        self.listtable.configure(state=NORMAL)
        self.update_trv()
        fokus=self.fokus_database
        print fokus
        self.cursor.execute("use "+fokus) # use table
        self.cursor.execute("show tables") # select the table

        tables = self.cursor.fetchall()
        for (table_name,) in self.cursor:
            print(table_name)        
            self.listtable.insert(END, table_name)

        self.listtable.bind('<ButtonRelease-1>', self.aktif_table)
    

    def aktif_table(self,Event=None):
        self.create.configure(state=NORMAL)
        self.update.configure(state=NORMAL)
        self.drop.configure(state=NORMAL)
        self.fokus_table=str (self.listtable.get(self.listtable.curselection()))
        
        print self.fokus_table
        fokus_table = self.fokus_table
        fokus_database=self.fokus_database
        #==============================
        
        sql = "desc "+fokus_table
        self.cursor.execute(sql)
        response = self.cursor.fetchall()
        data_heading = []
        for row in response:
            print row[0]
            data_heading.append(row[0])

        self.cursor.execute("SELECT * FROM "+ fokus_table)
        
        numrows = int(self.cursor.rowcount)
        data_isi = []
        for x in range(0,numrows):
            row = self.cursor.fetchone()
            data_isi.append(row)
##            print row
            
        # buat tabel dengan Treeview
        self.FmenuTrv = Frame(self.menuTombol,bg='#212121',relief=GROOVE,bd=2)
        self.FmenuTrv.pack(side=TOP,fill=BOTH,pady=2,padx=2,expand=YES)
        
        self.menuTrv = LabelFrame(self.FmenuTrv,text='Database '+fokus_database+', Table '+fokus_table,bg='#212121',
                                  fg='#e1f5fe',relief=GROOVE,bd=2)
        self.menuTrv.pack(side=TOP,fill=BOTH,pady=8,padx=6,expand=YES)
        
        self.trvTabel = ttk.Treeview(self.menuTrv, columns=data_heading,
                show='headings',height=8)
        ttk.Style().configure("Treeview", background="#004d40",foreground="#18ffff", fieldbackground="#004d43")#004d40
        ttk.Style().configure("Treeview.Heading", background="darkred",foreground="white", fieldbackground="darkred")
        # # buat scrollbar
        sbVer = ttk.Scrollbar(self.menuTrv, orient='vertical',
                command=self.trvTabel.yview,cursor='hand2')
        sbHor = ttk.Scrollbar(self.menuTrv, orient='horizontal',
                command=self.trvTabel.xview,cursor='hand2')
        # pasang dengan layout manager pack()
        sbVer.pack(side=RIGHT, fill=Y)
        sbHor.pack(side=BOTTOM, fill=X)
        self.trvTabel.pack(side=LEFT, expand=YES,fill=BOTH)
        
        
        for kolom in data_heading:
            self.trvTabel.heading(kolom, text=kolom)
            
        for x in data_isi:
            try:
                self.trvTabel.insert('', 'end', values=x)
            except UnicodeDecodeError:
                #return message show box
                pass
                
            
        self.table_kosong()
        self.listtable.bind('<ButtonRelease-1>', self.update_trv)
        
        self.data_isi=data_isi
        self.data_heading=data_heading
        
        self.listtable.configure(state=DISABLED)


    def update_trv(self,Event=None):
        try:
            self.FmenuTrv.destroy()
        except AttributeError:
            print 'ahhhhhhhh'
#------------------------------------        
#------------------------------------
    def update(self):
        try:
            #---------target atribut tabel
            item = self.trvTabel.selection()[0]
    ##        print(self.trvTabel.item(item,"values"))
            self.fokus_atribut=[]
            for row in (self.trvTabel.item(item,"values")):
                self.fokus_atribut.append(row)
            self.fokus_atributs=self.fokus_atribut[0]
    ##        print self.fokus_atribut[0]

            #----------proses masuk database > tampilkan data atribut[0] yang didapat dari desc
            fokus_table = self.fokus_table
            fokus_database=self.fokus_database

            sql = "desc "+fokus_table
            self.cursor.execute(sql)
            response = self.cursor.fetchall()
            masukan = []
            for row in response:
                print row[0]
                masukan.append(row[0])
            self.patokan_id = masukan[0]
            print masukan[0]
            #-------------kerangka update komponen   
            root = Toplevel()
            root.geometry('600x250')
            root.title("Update table "+"("+fokus_table+")"+" dengan id = "+self.fokus_atributs)
            
            self.inti = Frame(root,bg='#000000',relief=GROOVE,bd=2)
            self.inti.pack(side=BOTTOM,fill=BOTH,pady=2,padx=2)
            
            self.inti2 = Frame(root,bg='#000000',relief=GROOVE,bd=2)
            self.inti2.pack(side=TOP,fill=BOTH,pady=2,padx=2)
            
            self.pilih = LabelFrame(self.inti2,text='lokasi update',bg='#000000',
                                      fg='#e1f5fe',relief=GROOVE,bd=2)
            self.pilih.pack(side=LEFT,fill=BOTH,pady=8,padx=8)

            self.pilih2 = Frame(self.inti2,bg='#353535',relief=SUNKEN,bd=5)
            self.pilih2.pack(side=TOP,fill=BOTH,pady=2,padx=2)

            self.pilih3 = LabelFrame(self.inti2,text='Update data',bg='#000000',fg='#e1f5fe')
            self.pilih3.pack(side=TOP,fill=BOTH,pady=15,padx=2)

            self.listpilih = Listbox (self.pilih, bg="#004d40",fg="#18ffff")
            self.listpilih.pack(side=LEFT,fill=BOTH,pady=2,padx=2)
            s=ttk.Style()
            s.theme_use('classic')
            s.configure('TScrollbar', background='#3e2723')
            scrollbar = ttk.Scrollbar(self.pilih, orient=VERTICAL,
                                    command=self.listpilih.yview,cursor='hand2')
            scrollbar.pack(side=RIGHT, fill=Y)
            self.listpilih.config(yscrollcommand=scrollbar.set)

            self.informasi = Label(self.pilih2,text='Update pada ID = '+self.fokus_atributs ,bg='#353535',
                                      fg='#e1f5fe',relief=FLAT,bd=2)
            self.informasi.pack(side=TOP)

            self.pilih_lokasi = Label(self.pilih2,text='Target Update = Belum Ada',bg='#353535',
                                      fg='#e1f5fe',relief=FLAT,bd=2)
            self.pilih_lokasi.pack(side=TOP,fill=BOTH)

            self.informasi_data_lama = Label(self.pilih3,text='Data Belum Ada',bg='#000000',
                                      fg='#e1f5fe',relief=FLAT,bd=2)
            self.informasi_data_lama.pack(side=TOP,fill=BOTH)
            
            default = StringVar()   
            default.set( "Edit Data Kamu Disini..." )
            self.Data_baru = Entry(self.pilih3,fg='#000000',bg='#18ffff',
                                   relief=GROOVE,bd=2,width=25)
            self.Data_baru.pack(side=TOP,fill=BOTH,padx=4,pady=4)
            
            #--------function eksekusi pertahap
            def ketemu_target(e):
                self.fokus_lokasi = str (self.listpilih.get(self.listpilih.curselection()))
                self.pilih_lokasi.configure(text='Target Update = '+self.fokus_lokasi)
    ##            print  self.fokus_lokasi
                nilai_fokus = self.listpilih.curselection()
                self.nominal=[]
                for k in nilai_fokus:
                    self.nominal.append(k)
    ##            print self.nominal[0]

                item = self.trvTabel.selection()[0]
                self.x=[]
                for row in (self.trvTabel.item(item,"values")):
                    self.x.append(row)

                data_calon_di_update = self.x[self.nominal[0]]    
                print self.x[self.nominal[0]]
    ##            print self.patokan_id
                self.informasi_data_lama.configure(text=self.x[self.nominal[0]])
##                self.Data_baru.configure(state=NORMAL)
                self.Data_baru.delete(0,END)

            def input_data_update(e):
                masukan_update = self.Data_baru.get()
                '''
                "update nasabah  set alamat_nasabah='xx' where id_nasabah='11';"
                '''
                try:
                    if masukan_update == "":
                        pesan.showerror('PythonMydmin','Tidak Boleh Kosong')
                    else:                
                        try:            
                            self.cursor.execute("UPDATE  {} SET {}='{}' where {} = '{}';".format(fokus_table,self.fokus_lokasi,masukan_update,self.patokan_id,
                                                                                                       self.fokus_atributs))
                            self.db.commit()
                            self.reset()
                            pesan.showinfo('PythonMydmin','Data Sudah Masuk')
                            root.destroy()
                        except MySQLdb.OperationalError:   
                            pesan.showerror('PythonMydmin','Data Belum Masuk')
                except AttributeError:
                    pesan.showerror('PythonMydmin','Anda belum memilih data')
            def buat(root, masukan):
               entries = []
               for field in masukan:
                    self.listpilih.insert(END, field)
                  
            ents = buat(self.pilih, masukan)
            huhu = input_data_update
            root.bind('<Return>', (lambda event, e=ents: tampil(e)))   
            b1 = Button(self.inti, text='Update',command=(lambda e=huhu: input_data_update(e)),bg='darkred',fg='#e1f5fe',relief=GROOVE,bd=3)
            b1.pack(side=LEFT, padx=5, pady=5)
            b2 = Button(self.inti, text='Keluar', command=root.destroy,bg='darkred',fg='#e1f5fe',relief=GROOVE,bd=3)
            b2.pack(side=LEFT, padx=5, pady=5)

            self.listpilih.bind('<<ListboxSelect>>', ketemu_target )
        
        except IndexError:
            pesan.showwarning('PythonMydmin','Pilih Salah Satu Data!!!')
            
    def reset(self):
        '''Remove all items from the view'''
        self._nodes = [""]
        for item in self.trvTabel.get_children("") :
            self.trvTabel.delete(item)
            
        self.db = MySQLdb.connect("localhost",port=3306, user=self.user, passwd=self.password, db=self.fokus_database )
        self.cursor = self.db.cursor()
        
        fokus_table = self.fokus_table
        #==============================
        sql = "desc "+fokus_table
        self.cursor.execute(sql)
        response = self.cursor.fetchall()
        data_heading = []
        for row in response:
            print row[0]
            data_heading.append(row[0])
        self.cursor.execute("SELECT * FROM "+ fokus_table)      
        numrows = int(self.cursor.rowcount)
        data_isi = []
        for x in range(0,numrows):
            row = self.cursor.fetchone()
            data_isi.append(row)          
        for dat in data_isi:
            self.trvTabel.insert('', 'end', values=dat)#, tags = ('oddrow',))

    def _on_select(self, event=None):
        item=self.trvTabel.selection()[0]
        self.event_generate("<<EventSelected>>")
        
    def add(self):
        #------------------------------------
        fokus_table = self.fokus_table
        fokus_database=self.fokus_database

        sql = "desc "+fokus_table
        self.cursor.execute(sql)
        response = self.cursor.fetchall()
        masukan = []
        for row in response:
            print row[0]
            masukan.append(row[0])
        #------------------------------------    
        root = Toplevel()
        root.title(fokus_database+" "+"("+fokus_table+")")

        def ambil(entries):
             try:
                judul_x=[]
                isi_x=[]
                for entry in entries:
                  judul_entry = entry[0]
                  isi  = entry[1].get()
                  judul_x.append(judul_entry)
                  isi_x.append(isi)     
##                  print('%s: "%s"' % (judul_entry, isi))
                  
                  connection = MySQLdb.connect(host='localhost',user='root', passwd='x',
                                               db=fokus_database)
                  cursor = connection.cursor()
                  sql = "use "+fokus_table
                  
                judul_isi  = tuple(judul_x)
                isi_isi    = list(isi_x)
                try: bisi_isi[0] = int(isi_isi[0])
                except: isi_isi[0] = isi_isi[0]
                isi_isi = tuple(isi_x)

                print """INSERT INTO `{}` {} VALUES {}""".format(fokus_table, str(judul_isi).replace("'", "`"), isi_isi)
                cursor.execute("""INSERT INTO `{}` {} VALUES {}""".format(fokus_table, str(judul_isi).replace("'", "`"), isi_isi))
                connection.commit()                  
                pesan.showinfo('PythonMydmin','Data Sudah Masuk')
                self.reset()
                root.destroy()
                
             except MySQLdb.IntegrityError:
                print 'salah'
                pesan.showwarning('PythonMydmin','Salah')
             except MySQLdb.OperationalError:
                print 'salah'
                pesan.showwarning('PythonMydmin','Salah')
              

        def buat(root, masukan):
           entries = []
           for field in masukan:
              row = Frame(root,bg='#004d40')
              lab = Label(row, width=15, text=field, anchor='w',bg='#353535',fg='#e1f5fe',bd=4,relief=RIDGE)
              ent = Entry(row,fg='#004d40',bg='#18ffff')
              row.pack(side=TOP, fill=X, padx=5, pady=5)
              lab.pack(side=LEFT)
              ent.pack(side=RIGHT, expand=YES, fill=X)
              entries.append((field, ent))
           return entries
        
        ents = buat(root, masukan)
        root.bind('<Return>', (lambda event, e=ents: ambil(e)))   
        b1 = Button(root, text='Oke',
              command=(lambda e=ents: ambil(e)),bg='darkred',fg='#e1f5fe',relief=GROOVE,bd=3)
        b1.pack(side=LEFT, padx=5, pady=5)
        b2 = Button(root, text='Keluar', command=root.destroy,bg='darkred',fg='#e1f5fe',relief=GROOVE,bd=3)
        b2.pack(side=LEFT, padx=5, pady=5)
        
    def delete(self):
        try:
            if askyesno ("PythonMydmin","Anda Yakin Ingin Menghapus ?"):
                #---------target nominal atribut tabel
                item = self.trvTabel.selection()[0]
    ##            print(self.trvTabel.item(item,"values"))
                self.fokus_atribut=[]
                for row in (self.trvTabel.item(item,"values")):
                    self.fokus_atribut.append(row)
                self.fokus_atributs=self.fokus_atribut[0]
    ##            print self.fokus_atribut[0]

                #----------proses ketemu target atribut primary key
                fokus_table = self.fokus_table
                fokus_database=self.fokus_database

                sql = "desc "+fokus_table
                self.cursor.execute(sql)
                response = self.cursor.fetchall()
                masukan = []
                for row in response:
    ##                print row[0]
                    masukan.append(row[0])
                self.patokan_id = masukan[0]
    ##            print masukan[0]

                target_delete =("DELETE FROM  {} WHERE {} = '{}';".format(fokus_table,self.patokan_id ,self.fokus_atributs))
                print target_delete
                
                self.cursor.execute("DELETE FROM  {} WHERE {} = '{}';".format(fokus_table,self.patokan_id ,self.fokus_atributs))
                self.db.commit()
                self.reset()
            
        except IndexError:
            pesan.showwarning('PythonMydmin','Pilih Salah Satu Data!!!')       
    def about(self):
        
        root = Toplevel()
        root.overrideredirect(True) #menghapus kulit window
        root.after(4000, root.destroy)

        lebar =320
        tinggi = 285
 
        # ************************* penggunaan fungsi winfo_screenwidth()
        setTengahX = (root.winfo_screenwidth()-lebar)//2
        # ************************* penggunaan fungsi winfo_screenheight()
        setTengahY = (root.winfo_screenheight()-tinggi)//2
 
        root.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
        # **************************************************************** 
        
        self.inti1 = Frame(root,bg='#353535')
        self.inti1.pack(side=LEFT,fill=BOTH)

        self.gm = PhotoImage(file='WOLF.gif')
        self.WOLF = Label(self.inti1,bg='#353535',text='Rahmandani Herlambang \n \n harness the power of \n Python ',compound='top',fg='black',image=self.gm,
                          font=(40))
        self.WOLF.pack(side=RIGHT,padx=35)

if __name__ =='__main__':
    root = Tk()
    app = Data(root)
    root.mainloop()

#####************************************************************************************************************************
##import MySQLdb
##
##connection = MySQLdb.connect(
##                host = 'localhost',
##                user = 'root',
##                passwd = 'x')  # create the connection
##
##cursor = connection.cursor()     # get the cursor
##
##cursor.execute("USE perbankan") # select the database
##cursor.execute("desc perbankan")
##table_name = cursor.fetchall()
##for (table_name,) in cursor:
##        print(table_name)
##
##connection = MySQLdb.connect(host='localhost',user='root',passwd='x',db='perbankan')
##cursor = connection.cursor()
##sql = "desc rekening;"
##cursor.execute(sql)
##response = cursor.fetchall()
##for row in response:
##    print row[0]
####
##connection = MySQLdb.connect(host='localhost',user='root',passwd='x',db='perbankan')
##cursor = connection.cursor()
##sql = "use rekening;"
##cursor.execute("insert into rekening ( no_rekening , kode_cabangFK , pin, saldo) values (197,'BRUX' , '0000',500000);")
##connection.commit()

###************************************************************************************************************************
##
