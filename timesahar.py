#!/usr/bin/python3

# -*- coding: utf-8 -*-

import sys
import io
from tkinter import *
from tkinter import ttk
from tkinter import messagebox



class Nafeleh:     
         
    def __init__(self, root):        
        self.root = root       
        self.root.title('نافله شب')
        self.root.resizable(False, False)
 
        window_width = 400
        window_height = 260

        # get the screen dimension
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        # set the position of the window to the center of the screen
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        
        leb1 = ttk.Label(self.root, text="hour sundown :‌")
        leb1.place(relx=0.15, rely=0.2, anchor='center')
        
        leb2 = ttk.Label(self.root, text="min sundown :‌")
        leb2.place(relx=0.15, rely=0.35, anchor='s')
        
        leb3 = ttk.Label(self.root, text="hour sunup :‌")
        leb3.place(relx=0.6, rely=0.2, anchor='center')
        
        leb4 = ttk.Label(self.root, text="min sunup :‌")
        leb4.place(relx=0.6, rely=0.35, anchor='s')
        
        leb5 = ttk.Label(self.root, text="Time A : ")
        leb5.place(relx=0.45, rely=0.5, anchor='center')
        
        leb6 = ttk.Label(self.root, text="Time B : ")
        leb6.place(relx=0.45, rely=0.6, anchor='s')
        
        
        self.combx1 = ttk.Combobox(self.root, width="3", values=['1','2','3','4','5','6','7','8','9','10','11',
            '12','13','14','15','16','17','18','19','20','21','22','23','24'])
        self.combx1.place(relx=0.35, rely=0.2, anchor='center')
        self.combx1['state'] = 'readonly'


        self.combx2 = ttk.Combobox(self.root, width="3", values=['1','2','3','4','5','6','7','8','9','10','11',
                                                 '12','13','14','15','16','17','18','19','20','21',
                                                 '22','23','24','25','26','27','28','29','30','31','32',
                                                 '33','34','35','36','37','38','39','40','41','42','43','44',
                                                 '45','46','47','48','49','50','51','52','53','54','55','56',
                                                 '57','58','59','60'])
        self.combx2.place(relx=0.35, rely=0.35, anchor='s')
        self.combx2['state'] = 'readonly'
        
        
        
        self.combx3 = ttk.Combobox(self.root, width="3", values=['1','2','3','4','5','6','7','8','9','10','11',
            '12','13','14','15','16','17','18','19','20','21','22','23','24'])
        self.combx3.place(relx=0.8, rely=0.2, anchor='center')
        self.combx3['state'] = 'readonly'


        self.combx4 = ttk.Combobox(self.root, width="3", values=['1','2','3','4','5','6','7','8','9','10','11',
                                                 '12','13','14','15','16','17','18','19','20','21',
                                                 '22','23','24','25','26','27','28','29','30','31','32',
                                                 '33','34','35','36','37','38','39','40','41','42','43','44',
                                                 '45','46','47','48','49','50','51','52','53','54','55','56',
                                                 '57','58','59','60'])
        self.combx4.place(relx=0.8, rely=0.35, anchor='s')
        self.combx4['state'] = 'readonly'
        
        self.but = ttk.Button(self.root, text="Computing", command= self.comp)
        self.but.place(relx=0.15, rely=0.7, anchor='center')
        
        self.butquit = ttk.Button(self.root, text="exit", command= self.quitForm)
        self.butquit.place(relx=0.15, rely=0.9, anchor='s')

    def comp(self):
        cm1 = self.combx1.get()
        cm2 = self.combx2.get()
        cm3 = self.combx3.get()
        cm4 = self.combx4.get()
        input_hour_g = int(cm1)
        input_min_g = int(cm2)
        input_hour_t = int(cm3)
        input_min_t = int(cm4)
        
        # messagebox.showinfo("result message", "result : " + str(c))
        
        fullhour = 24
        lenhour = fullhour - input_hour_g
        lenfullhours = lenhour + input_hour_t
        
        hourtomin = lenfullhours * 60
        resultmin = (hourtomin-input_min_g) + input_min_t
        
        tm_hesab1 = round(resultmin * (18/24))
        tm_hesab2 = round(resultmin * (19/24))
        
        area1 = tm_hesab1/60
        area2 = tm_hesab2/60 
        toint1 = int(area1)
        toint2 = int(area2)
        tmround1 = area1 - toint1
        tmround2 = area2 - toint2 
        res_min1 = round(tmround1 * 60)
        res_min2 = round(tmround2 * 60)
        houradd1 = toint1 + input_hour_g
        houradd2 = toint2 + input_hour_g
        minadd1 = input_min_g + res_min1 
        minadd2 = input_min_g + res_min2 
        
        
        if (houradd1 > 24 and houradd2 > 24):
            resh1 = houradd1 - 24
            resh2 = houradd2 - 24
        if (minadd1 < 60):
            # print("time section 1 = ", resh1, ":", minadd1)
            # messagebox.showinfo("result message", "time section 1 = " 
            #                     + str(resh1) + ":" + str(minadd1))
            labtime_section1 = ttk.Label(self.root, text=str(resh1) + ":" + str(minadd1))
            labtime_section1.place(relx=0.6, rely=0.5, anchor='center')
            labtime_section1.configure(foreground='green')
        if (minadd2 < 60):
            # print("time section 2 = ", resh2, ":", minadd2)
            # messagebox.showinfo("result message", "time section 2 = " 
            #                     + str(resh2) + ":" + str(minadd2))
            labtime_section2 = ttk.Label(self.root, text=str(resh2) + ":" + str(minadd2))
            labtime_section2.place(relx=0.6, rely=0.6, anchor='s')
            labtime_section2.configure(foreground='red')
        if (minadd1 >= 60):
            minarea1 = minadd1/60
            tointmin1 = int(minarea1)
            hourinmin1 = minarea1 - tointmin1
            finalmin1 = round(hourinmin1 * 60)
            finalhour1 = resh1 + tointmin1
            # print("time section 1 = ", finalhour1, ":", finalmin1)
            # messagebox.showinfo("result message", "time section 1 = " 
            #                     + str(finalhour1) + ":" + str(finalmin1))
            labtime_section3 = ttk.Label(self.root, text=str(finalhour1) + ":" + str(finalmin1)) 
            labtime_section3.place(relx=0.6, rely=0.5, anchor='center')
            labtime_section3.configure(foreground='red')
        if (minadd2 >= 60):
            minarea2 = minadd2/60
            tointmin2 = int(minarea2)
            hourinmin2 = minarea2 - tointmin2
            finalmin2 = round(hourinmin2 * 60)
            finalhour2 = resh2 + tointmin2
            # print("time section 2 = ", finalhour2, ":", finalmin2)
            # messagebox.showinfo("result message", "time section 2 = " 
            #                     + str(finalhour2) + ":" + str(finalmin2))
            labtime_section4 = ttk.Label(self.root, text=str(finalhour2) + ":" + str(finalmin2)) 
            labtime_section4.place(relx=0.6, rely=0.6, anchor='s')
            labtime_section4.configure(foreground='green')
    def quitForm(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Nafeleh(root)
    root.mainloop()






        