import  tkinter as tk
import main as ma
import tkinter.messagebox as messagebox

#登錄界面
root=tk.Tk()
photo = tk.PhotoImage(file="d12.png")
# lb=tk.Label(cav,image=photo)
# lb.grid(row=5,columns=5)
tx=tk.Text(root,width=45,height=10)
tx.image_create(index="end",image=photo,padx=80)
tx.config(state="disable")
tx.grid(row=0,column=0,columnspan=3)


lbl_emp=tk.Label(text="职号")
txt_emp=tk.Entry(root)
lbl_emp.grid(row=2,column=0)
txt_emp.grid(row=2,column=1)





lbl_pwd=tk.Label(text="密碼")
txt_pwd=tk.Entry(root,show='*')
lbl_pwd.grid(row=3,column=0)
txt_pwd.grid(row=3,column=1)




def login2(root):
    # varemp=txt_emp.get()
    # if(varemp=='90'):
    #     messagebox.showinfo("","dd")
    root.quit()
    ma.Main()




btn_login=tk.Button(text="登錄",width=10,command=lambda :login2(root))
btn_login.grid(row=4,column=0,columnspan=3)

btn_login=tk.Button(text="幫助",width=10,command=lambda :messagebox.showinfo("About us","有疑問撥打2270"))
btn_login.grid(row=5,column=0,columnspan=3)


root.title("電腦管理系統")
root.geometry(newGeometry="300x250")
root.resizable(width=False,height=False)
root.mainloop()








