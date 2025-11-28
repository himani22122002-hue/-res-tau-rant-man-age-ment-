Query = ("select * from register where email=%s")
                value =(self.var_email.get(),)
                cursor.execute(Query, value)
                row=cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error", "User already Exist,please try another email")
            else:

                '''jyoti = mysql.connector.connect(host="localhost", user="root", password='Root@1234', database="jyoti",auth_plugin="mysql_native_password")
                            my_cursor = jyoti.cursor(buffered=True)
                            my_cursor.execute("=%s and password=%s",
                            (
                                self.var_email.get(),
                                self.var_password.get()select * from register where email
                            ))
                            row=my_cursor.fetchone()
                            if row==None:
                                messagebox.showerror("error","invalid username &password")
                            else:
                                open_main=messagebox.askyesno("yesno","access only admin")
                                if open_main>0:
                                    self.new_window=Toplevel(self.new_window)
                                    self.app=HotelManagementSystem(self.new_window)
                                else:
                                    if not open_main:
                                        return
                
                
                
                jyoti = mysql.connector.connect(host="localhost", user="root", password='Root@1234', database="jyoti",auth_plugin="mysql_native_password")
                        my_cursor = jyoti.cursor(buffered=True)
                        email=self.textuser.get()
                        password=self.passwordentry.get()
                        sql="select * from register where email=%s and password=%s"
                        my_cursor.execute(sql,[(email),(password)])
                        results=my_cursor.fetchall()
                        if results:
                            messagebox.showinfo("","login successfully")
                            return True
                        else:
                                messagebox.showinfo("","incorrect username&password")
                        jyoti.commit()
                        jyoti.close()