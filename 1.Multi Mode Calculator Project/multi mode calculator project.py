import tkinter as tk
import math
from tkinter import Menu, PhotoImage,ttk

class CalculatorApp:
    def __init__(self, window):
        self.window = window
        self.window.title("CALCULATOR")
        self.window.geometry("900x800+10+10")  # Fixed size for both calculators
        self.window['bg'] = "lightblue"
        self.menu_created = False

        self.standard = PhotoImage(file=r"C:\Users\udayk\Downloads\calculator.png").subsample(25, 25)
        self.scientific_icon = PhotoImage(file=r"C:\Users\udayk\Downloads\flask.png").subsample(25, 25)
        self.currency_icon = PhotoImage(file=r"C:\Users\udayk\Downloads\exchange.png").subsample(25, 25)
        self.volume_icon = PhotoImage(file=r"C:\Users\udayk\Downloads\measure.png").subsample(25, 25)
        self.length_icon = PhotoImage(file=r"C:\Users\udayk\Downloads\measuring-tape.png").subsample(25, 25)
        self.weight_mass = PhotoImage(file=r"C:\Users\udayk\Downloads\weight.png").subsample(25, 25)
        self.temperature_icon = PhotoImage(file=r"C:\Users\udayk\Downloads\hot.png").subsample(25, 25)
        self.area_icon = PhotoImage(file=r"C:\Users\udayk\Downloads\area-graph.png").subsample(25, 25)
        self.speed_icon = PhotoImage(file=r"C:\Users\udayk\Downloads\speedometer.png").subsample(25, 25)
        self.time_icon = PhotoImage(file=r"C:\Users\udayk\Downloads\chronometer.png").subsample(25, 25)
        self.power_icon = PhotoImage(file=r"C:\Users\udayk\Downloads\flash.png").subsample(25, 25)
        self.angle_icon = PhotoImage(file=r"C:\Users\udayk\Downloads\angle.png").subsample(25, 25)
        self.pressure_icon = PhotoImage(file=r"C:\Users\udayk\Downloads\pressure-gauge.png").subsample(25, 25)
        self.data_icon = PhotoImage(file=r"C:\Users\udayk\Downloads\master-data.png").subsample(25, 25)

        self.create_ui()

        #Initialize the frames for each calculator mode
        self.standard_frame=self.create_standard_frame()
        self.scientific_frame = self.create_scientific_frame()
        self.currency_frame=self.create_currency_frame()
        self.temperature_frame=self.create_temperature_frame()
        self.power_frame=self.create_power_frame()
        self.speed_frame=self.create_speed_frame()
        self.pressure_frame=self.create_pressure_frame()
        self.data_frame=self.create_data_frame()
        self.time_frame=self.create_time_frame()
        self.length_frame=self.create_length_frame()
        self.weightmass_frame=self.create_weightmass_frame()
        self.volume_frame=self.create_volume_frame()
        self.area_frame=self.create_area_frame()
        self.angle_frame=self.create_angle_frame()  

        # show the default frame (standard calculator)
        self.show_frame(self.standard_frame)

    def create_ui(self):
        
        # Menu creation
        self.menu_button = tk.Button(self.window, text="≡", bg="lightblue", compound="left", width=3, height=1,font=("Arial",15,"bold"))
        self.menu_button.grid(row=0, sticky="W", column=0, padx=5, pady=10)
        self.menu_button.bind('<Button-1>', self.show_menu)

        self.label_menu = Menu(self.window, tearoff=0)

        self.label = tk.Label(self.window, text="CALCULATOR", bg="orange", font=("Arial", 12, "bold"))
        self.label.grid(row=0, column=0, padx=10, pady=10)

    def show_menu(self, event):
        if not self.menu_created:
            menu_items = [
                ("Standard", self.switch_to_standard, self.standard),
                ("Scientific", self.switch_to_scientific, self.scientific_icon),
                ("Currency",self.switch_to_currency, self.currency_icon),
                ("Volume",self.switch_to_volume, self.volume_icon),
                ("Length",self.switch_to_length, self.length_icon),
                ("Weight and mass",self.switch_to_weight_mass, self.weight_mass),
                ("Temperature",self.switch_to_temperature, self.temperature_icon),
                ("Area",self.switch_to_area, self.area_icon),
                ("Speed",self.switch_to_speed, self.speed_icon),
                ("Time",self.switch_to_time, self.time_icon),
                ("power",self.switch_to_power, self.power_icon),
                ("Angle",self.switch_to_angle, self.angle_icon),
                ("Pressure",self.switch_to_pressure, self.pressure_icon),
                ("Data",self.switch_to_data, self.data_icon),            
            ]
            
            for label, command, icon in menu_items:
                self.label_menu.add_command(label=label, image=icon, compound='left', command=command)
                idx = self.label_menu.index(tk.END)
                self.label_menu.entryconfig(idx, background="lightblue", foreground="black", font=("Arial", 13, "bold"))

            self.menu_created = True

        x = self.menu_button.winfo_rootx()
        y = self.menu_button.winfo_rooty() + self.menu_button.winfo_height()
        self.label_menu.post(x, y)

    def show_frame(self,frame):
        self.standard_frame.grid_forget()
        self.scientific_frame.grid_forget()
        self.currency_frame.grid_forget()
        self.temperature_frame.grid_forget()
        self.power_frame.grid_forget()
        self.pressure_frame.grid_forget()
        self.time_frame.grid_forget()
        self.data_frame.grid_forget()
        self.speed_frame.grid_forget()
        self.length_frame.grid_forget()
        self.weightmass_frame.grid_forget()
        self.volume_frame.grid_forget()
        self.area_frame.grid_forget()
        self.angle_frame.grid_forget()

        frame.grid(row=1,column=0)

    def create_standard_frame(self):
        
        frame = tk.Frame(self.window,bg="lightblue",width=600,height=800)
        frame.grid(row=0, column=0, sticky="nsew")

        self.l1 = tk.Label(frame, text="standard calculator", bg="orange", font=("Arial", 12, "bold"))
        self.l1.grid(row=0, column=1, padx=10, pady=10)

        self.e1 = tk.Entry(frame, width=40, justify="right", bd=0, highlightthickness=0, font=("Arial", 12, "bold"))
        self.e1.grid(row=1, column=3, columnspan=7, padx=10)

        self.e2 = tk.Entry(frame, width=40, justify="right", bd=0, highlightthickness=0, font=("Arial", 12, "bold"))
        self.e2.grid(row=2, column=3, columnspan=7, padx=10)

        buttons = [
            'c', '%', 'π', '←',
            '1/x', 'x²', '√', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '.', '0', '='
        ]

        row_val = 3
        col_val = 3

        for button in buttons:
            
            if button == "=":
                b = tk.Button(frame, text=button, width=11, height=2, bg="red", fg="white", relief="raised", borderwidth=3,
                              command=self.standard_calculate, font=("Arial", 15, "bold"))
                b.grid(row=row_val, column=col_val,columnspan=3, padx=10, pady=10)
                
            elif button == "c":
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=lambda: (self.e1.delete(0, tk.END), self.e2.delete(0, tk.END)))
            elif button == '←':
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=self.delete_last_character1)
            elif button == '√':
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=self.standard_sqrt)
            elif button == 'π':
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=self.standard_pi)
            elif button == '1/x':
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=self.standard_inverse)
                
            elif button == 'x²':
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=self.standard_square_power)
            else:
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=lambda value=button: self.add_to_expression1(value))
            b.grid(row=row_val, column=col_val, padx=10, pady=10)
            
            col_val += 1
            if col_val > 6:
                col_val = 3
                row_val += 1

        return frame

    def create_scientific_frame(self):
        
        frame = tk.Frame(self.window, bg="lightblue", width=600, height=600)
        self.l2= tk.Label(frame, text="scientific calculator", bg="orange", font=("Arial", 12, "bold"))
        self.l2.grid(row=0, column=1, padx=10, pady=10)

        self.e3 = tk.Entry(frame, width=40, justify="right", bd=0, highlightthickness=0, font=("Arial", 12, "bold"))
        self.e3.grid(row=1, column=3, columnspan=7, padx=10)

        self.e4 = tk.Entry(frame, width=40, justify="right", bd=0, highlightthickness=0, font=("Arial", 12, "bold"))
        self.e4.grid(row=2, column=3, columnspan=7, padx=10)

        buttons = [
           'sin','cos','tan','(','←','c',
           'asin','acos','atan',')','log','1/x',
           'sinh','cosh','tanh','7','8','9',
           '√','%','/','4','5','6',
           'π','*','-','1','2','3',
           'ln','x²','+','.','0','='
           
        ]

        row_val = 3
        col_val = 3

        for button in buttons:
            
            if button == "=":
                b = tk.Button(frame, text=button, width=5, height=2, bg="red", fg="white", relief="raised", borderwidth=3,
                              command=self.scientific_calculate, font=("Arial", 15, "bold"))
                b.grid(row=row_val, column=col_val ,padx=10, pady=10)
                
            elif button == "c":
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=lambda: (self.e3.delete(0, tk.END), self.e4.delete(0, tk.END)))

            elif button == '←':
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=self.delete_last_character2)
                
            elif button == '√':
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=self.scientific_sqrt)
                
            elif button == 'π':
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=self.scientific_pi)
            elif button == '1/x':
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=self.scientific_inverse)
                
            elif button == 'x²':
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=self.scientific_square_power)
                
            elif button == 'ln':
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=self.calculate_ln)
                
            elif button == 'log':
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=self.calculate_log)
                
            elif button == 'sin':
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=self.sin)               
                
            elif button == 'cos':
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=self.cos)

            elif button == 'tan':
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=self.tan)

            elif button == 'asin':
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=self.asin)

            elif button == 'acos':
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=self.acos)

            elif button == 'atan':
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=self.atan)
                
            elif button == 'sinh':
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=self.atan)
            elif button == 'cosh':
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=self.atan)
                
            elif button == 'tanh':
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=self.atan)
                
            elif button == 'n!':
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=self.factorial)
    
            else:
                b = tk.Button(frame, text=button, width=5, height=2, bg="black", fg="white", font=("Arial", 15, "bold"),
                              relief="raised", borderwidth=3, command=lambda value=button: self.add_to_expression2(value))
            b.grid(row=row_val, column=col_val, padx=10, pady=10)
            
            col_val += 1
            if col_val > 8:
                col_val = 3
                row_val += 1

        return frame

    def create_currency_frame(self):
        
        frame=tk.Frame(self.window,bg="lightblue", width=500, height=600)

        l3 = ttk.Label(frame, text="Currency Converter",
                       background='orange', foreground="black",
                       font=("Times New Roman", 15))
        l3.grid(row=0, column=0, padx=5, pady=10, sticky="W")
        
        self.e5 = ttk.Entry(frame, width=20, justify="right", font=("Arial", 15, "bold"))
        self.e5.grid(row=1, column=1, columnspan=7, padx=5, pady=10, sticky="W")
        
        l4 = ttk.Label(frame, text="Select the 'from' currency:",
                       font=("Times New Roman", 10))
        l4.grid(column=1, row=2, padx=10, pady=25)
        
        self.n1 = tk.StringVar(value='USD')
        self.from_currency_combo = ttk.Combobox(frame, width=27, textvariable=self.n1)
        self.from_currency_combo['values'] = ('USD', 'INR', 'EUR', 'GBP')
        self.from_currency_combo.grid(column=2, row=2, pady=30)
   
        l5 = ttk.Label(frame, text="Select the 'to' currency:",
                       font=("Times New Roman", 10))
        l5.grid(column=1, row=7, padx=10, pady=25)
  
        self.n2 = tk.StringVar(value='INR')
        self.to_currency_combo = ttk.Combobox(frame, width=27, textvariable=self.n2)
        self.to_currency_combo['values'] = ('USD', 'INR', 'EUR', 'GBP')
        self.to_currency_combo.grid(column=2, row=7, pady=30)
        
        self.e6= ttk.Entry(frame, width=20, justify="right", font=("Arial", 15, "bold"))
        self.e6.grid(row=8, column=1, columnspan=7, padx=5, pady=30, sticky="W")

        button_row_start = 3
        button_row_end = 6
        button_column_start = 3  # To position the buttons towards the right side

        for i in range(9, -1, -1):
            button = tk.Button(frame, text=str(i),bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"),command=lambda i=i: self.on_button_currency(i))
            row = button_row_start + (9 - i) // 3  # Adjust row positioning
            col = button_column_start + (9 - i) % 3  # Adjust column positioning to the right side
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        dot_button = tk.Button(frame, text='.',width=4, height=1,bg="black",fg="white",font=("Arial", 15, "bold"),command=lambda: self.on_button_currency('.'))
        dot_button.grid(row=button_row_end, column=button_column_start + 1, padx=5, pady=5, sticky="nsew")

        # Creating delete button
        delete_button = tk.Button(frame, text='←',width=4, height=1,bg="black",fg="white", font=("Arial", 15, "bold"),command=self.delete_last_character3)
        delete_button.grid(row=button_row_end, column=button_column_start + 2, padx=5, pady=5, sticky="nsew")

        # Creating clear button
        clear_button = tk.Button(frame, text='C',width=4, height=1,bg="black",fg="white", font=("Arial", 15, "bold"),command=lambda: (self.e5.delete(0, tk.END), self.e6.delete(0, tk.END)))
        clear_button.grid(row=button_row_start + 4, column=4, padx=5, pady=5, sticky="nsew")

        # Creating "=" button for conversion
        equal_button = tk.Button(frame, text='=',width=4, height=1,bg="black",fg="white",font=("Arial", 15, "bold"), command=self.convert_currency)
        equal_button.grid(row=button_row_start + 4, column=5, padx=5, pady=5, sticky="nsew")

        # Adjust row/column weights to make buttons expand
        for i in range(3):
            frame.grid_columnconfigure(i + button_column_start, weight=1)
        for i in range(button_row_start, button_row_end + 1):
            frame.grid_rowconfigure(i, weight=1)

        return frame
    
    def create_temperature_frame(self):
        
        frame=tk.Frame(self.window,bg="lightblue", width=500, height=600)

        l6 = ttk.Label(frame, text="Temperature Converter",
                       background='orange', foreground="black",
                       font=("Times New Roman", 15))
        l6.grid(row=0, column=0, padx=5, pady=10, sticky="W")
        
        self.e7 = ttk.Entry(frame, width=20, justify="right", font=("Arial", 15, "bold"))
        self.e7.grid(row=1, column=1, columnspan=7, padx=5, pady=10, sticky="W")
        
        l7 = ttk.Label(frame, text="Select the 'from' Temperature:",
                       font=("Times New Roman", 10))
        l7.grid(column=1, row=2, padx=10, pady=25)
        
        self.n3 = tk.StringVar(value='Kelvin')
        self.from_temperature_combo = ttk.Combobox(frame, width=27, textvariable=self.n3)
        self.from_temperature_combo['values'] = ('Fahrenheit', 'Celsius', 'Kelvin')
        self.from_temperature_combo.grid(column=2, row=2, pady=30)
   
        l8 = ttk.Label(frame, text="Select the 'to' Temperature:",
                       font=("Times New Roman", 10))
        l8.grid(column=1, row=7, padx=5, pady=10)

        self.n4 = tk.StringVar(value='Celsius')
        self.to_temperature_combo = ttk.Combobox(frame, width=27, textvariable=self.n4)
        self.to_temperature_combo['values'] = ('Fahrenheit', 'Celsius', 'Kelvin')
        self.to_temperature_combo.grid(column=2, row=7, pady=30)
        
        self.e8= ttk.Entry(frame, width=20, justify="right", font=("Arial", 15, "bold"))
        self.e8.grid(row=8, column=1, columnspan=7, padx=5, pady=30, sticky="W")

        button_row_start = 3
        button_row_end = 6
        button_column_start = 3  # To position the buttons towards the right side
        
        for i in range(9, -1, -1):
            button = tk.Button(frame, text=str(i), bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"),command=lambda i=i: self.on_button_temperature(i))
            row = button_row_start + (9 - i) // 3  # Adjust row positioning
            col = button_column_start + (9 - i) % 3  # Adjust column positioning to the right side
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        dot_button = tk.Button(frame, text='.',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda: self.on_button_temperature('.'))
        dot_button.grid(row=button_row_end, column=button_column_start + 1, padx=5, pady=5, sticky="nsew")

        # Creating delete button
        delete_button = tk.Button(frame, text='←',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"),command=self.delete_last_character4)
        delete_button.grid(row=button_row_end, column=button_column_start + 2, padx=5, pady=5, sticky="nsew")

       # Creating clear button
        clear_button = tk.Button(frame, text='C',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"),command=lambda: (self.e7.delete(0, tk.END), self.e8.delete(0, tk.END)))
        clear_button.grid(row=button_row_start + 4, column=4, padx=5, pady=5, sticky="nsew")

        # Creating "=" button for conversion
        equal_button = tk.Button(frame, text='=',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=self.convert_temperature)
        equal_button.grid(row=button_row_start + 4, column=5, padx=5, pady=5, sticky="nsew")

        # Adjust row/column weights to make buttons expand
        for i in range(3):
            frame.grid_columnconfigure(i + button_column_start, weight=1)
        for i in range(button_row_start, button_row_end + 1):
            frame.grid_rowconfigure(i, weight=1)

        return frame
    
    def create_power_frame(self):
        
        frame=tk.Frame(self.window,bg="lightblue", width=500, height=600)

        l9 = ttk.Label(frame, text="Power Converter",
                       background='orange', foreground="black",
                       font=("Times New Roman", 15))
        l9.grid(row=0, column=0, padx=5, pady=10, sticky="W")
        
        self.e9 = ttk.Entry(frame, width=20, justify="right", font=("Arial", 15, "bold"))
        self.e9.grid(row=1, column=1, columnspan=7, padx=5, pady=10, sticky="W")
        
        l10 = ttk.Label(frame, text="Select the 'from' power:",
                       font=("Times New Roman", 10))
        l10.grid(column=1, row=2, padx=10, pady=25)
        
        self.n5 = tk.StringVar(value='Kilowatts')
        self.from_power_combo = ttk.Combobox(frame, width=27, textvariable=self.n5)
        self.from_power_combo['values'] = ('Watts', 'Kilowatts', 'Horsepower')
        self.from_power_combo.grid(column=2, row=2, pady=30)
   
        l11 = ttk.Label(frame, text="Select the 'to' Temperature:",
                       font=("Times New Roman", 10))
        l11.grid(column=1, row=7, padx=5, pady=10)

        self.n6 = tk.StringVar(value='Watts')
        self.to_power_combo = ttk.Combobox(frame, width=27, textvariable=self.n6)
        self.to_power_combo['values'] = ('Watts', 'Kilowatts', 'Horsepower')
        self.to_power_combo.grid(column=2, row=7, pady=30)
        
        self.e10= ttk.Entry(frame, width=20, justify="right", font=("Arial", 15, "bold"))
        self.e10.grid(row=8, column=1, columnspan=7, padx=5, pady=30, sticky="W")

        button_row_start = 3
        button_row_end = 6
        button_column_start = 3  # To position the buttons towards the right side

        for i in range(9, -1, -1):
            button = tk.Button(frame, text=str(i),bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda i=i: self.on_button_power(i))
            row = button_row_start + (9 - i) // 3  # Adjust row positioning
            col = button_column_start + (9 - i) % 3  # Adjust column positioning to the right side
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        dot_button = tk.Button(frame, text='.',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda: self.on_button_power('.'))
        dot_button.grid(row=button_row_end, column=button_column_start + 1, padx=5, pady=5, sticky="nsew")

        # Creating delete button
        delete_button = tk.Button(frame, text='←',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=self.delete_last_character5)
        delete_button.grid(row=button_row_end, column=button_column_start + 2, padx=5, pady=5, sticky="nsew")

       # Creating clear button
        clear_button = tk.Button(frame, text='C',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda: (self.e9.delete(0, tk.END), self.e10.delete(0, tk.END)))
        clear_button.grid(row=button_row_start + 4, column=4, padx=5, pady=5, sticky="nsew")

        # Creating "=" button for conversion
        equal_button = tk.Button(frame, text='=',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=self.convert_power)
        equal_button.grid(row=button_row_start + 4, column=5, padx=5, pady=5, sticky="nsew")

        # Adjust row/column weights to make buttons expand
        for i in range(3):
            frame.grid_columnconfigure(i + button_column_start, weight=1)
        for i in range(button_row_start, button_row_end + 1):
            frame.grid_rowconfigure(i, weight=1)

        return frame

    def create_pressure_frame(self):
        
        frame=tk.Frame(self.window,bg="lightblue", width=500, height=600)

        l10 = ttk.Label(frame, text="Pressure Converter",
                       background='orange', foreground="black",
                       font=("Times New Roman", 15))
        l10.grid(row=0, column=0, padx=5, pady=10, sticky="W")
        
        self.e11 = ttk.Entry(frame, width=20, justify="right", font=("Arial", 15, "bold"))
        self.e11.grid(row=1, column=1, columnspan=7, padx=5, pady=10, sticky="W")
        
        l11 = ttk.Label(frame, text="Select the 'from' pressure:",
                       font=("Times New Roman", 10))
        l11.grid(column=1, row=2, padx=10, pady=25)
        
        self.n7= tk.StringVar(value='Pascals (Pa)')
        self.from_pressure_combo = ttk.Combobox(frame, width=27, textvariable=self.n7)
        self.from_pressure_combo['values'] = ('Pascals (Pa)', 'Bar', 'Atmospheres (atm)','Pounds per square inch (psi)')
        self.from_pressure_combo.grid(column=2, row=2, pady=30)
   
        l12 = ttk.Label(frame, text="Select the 'to' pressure:",
                       font=("Times New Roman", 10))
        l12.grid(column=1, row=7, padx=5, pady=10)

        self.n8 = tk.StringVar(value='Bar')
        self.to_pressure_combo = ttk.Combobox(frame, width=27, textvariable=self.n8)
        self.to_pressure_combo['values'] = ('Pascals (Pa)', 'Bar', 'Atmospheres (atm)','Pounds per square inch (psi)')
        self.to_pressure_combo.grid(column=2, row=7, pady=30)
        
        self.e12= ttk.Entry(frame, width=20, justify="right", font=("Arial", 15, "bold"))
        self.e12.grid(row=8, column=1, columnspan=7, padx=5, pady=30, sticky="W")

        button_row_start = 3
        button_row_end = 6
        button_column_start = 3  # To position the buttons towards the right side

        for i in range(9, -1, -1):
            button = tk.Button(frame, text=str(i),bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda i=i: self.on_button_pressure(i))
            row = button_row_start + (9 - i) // 3  # Adjust row positioning
            col = button_column_start + (9 - i) % 3  # Adjust column positioning to the right side
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        dot_button = tk.Button(frame, text='.',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda: self.on_button_pressure('.'))
        dot_button.grid(row=button_row_end, column=button_column_start + 1, padx=5, pady=5, sticky="nsew")

        # Creating delete button
        delete_button = tk.Button(frame, text='←', bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"),command=self.delete_last_character6)
        delete_button.grid(row=button_row_end, column=button_column_start + 2, padx=5, pady=5, sticky="nsew")

       # Creating clear button
        clear_button = tk.Button(frame, text='C',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda: (self.e11.delete(0, tk.END), self.e12.delete(0, tk.END)))
        clear_button.grid(row=button_row_start + 4, column=4, padx=5, pady=5, sticky="nsew")

        # Creating "=" button for conversion
        equal_button = tk.Button(frame, text='=',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"),command=self.convert_pressure)
        equal_button.grid(row=button_row_start + 4, column=5, padx=5, pady=5, sticky="nsew")

        # Adjust row/column weights to make buttons expand
        for i in range(3):
            frame.grid_columnconfigure(i + button_column_start, weight=1)
        for i in range(button_row_start, button_row_end + 1):
            frame.grid_rowconfigure(i, weight=1)

        return frame
    
    def create_data_frame(self):
        
        frame=tk.Frame(self.window,bg="lightblue", width=500, height=600)

        l13 = ttk.Label(frame, text="Data Converter",
                       background='orange', foreground="black",
                       font=("Times New Roman", 15))
        l13.grid(row=0, column=0, padx=5, pady=10, sticky="W")
        
        self.e13 = ttk.Entry(frame, width=20, justify="right", font=("Arial", 15, "bold"))
        self.e13.grid(row=1, column=1, columnspan=7, padx=5, pady=10, sticky="W")
        
        l14 = ttk.Label(frame, text="Select the 'from' data:",
                       font=("Times New Roman", 10))
        l14.grid(column=1, row=2, padx=10, pady=25)
        
        self.n9 = tk.StringVar(value='Bytes (B)')
        self.from_data_combo = ttk.Combobox(frame, width=27, textvariable=self.n9)
        self.from_data_combo['values'] = ('Bytes (B)', 'Kilobytes (KB)', 'Megabytes (MB)', 'Gigabytes (GB)', 'Terabytes (TB)')
        self.from_data_combo.grid(column=2, row=2, pady=30)
   
        l15 = ttk.Label(frame, text="Select the 'to' data:",
                       font=("Times New Roman", 10))
        l15.grid(column=1, row=7, padx=5, pady=10)

        self.n10 = tk.StringVar(value='Kilobytes (KB)')
        self.to_data_combo = ttk.Combobox(frame, width=27, textvariable=self.n10)
        self.to_data_combo['values'] = ('Bytes (B)', 'Kilobytes (KB)', 'Megabytes (MB)', 'Gigabytes (GB)', 'Terabytes (TB)')
        self.to_data_combo.grid(column=2, row=7, pady=30)
        
        self.e14= ttk.Entry(frame, width=20, justify="right", font=("Arial", 15, "bold"))
        self.e14.grid(row=8, column=1, columnspan=7, padx=5, pady=30, sticky="W")

        button_row_start = 3
        button_row_end = 6
        button_column_start = 3  # To position the buttons towards the right side

        for i in range(9, -1, -1):
            button = tk.Button(frame, text=str(i), bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"),command=lambda i=i: self.on_button_data(i))
            row = button_row_start + (9 - i) // 3  # Adjust row positioning
            col = button_column_start + (9 - i) % 3  # Adjust column positioning to the right side
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        dot_button = tk.Button(frame, text='.',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda: self.on_button_data('.'))
        dot_button.grid(row=button_row_end, column=button_column_start + 1, padx=5, pady=5, sticky="nsew")

        # Creating delete button
        delete_button = tk.Button(frame, text='←',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=self.delete_last_character7)
        delete_button.grid(row=button_row_end, column=button_column_start + 2, padx=5, pady=5, sticky="nsew")

       # Creating clear button
        clear_button = tk.Button(frame, text='C',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda: (self.e13.delete(0, tk.END), self.e14.delete(0, tk.END)))
        clear_button.grid(row=button_row_start + 4, column=4, padx=5, pady=5, sticky="nsew")

        # Creating "=" button for conversion
        equal_button = tk.Button(frame, text='=', bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"),command=self.convert_data)
        equal_button.grid(row=button_row_start + 4, column=5, padx=5, pady=5, sticky="nsew")

        # Adjust row/column weights to make buttons expand
        for i in range(3):
            frame.grid_columnconfigure(i + button_column_start, weight=1)
        for i in range(button_row_start, button_row_end + 1):
            frame.grid_rowconfigure(i, weight=1)

        return frame

    def create_time_frame(self):
        
        frame=tk.Frame(self.window,bg="lightblue", width=400, height=600)

        l19 = ttk.Label(frame, text="Time Converter",
                       background='orange', foreground="black",
                       font=("Times New Roman", 15))
        l19.grid(row=0, column=0, padx=5, pady=10, sticky="W")
        
        self.e17 = ttk.Entry(frame, width=20, justify="right", font=("Arial", 15, "bold"))
        self.e17.grid(row=1, column=1, columnspan=7, padx=5, pady=10, sticky="W")
        
        l20 = ttk.Label(frame, text="Select the 'from' time:",
                       font=("Times New Roman", 10))
        l20.grid(column=1, row=2, padx=10, pady=25)
        
        self.n13 = tk.StringVar(value='Hours')
        self.from_time_combo = ttk.Combobox(frame, width=27, textvariable=self.n13)
        self.from_time_combo['values'] = ('Seconds', 'Minutes', 'Hours', 'Days')
        self.from_time_combo.grid(column=2, row=2, pady=30)
   
        l21 = ttk.Label(frame, text="Select the 'to' time:",
                       font=("Times New Roman", 10))
        l21.grid(column=1, row=7, padx=5, pady=10)

        self.n14 = tk.StringVar(value='Minutes')
        self.to_time_combo = ttk.Combobox(frame, width=27, textvariable=self.n14)
        self.to_time_combo['values'] = ('Seconds', 'Minutes', 'Hours', 'Days')
        self.to_time_combo.grid(column=2, row=7, pady=30)
        
        self.e18= ttk.Entry(frame, width=20, justify="right", font=("Arial", 15, "bold"))
        self.e18.grid(row=8, column=1, columnspan=7, padx=5, pady=30, sticky="W")

        button_row_start = 3
        button_row_end = 6
        button_column_start = 3  # To position the buttons towards the right side

        for i in range(9, -1, -1):
            button = tk.Button(frame, text=str(i),bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda i=i: self.on_button_time(i))
            row = button_row_start + (9 - i) // 3  # Adjust row positioning
            col = button_column_start + (9 - i) % 3  # Adjust column positioning to the right side
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        dot_button = tk.Button(frame, text='.',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda: self.on_button_time('.'))
        dot_button.grid(row=button_row_end, column=button_column_start + 1, padx=5, pady=5, sticky="nsew")

        # Creating delete button
        delete_button = tk.Button(frame, text='←', bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"),command=self.delete_last_character9)
        delete_button.grid(row=button_row_end, column=button_column_start + 2, padx=5, pady=5, sticky="nsew")

       # Creating clear button
        clear_button = tk.Button(frame, text='C',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda: (self.e17.delete(0, tk.END), self.e18.delete(0, tk.END)))
        clear_button.grid(row=button_row_start + 4, column=4, padx=5, pady=5, sticky="nsew")

        # Creating "=" button for conversion
        equal_button = tk.Button(frame, text='=',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=self.convert_time)
        equal_button.grid(row=button_row_start + 4, column=5, padx=5, pady=5, sticky="nsew")

        # Adjust row/column weights to make buttons expand
        for i in range(3):
            frame.grid_columnconfigure(i + button_column_start, weight=1)
        for i in range(button_row_start, button_row_end + 1):
            frame.grid_rowconfigure(i, weight=1)

        return frame

    def create_speed_frame(self):
        
        frame=tk.Frame(self.window,bg="lightblue", width=500, height=600)

        l16 = ttk.Label(frame, text="Speed Converter",
                       background='orange', foreground="black",
                       font=("Times New Roman", 15))
        l16.grid(row=0, column=0, padx=5, pady=10, sticky="W")
        
        self.e15 = ttk.Entry(frame, width=20, justify="right", font=("Arial", 15, "bold"))
        self.e15.grid(row=1, column=1, columnspan=7, padx=5, pady=10, sticky="W")
        
        l17 = ttk.Label(frame, text="Select the 'from' speed:",
                       font=("Times New Roman", 10))
        l17.grid(column=1, row=2, padx=10, pady=25)
        
        self.n11 = tk.StringVar(value='Miles per hour (mph)')
        self.from_speed_combo = ttk.Combobox(frame, width=27, textvariable=self.n11)
        self.from_speed_combo['values'] = ('Meters per second (m/s)', 'Kilometers per hour (km/h)', 'Miles per hour (mph)')
        self.from_speed_combo.grid(column=2, row=2, pady=30)
   
        l18 = ttk.Label(frame, text="Select the 'to' speed:",
                       font=("Times New Roman", 10))
        l18.grid(column=1, row=7, padx=5, pady=10)

        self.n12 = tk.StringVar(value='Kilometers per hour (km/h)')
        self.to_speed_combo = ttk.Combobox(frame, width=27, textvariable=self.n12)
        self.to_speed_combo['values'] = ('Meters per second (m/s)', 'Kilometers per hour (km/h)', 'Miles per hour (mph)')
        self.to_speed_combo.grid(column=2, row=7, pady=30)
        
        self.e16= ttk.Entry(frame, width=20, justify="right", font=("Arial", 15, "bold"))
        self.e16.grid(row=8, column=1, columnspan=7, padx=5, pady=30, sticky="W")

        button_row_start = 3
        button_row_end = 6
        button_column_start = 3  # To position the buttons towards the right side

        for i in range(9, -1, -1):
            button = tk.Button(frame, text=str(i),bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda i=i: self.on_button_speed(i))
            row = button_row_start + (9 - i) // 3  # Adjust row positioning
            col = button_column_start + (9 - i) % 3  # Adjust column positioning to the right side
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        dot_button = tk.Button(frame, text='.',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda: self.on_button_speed('.'))
        dot_button.grid(row=button_row_end, column=button_column_start + 1, padx=5, pady=5, sticky="nsew")

        # Creating delete button
        delete_button = tk.Button(frame, text='←',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=self.delete_last_character9)
        delete_button.grid(row=button_row_end, column=button_column_start + 2, padx=5, pady=5, sticky="nsew")

       # Creating clear button
        clear_button = tk.Button(frame, text='C',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda: (self.e15.delete(0, tk.END), self.e16.delete(0, tk.END)))
        clear_button.grid(row=button_row_start + 4, column=4, padx=5, pady=5, sticky="nsew")

        # Creating "=" button for conversion
        equal_button = tk.Button(frame, text='=',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=self.convert_speed)
        equal_button.grid(row=button_row_start + 4, column=5, padx=5, pady=5, sticky="nsew")

        # Adjust row/column weights to make buttons expand
        for i in range(3):
            frame.grid_columnconfigure(i + button_column_start, weight=1)
        for i in range(button_row_start, button_row_end + 1):
            frame.grid_rowconfigure(i, weight=1)

        return frame

    def create_length_frame(self):
        
        frame=tk.Frame(self.window,bg="lightblue", width=500, height=600)

        l22 = ttk.Label(frame, text="Length Converter",
                       background='orange', foreground="black",
                       font=("Times New Roman", 15))
        l22.grid(row=0, column=0, padx=5, pady=10, sticky="W")
        
        self.e19 = ttk.Entry(frame, width=20, justify="right", font=("Arial", 15, "bold"))
        self.e19.grid(row=1, column=1, columnspan=7, padx=5, pady=10, sticky="W")
        
        l23 = ttk.Label(frame, text="Select the 'from' length:",
                       font=("Times New Roman", 10))
        l23.grid(column=1, row=2, padx=10, pady=25)
        
        self.n15 = tk.StringVar(value='Meters')
        self.from_length_combo = ttk.Combobox(frame, width=27, textvariable=self.n15)
        self.from_length_combo['values'] = ('Meters','Kilometers','Centimeters','Miles','Feet')
        self.from_length_combo.grid(column=2, row=2, pady=30)
   
        l24 = ttk.Label(frame, text="Select the 'to' length:",
                       font=("Times New Roman", 10))
        l24.grid(column=1, row=7, padx=5, pady=10)

        self.n16 = tk.StringVar(value='Kilometers')
        self.to_length_combo = ttk.Combobox(frame, width=27, textvariable=self.n16)
        self.to_length_combo['values'] = ('Meters','Kilometers','Centimeters','Miles','Feet')
        self.to_length_combo.grid(column=2, row=7, pady=30)
        
        self.e20= ttk.Entry(frame, width=20, justify="right", font=("Arial", 15, "bold"))
        self.e20.grid(row=8, column=1, columnspan=7, padx=5, pady=30, sticky="W")

        button_row_start = 3
        button_row_end = 6
        button_column_start = 3  # To position the buttons towards the right side

        for i in range(9, -1, -1):
            button = tk.Button(frame, text=str(i),bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda i=i: self.on_button_length(i))
            row = button_row_start + (9 - i) // 3  # Adjust row positioning
            col = button_column_start + (9 - i) % 3  # Adjust column positioning to the right side
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        dot_button = tk.Button(frame, text='.',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda: self.on_button_length('.'))
        dot_button.grid(row=button_row_end, column=button_column_start + 1, padx=5, pady=5, sticky="nsew")

        # Creating delete button
        delete_button = tk.Button(frame, text='←',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=self.delete_last_character10)
        delete_button.grid(row=button_row_end, column=button_column_start + 2, padx=5, pady=5, sticky="nsew")

       # Creating clear button
        clear_button = tk.Button(frame, text='C',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda: (self.e19.delete(0, tk.END), self.e20.delete(0, tk.END)))
        clear_button.grid(row=button_row_start + 4, column=4, padx=5, pady=5, sticky="nsew")

        # Creating "=" button for conversion
        equal_button = tk.Button(frame, text='=',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=self.convert_length)
        equal_button.grid(row=button_row_start + 4, column=5, padx=5, pady=5, sticky="nsew")

        # Adjust row/column weights to make buttons expand
        for i in range(3):
            frame.grid_columnconfigure(i + button_column_start, weight=1)
        for i in range(button_row_start, button_row_end + 1):
            frame.grid_rowconfigure(i, weight=1)

        return frame

    def create_weightmass_frame(self):
        
        frame=tk.Frame(self.window,bg="lightblue", width=500, height=600)

        l25 = ttk.Label(frame, text="Weight & Mass Converter",
                       background='orange', foreground="black",
                       font=("Times New Roman", 15))
        l25.grid(row=0, column=0, padx=5, pady=10, sticky="W")
        
        self.e21 = ttk.Entry(frame, width=20, justify="right", font=("Arial", 15, "bold"))
        self.e21.grid(row=1, column=1, columnspan=4, padx=5, pady=10, sticky="W")
        
        l26 = ttk.Label(frame, text="Select the 'from' weight  & mass:",
                       font=("Times New Roman", 10))
        l26.grid(column=1, row=2, padx=10, pady=25)
        
        self.n17 = tk.StringVar(value='Kilograms')
        self.from_weightmass_combo = ttk.Combobox(frame, width=27, textvariable=self.n17)
        self.from_weightmass_combo['values'] = ('Grams','Kilograms','Pounds', 'Ounces')
        self.from_weightmass_combo.grid(column=2, row=2, pady=30)
   
        l27 = ttk.Label(frame, text="Select the 'to' weight & mass:",
                       font=("Times New Roman", 10))
        l27.grid(column=1, row=7, padx=5, pady=10)

        self.n18 = tk.StringVar(value='Grams')
        self.to_weightmass_combo = ttk.Combobox(frame, width=27, textvariable=self.n18)
        self.to_weightmass_combo['values'] = ('Grams','Kilograms','Pounds', 'Ounces')
        self.to_weightmass_combo.grid(column=2, row=7, pady=30)
        
        self.e22= ttk.Entry(frame, width=20, justify="right", font=("Arial", 15, "bold"))
        self.e22.grid(row=8, column=1, columnspan=7, padx=5, pady=30, sticky="W")

        button_row_start = 3
        button_row_end = 6
        button_column_start = 3  # To position the buttons towards the right side

        for i in range(9, -1, -1):
            button = tk.Button(frame, text=str(i),bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda i=i: self.on_button_weightmass(i))
            row = button_row_start + (9 - i) // 3  # Adjust row positioning
            col = button_column_start + (9 - i) % 3  # Adjust column positioning to the right side
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        dot_button = tk.Button(frame, text='.', bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"),command=lambda: self.on_button_weightmass('.'))
        dot_button.grid(row=button_row_end, column=button_column_start + 1, padx=5, pady=5, sticky="nsew")

        # Creating delete button
        delete_button = tk.Button(frame, text='←',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=self.delete_last_character11)
        delete_button.grid(row=button_row_end, column=button_column_start + 2, padx=5, pady=5, sticky="nsew")

       # Creating clear button
        clear_button = tk.Button(frame, text='C',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda: (self.e21.delete(0, tk.END), self.e22.delete(0, tk.END)))
        clear_button.grid(row=button_row_start + 4, column=4, padx=5, pady=5, sticky="nsew")

        # Creating "=" button for conversion
        equal_button = tk.Button(frame, text='=', bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"),command=self.convert_weightmass)
        equal_button.grid(row=button_row_start + 4, column=5, padx=5, pady=5, sticky="nsew")

        # Adjust row/column weights to make buttons expand
        for i in range(3):
            frame.grid_columnconfigure(i + button_column_start, weight=1)
        for i in range(button_row_start, button_row_end + 1):
            frame.grid_rowconfigure(i, weight=1)

        return frame

    def create_volume_frame(self):
        
        frame=tk.Frame(self.window,bg="lightblue", width=500, height=600)

        l28 = ttk.Label(frame, text="Volume Converter",
                       background='orange', foreground="black",
                       font=("Times New Roman", 15))
        l28.grid(row=0, column=0, padx=5, pady=10, sticky="W")
        
        self.e23 = ttk.Entry(frame, width=20, justify="right", font=("Arial", 15, "bold"))
        self.e23.grid(row=1, column=1, columnspan=4, padx=5, pady=10, sticky="W")
        
        l29 = ttk.Label(frame, text="Select the 'from' volume:",
                       font=("Times New Roman", 10))
        l29.grid(column=1, row=2, padx=10, pady=25)
        
        self.n19 = tk.StringVar(value='Milliliters')
        self.from_volume_combo = ttk.Combobox(frame, width=27, textvariable=self.n19)
        self.from_volume_combo['values'] = ('Milliliters','Liters','Cubic meters','Cubic centimeters')
        self.from_volume_combo.grid(column=2, row=2, pady=30)
   
        l30 = ttk.Label(frame, text="Select the 'to' volume:",
                       font=("Times New Roman", 10))
        l30.grid(column=1, row=7, padx=5, pady=10)

        self.n20 = tk.StringVar(value='Liters')
        self.to_volume_combo = ttk.Combobox(frame, width=27, textvariable=self.n20)
        self.to_volume_combo['values'] = ('Milliliters','Liters','Cubic meters','Cubic centimeters')
        self.to_volume_combo.grid(column=2, row=7, pady=30)
        
        self.e24= ttk.Entry(frame, width=20, justify="right", font=("Arial", 15, "bold"))
        self.e24.grid(row=8, column=1, columnspan=7, padx=5, pady=30, sticky="W")

        button_row_start = 3
        button_row_end = 6
        button_column_start = 3  # To position the buttons towards the right side

        for i in range(9, -1, -1):
            button = tk.Button(frame, text=str(i),bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda i=i: self.on_button_volume(i))
            row = button_row_start + (9 - i) // 3  # Adjust row positioning
            col = button_column_start + (9 - i) % 3  # Adjust column positioning to the right side
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        dot_button = tk.Button(frame, text='.',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda: self.on_button_volume('.'))
        dot_button.grid(row=button_row_end, column=button_column_start + 1, padx=5, pady=5, sticky="nsew")

        # Creating delete button
        delete_button = tk.Button(frame, text='←', bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"),command=self.delete_last_character12)
        delete_button.grid(row=button_row_end, column=button_column_start + 2, padx=5, pady=5, sticky="nsew")

       # Creating clear button
        clear_button = tk.Button(frame, text='C', bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"),command=lambda: (self.e23.delete(0, tk.END), self.e24.delete(0, tk.END)))
        clear_button.grid(row=button_row_start + 4, column=4, padx=5, pady=5, sticky="nsew")

        # Creating "=" button for conversion
        equal_button = tk.Button(frame, text='=', bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"),command=self.convert_volume)
        equal_button.grid(row=button_row_start + 4, column=5, padx=5, pady=5, sticky="nsew")

        # Adjust row/column weights to make buttons expand
        for i in range(3):
            frame.grid_columnconfigure(i + button_column_start, weight=1)
        for i in range(button_row_start, button_row_end + 1):
            frame.grid_rowconfigure(i, weight=1)

        return frame

    def create_area_frame(self):
        
        frame=tk.Frame(self.window,bg="lightblue", width=500, height=600)

        l31 = ttk.Label(frame, text="Area Converter",
                       background='orange', foreground="black",
                       font=("Times New Roman", 15))
        l31.grid(row=0, column=0, padx=5, pady=10, sticky="W")
        
        self.e25 = ttk.Entry(frame, width=20, justify="right", font=("Arial", 15, "bold"))
        self.e25.grid(row=1, column=1, columnspan=4, padx=5, pady=10, sticky="W")

        
        l32 = ttk.Label(frame, text="Select the 'from' area:",
                       font=("Times New Roman", 10))
        l32.grid(column=1, row=2, padx=10, pady=25)
        
        self.n21 = tk.StringVar(value='Square meters')
        self.from_area_combo = ttk.Combobox(frame, width=27, textvariable=self.n21)
        self.from_area_combo['values'] = ('Square meters','Square kilometers','Square feet','Acres')
        self.from_area_combo.grid(column=2, row=2, pady=30)
   
        l33= ttk.Label(frame, text="Select the 'to' speed:",
                       font=("Times New Roman", 10))
        l33.grid(column=1, row=7, padx=5, pady=10)

        self.n22 = tk.StringVar(value='Square kilometers')
        self.to_area_combo = ttk.Combobox(frame, width=27, textvariable=self.n22)
        self.to_area_combo['values'] = ('Square meters','Square kilometers','Square feet','Acres')
        self.to_area_combo.grid(column=2, row=7, pady=30)
        
        self.e26= ttk.Entry(frame, width=20, justify="right", font=("Arial", 15, "bold"))
        self.e26.grid(row=8, column=1, columnspan=7, padx=5, pady=30, sticky="W")

        button_row_start = 3
        button_row_end = 6
        button_column_start = 3  # To position the buttons towards the right side

        for i in range(9, -1, -1):
            button = tk.Button(frame, text=str(i), bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"),command=lambda i=i: self.on_button_area(i))
            row = button_row_start + (9 - i) // 3  # Adjust row positioning
            col = button_column_start + (9 - i) % 3  # Adjust column positioning to the right side
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        dot_button = tk.Button(frame, text='.',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda: self.on_button_area('.'))
        dot_button.grid(row=button_row_end, column=button_column_start + 1, padx=5, pady=5, sticky="nsew")

        # Creating delete button
        delete_button = tk.Button(frame, text='←',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=self.delete_last_character13)
        delete_button.grid(row=button_row_end, column=button_column_start + 2, padx=5, pady=5, sticky="nsew")

       # Creating clear button
        clear_button = tk.Button(frame, text='C',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda: (self.e25.delete(0, tk.END), self.e26.delete(0, tk.END)))
        clear_button.grid(row=button_row_start + 4, column=4, padx=5, pady=5, sticky="nsew")

        # Creating "=" button for conversion
        equal_button = tk.Button(frame, text='=',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=self.convert_area)
        equal_button.grid(row=button_row_start + 4, column=5, padx=5, pady=5, sticky="nsew")

        # Adjust row/column weights to make buttons expand
        for i in range(3):
            frame.grid_columnconfigure(i + button_column_start, weight=1)
        for i in range(button_row_start, button_row_end + 1):
            frame.grid_rowconfigure(i, weight=1)

        return frame

    def create_angle_frame(self):
        
        frame=tk.Frame(self.window,bg="lightblue", width=500, height=600)

        l34 = ttk.Label(frame, text="Angle Converter",
                       background='orange', foreground="black",
                       font=("Times New Roman", 15))
        l34.grid(row=0, column=0, padx=5, pady=10, sticky="W")
        
        self.e27 = ttk.Entry(frame, width=20, justify="right", font=("Arial", 15, "bold"))
        self.e27.grid(row=1, column=1, columnspan=7, padx=5, pady=10, sticky="W")
        
        l35 = ttk.Label(frame, text="Select the 'from' angle:",
                       font=("Times New Roman", 10))
        l35.grid(column=1, row=2, padx=10, pady=25)
        
        self.n23 = tk.StringVar(value='Degrees')
        self.from_angle_combo = ttk.Combobox(frame, width=27, textvariable=self.n23)
        self.from_angle_combo['values'] = ('Degrees','Radians','Gradians')
        self.from_angle_combo.grid(column=2, row=2, pady=30)
   
        l36 = ttk.Label(frame, text="Select the 'to' angle:",
                       font=("Times New Roman", 10))
        l36.grid(column=1, row=7, padx=5, pady=10)

        self.n24 = tk.StringVar(value='Gradians')
        self.to_angle_combo = ttk.Combobox(frame, width=27, textvariable=self.n24)
        self.to_angle_combo['values'] = ('Degrees','Radians','Gradians')
        self.to_angle_combo.grid(column=2, row=7, pady=30)
        
        self.e28= ttk.Entry(frame, width=20, justify="right", font=("Arial", 15, "bold"))
        self.e28.grid(row=8, column=1, columnspan=7, padx=5, pady=30, sticky="W")

        button_row_start = 3
        button_row_end = 6
        button_column_start = 3  # To position the buttons towards the right side

        for i in range(9, -1, -1):
            button = tk.Button(frame, text=str(i),bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda i=i: self.on_button_angle(i))
            row = button_row_start + (9 - i) // 3  # Adjust row positioning
            col = button_column_start + (9 - i) % 3  # Adjust column positioning to the right side
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        dot_button = tk.Button(frame, text='.',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda: self.on_button_angle('.'))
        dot_button.grid(row=button_row_end, column=button_column_start + 1, padx=5, pady=5, sticky="nsew")

        # Creating delete button
        delete_button = tk.Button(frame, text='←',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=self.delete_last_character14)
        delete_button.grid(row=button_row_end, column=button_column_start + 2, padx=5, pady=5, sticky="nsew")

       # Creating clear button
        clear_button = tk.Button(frame, text='C',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=lambda: (self.e27.delete(0, tk.END), self.e28.delete(0, tk.END)))
        clear_button.grid(row=button_row_start + 4, column=4, padx=5, pady=5, sticky="nsew")

        # Creating "=" button for conversion
        equal_button = tk.Button(frame, text='=',bg="black",fg="white",width=4, height=1,font=("Arial", 15, "bold"), command=self.convert_angle)
        equal_button.grid(row=button_row_start + 4, column=5, padx=5, pady=5, sticky="nsew")

        # Adjust row/column weights to make buttons expand
        for i in range(3):
            frame.grid_columnconfigure(i + button_column_start, weight=1)
        for i in range(button_row_start, button_row_end + 1):
            frame.grid_rowconfigure(i, weight=1)

        return frame

    def switch_to_standard(self):
        self.show_frame(self.standard_frame)
        
    def switch_to_scientific(self):
       self.show_frame(self.scientific_frame)
       
    def switch_to_currency(self):
        self.show_frame(self.currency_frame)

    def switch_to_volume(self):
        self.show_frame(self.volume_frame)

    def switch_to_length(self):
        self.show_frame(self.length_frame)

    def switch_to_weight_mass(self):
       self.show_frame(self.weightmass_frame)

    def switch_to_temperature(self):
        self.show_frame(self.temperature_frame)

    def switch_to_area(self):
        self.show_frame(self.area_frame)

    def switch_to_speed(self):
        self.show_frame(self.speed_frame)

    def switch_to_time(self):
        self.show_frame(self.time_frame)

    def switch_to_power(self):
        self.show_frame(self.power_frame)

    def switch_to_angle(self):
        self.show_frame(self.angle_frame)

    def switch_to_pressure(self):
        self.show_frame(self.pressure_frame)

    def switch_to_data(self):
        self.show_frame(self.data_frame)

    def standard_calculate(self):
        try:
            expression = self.e1.get()
            while '√' in expression:
                pos = expression.index('√')
                end_pos = pos + 1
                while end_pos < len(expression) and expression[end_pos] in '1234567890.':
                    end_pos += 1
                number = expression[pos + 1:end_pos]
                if not number:
                    raise ValueError("Syntax Error")
                expression = expression[:pos] + 'math.sqrt(' + number + ')' + expression[end_pos:]

            if expression.count('(') != expression.count(')'):
                    self.input_var.set("Error: Unmatched parentheses")
                    return
                
            expression = expression.replace('π', str(math.pi))
            result = eval(expression)

            self.e2.delete(0, tk.END)
            self.e2.config(state='normal')
            self.e2.insert(0, str(result))
        except ZeroDivisionError:
            self.e2.config(state='normal')
            self.e2.delete(0, tk.END)
            self.e2.insert(0, "Division by Zero error")
        except Exception as e:
            self.e2.delete(0, tk.END)
            self.e2.config(state='normal')
            self.e1.delete(0, tk.END)      

    def scientific_calculate(self):
        try:
            expression = self.e3.get()
            while '√' in expression:
                pos = expression.index('√')
                end_pos = pos + 1
                while end_pos < len(expression) and expression[end_pos] in '1234567890.':
                    end_pos += 1
                number = expression[pos + 1:end_pos]
                if not number:
                    raise ValueError("Syntax Error")
                expression = expression[:pos] + 'math.sqrt(' + number + ')' + expression[end_pos:]

            if expression.count('(') != expression.count(')'):
                    self.input_var.set("Error: Unmatched parentheses")
                    return

            # handle trigonometric functions
            for func in ['sin', 'cos', 'tan']:

                while func in expression:
                    pos = expression.index(func)
                    end_pos = pos + 4  

                    while end_pos < len(expression) and (expression[end_pos].isdigit() or expression[end_pos] in '.-'):
                        end_pos += 1
               
                    if end_pos < len(expression) and expression[end_pos] == ')':                   
                        number = expression[pos + 4:end_pos]  
                        if not number:  
                            raise ValueError("Syntax Error: No value provided for cosine")     
                        expression = expression[:pos] + 'math.'+func+'(math.radians(' + number + '))' + expression[end_pos + 1:]
                    else:
                        break

                for func in ['sinh', 'cosh', 'tanh','asin','acos','atan']:

                    while func in expression:
                        pos = expression.index(func)
                        end_pos = pos + 5  

                        while end_pos < len(expression) and (expression[end_pos].isdigit() or expression[end_pos] in '.-'):
                            end_pos += 1
                   
                        if end_pos < len(expression) and expression[end_pos] == ')':                   
                            number = expression[pos + 5:end_pos]  
                            if not number:  
                                raise ValueError("Syntax Error: No value provided for cosine")     
                            expression = expression[:pos] + 'math.'+func+'(math.radians(' + number + '))' + expression[end_pos + 1:]

                        else:
                            break             
                
            expression = expression.replace('π', str(math.pi))
            result = eval(expression)

            self.e4.delete(0, tk.END)
            self.e4.config(state='normal')
            self.e4.insert(0, str(result))
        except ZeroDivisionError:
            self.e4.config(state='normal')
            self.e4.delete(0, tk.END)
            self.e4.insert(0, "Division by Zero error")
        except Exception as e:
            self.e4.delete(0, tk.END)
            self.e4.config(state='normal')
            self.e3.delete(0, tk.END)    

    def add_to_expression1(self, value):
        self.e1.insert(tk.END, value)
        
    def add_to_expression2(self, value):
        self.e3.insert(tk.END, value)

    def delete_last_character1(self):
        current_text = self.e1.get()
        if current_text:
            self.e1.delete(len(current_text) - 1, tk.END)

    def delete_last_character2(self):
        current_text = self.e3.get()
        if current_text:
            self.e3.delete(len(current_text) - 1, tk.END)

    def delete_last_character3(self):
        current_text = self.e5.get()
        if current_text:
            self.e5.delete(len(current_text) - 1, tk.END)

    def delete_last_character4(self):
        current_text = self.e7.get()
        if current_text:
            self.e7.delete(len(current_text) - 1, tk.END)

    def delete_last_character5(self):
        current_text = self.e9.get()
        if current_text:
            self.e9.delete(len(current_text) - 1, tk.END)

    def delete_last_character6(self):
        current_text = self.e11.get()
        if current_text:
            self.e11.delete(len(current_text) - 1, tk.END)

    def delete_last_character7(self):
        current_text = self.e13.get()
        if current_text:
            self.e13.delete(len(current_text) - 1, tk.END)

    def delete_last_character8(self):
        current_text = self.e15.get()
        if current_text:
            self.e15.delete(len(current_text) - 1, tk.END)

    def delete_last_character9(self):
        current_text = self.e17.get()
        if current_text:
            self.e17.delete(len(current_text) - 1, tk.END)

    def delete_last_character10(self):
        current_text = self.e19.get()
        if current_text:
            self.e19.delete(len(current_text) - 1, tk.END)

    def delete_last_character11(self):
        current_text = self.e21.get()
        if current_text:
            self.e21.delete(len(current_text) - 1, tk.END)

    def delete_last_character12(self):
        current_text = self.e23.get()
        if current_text:
            self.e23.delete(len(current_text) - 1, tk.END)

    def delete_last_character13(self):
        current_text = self.e25.get()
        if current_text:
            self.e25.delete(len(current_text) - 1, tk.END)

    def delete_last_character14(self):
        current_text = self.e27.get()
        if current_text:
            self.e27.delete(len(current_text) - 1, tk.END)                

    def standard_sqrt(self):
        self.add_to_expression1('√')

    def standard_pi(self):
        self.add_to_expression1('π')

    def scientific_sqrt(self):
        self.add_to_expression2('√')

    def scientific_pi(self):
        self.add_to_expression2('π')

    def scientific_log(self):
        self.add_to_expression2('log(')

    def scientific_ln(self):
        self.add_to_expression2('ln(')

    def sin(self):
        self.add_to_expression2('sin(')

    def cos(self):
        self.add_to_expression2('cos(')

    def tan(self):
        self.add_to_expression2('tan(')

    def sinh(self):
        self.add_to_expression2('sinh(')

    def cosh(self):
        self.add_to_expression2('cosh(')

    def tanh(self):
        self.add_to_expression2('tanh(')
        
    def atan(self):
        self.add_to_expression2('atan(')

    def asin(self):
        self.add_to_expression2('asin(')

    def acos(self):
        self.add_to_expression2('acos(')  

    def standard_inverse(self):
        try:
            current_value = self.e1.get()
            if not current_value:
                raise ValueError("Syntax Error")
            num = float(current_value)
            if num == 0:
                raise ZeroDivisionError("Division by zero error")
            result = 1 / num
            self.e2.config(state="normal")
            self.e2.delete(0, tk.END)
            self.e2.insert(0, str(result))
        except Exception as e:
            self.e2.config(state="normal")
            self.e2.delete(0, tk.END)
            self.e2.insert(0, f"{e}")

    def scientific_inverse(self):
        try:
            current_value = self.e3.get()
            if not current_value:
                raise ValueError("Syntax Error")
            num = float(current_value)
            if num == 0:
                raise ZeroDivisionError("Division by zero error")
            result = 1 / num
            self.e4.config(state="normal")
            self.e4.delete(0, tk.END)
            self.e4.insert(0, str(result))
        except Exception as e:
            self.e4.config(state="normal")
            self.e4.delete(0, tk.END)
            self.e4.insert(0, f"{e}")

    def standard_square_power(self):
        try:
            current_value = self.e1.get()
            if not current_value:
                raise ValueError("syntax error")
            num = float(current_value)
            result = num ** 2
            self.e2.config(state="normal")
            self.e2.delete(0, tk.END)
            self.e2.insert(0, str(result))
        except Exception as e:
            self.e2.config(state="normal")
            self.e2.delete(0, tk.END)
            self.e2.insert(0, f"{e}")
            
    def scientific_square_power(self):
        try:
            current_value = self.e3.get()
            if not current_value:
                raise ValueError("syntax error")
            num = float(current_value)
            result = num ** 2
            self.e4.config(state="normal")
            self.e4.delete(0, tk.END)
            self.e4.insert(0, str(result))
        except Exception as e:
            self.e4.config(state="normal")
            self.e4.delete(0, tk.END)
            self.e4.insert(0, f"{e}")

    def factorial(self):
        try:
            current_value = self.e3.get()
            if not current_value:
                raise ValueError("Syntax error: No input provided.")
            num = int(current_value)  # Factorial is defined for non-negative integers only
            if num < 0:
                raise ValueError("Syntax error: Factorial is not defined for negative numbers.")
            
            result = math.factorial(num)  # Calculate factorial using math.factorial
            
            self.e4.config(state="normal")
            self.e4.delete(0, tk.END)
            self.e4.insert(0, str(result))
            
        except Exception as e:
            self.e4.config(state="normal")
            self.e4.delete(0, tk.END)
            self.e4.insert(0, f"{e}")
            
    def calculate_ln(self):
        try:
            current_value = self.e3.get()
            if not current_value:
                raise ValueError("Syntax error: No input provided.")
            num = float(current_value)  # Convert input to float
            if num <= 0:
                raise ValueError("Syntax error: Natural logarithm is not defined for non-positive numbers.")
            
            result = math.log(num)  # Calculate natural logarithm (base e)
            
            self.e4.config(state="normal")
            self.e4.delete(0, tk.END)
            self.e4.insert(0, str(round(result, 4)))  # Round the result for better readability       
            
        except Exception as e:
            self.e4.config(state="normal")
            self.e4.delete(0, tk.END)
            self.e4.insert(0, f"{e}")
            
    def calculate_log(self):
        try:
            current_value = self.e3.get()
            if not current_value:
                raise ValueError("Syntax error: No input provided.")
            num = float(current_value)  # Convert input to float
            if num <= 0:
                raise ValueError("Syntax error: Logarithm is not defined for non-positive numbers.")         

            result = math.log10(num)  # Calculate log base 10
         
            self.e4.config(state="normal")
            self.e4.delete(0, tk.END)
            self.e4.insert(0, str(round(result, 4)))  # Round the result for better readability
            
        except Exception as e:
            self.e4.config(state="normal")
            self.e4.delete(0, tk.END)
            self.e4.insert(0, f"{e}")

    def on_button_currency(self,number):
        current_value=self.e5.get()
        self.e5.delete(0,tk.END)
        self.e5.insert(0,current_value+str(number))

    def on_button_temperature(self,number):
        current_value=self.e7.get()
        self.e7.delete(0,tk.END)
        self.e7.insert(0,current_value+str(number))

    def on_button_power(self,number):
        current_value=self.e9.get()
        self.e9.delete(0,tk.END)
        self.e9.insert(0,current_value+str(number))
    
    def on_button_pressure(self,number):
        current_value=self.e11.get()
        self.e11.delete(0,tk.END)
        self.e11.insert(0,current_value+str(number))

    def on_button_data(self,number):
        current_value=self.e13.get()
        self.e13.delete(0,tk.END)
        self.e13.insert(0,current_value+str(number))

    def on_button_speed(self,number):
        current_value=self.e15.get()
        self.e15.delete(0,tk.END)
        self.e15.insert(0,current_value+str(number))

    def on_button_time(self,number):
        current_value=self.e17.get()
        self.e17.delete(0,tk.END)
        self.e17.insert(0,current_value+str(number))
        
    def on_button_length(self,number):
        current_value=self.e19.get()
        self.e19.delete(0,tk.END)
        self.e19.insert(0,current_value+str(number))

    def on_button_weightmass(self,number):
        current_value=self.e21.get()
        self.e21.delete(0,tk.END)
        self.e21.insert(0,current_value+str(number))

    def on_button_volume(self,number):
        current_value=self.e23.get()
        self.e23.delete(0,tk.END)
        self.e23.insert(0,current_value+str(number))

    def on_button_area(self,number):
        current_value=self.e25.get()
        self.e25.delete(0,tk.END)
        self.e25.insert(0,current_value+str(number))

    def on_button_angle(self,number):
        current_value=self.e27.get()
        self.e27.delete(0,tk.END)
        self.e27.insert(0,current_value+str(number))
        
    def convert_currency(self):
        conversion_rates = {
            'USD': {'INR': 82.50, 'EUR': 0.85, 'GBP': 0.75},
            'INR': {'USD': 0.012, 'EUR': 0.011, 'GBP': 0.009},
            'EUR': {'USD': 1.18, 'INR': 88.50, 'GBP': 0.88},
            'GBP': {'USD': 1.35, 'INR': 102.50, 'EUR': 1.14}
        }
        try:
            input_value = float(self.e5.get())  # Get input value (amount)
            from_currency = self.from_currency_combo.get()  # Get selected "from" currency
            to_currency = self.to_currency_combo.get()      # Get selected "to" currency
            
            # Get the conversion rate
            if from_currency == to_currency:
                output_value = input_value  # Same currency conversion
            else:
                output_value = input_value * conversion_rates[from_currency][to_currency]
            
            # Display the converted value
            self.e6.delete(0, tk.END)  # Clear the output entry
            self.e6.insert(0, str(round(output_value, 2)))  # Insert the output value rounded to 2 decimal places

        except ValueError:
            self.e6.delete(0, tk.END)  # Clear the output entry in case of error
            self.e6.insert(0, "Invalid input")  # Show error message

    def convert_temperature(self):
        try:
            input_value = float(self.e7.get())  # Get input value
            from_scale = self.from_temperature_combo.get()    # Get selected scale from input
            to_scale = self.to_temperature_combo.get()      # Get selected scale for output
            
            # Convert input value to Celsius for comparison
            if from_scale == 'Celsius':
                celsius_value = input_value
            elif from_scale == 'Fahrenheit':
                celsius_value = (input_value - 32) * 5.0 / 9.0
            elif from_scale == 'Kelvin':
                celsius_value = input_value - 273.15

            # Convert Celsius to the selected output scale
            if to_scale == 'Celsius':
                output_value = celsius_value
            elif to_scale == 'Fahrenheit':
                output_value = (celsius_value * 9.0 / 5.0) + 32
            elif to_scale == 'Kelvin':
                output_value = celsius_value + 273.15
            
            # Display the converted value
            self.e8.delete(0, tk.END)  # Clear the output entry
            self.e8.insert(0, str(round(output_value, 2)))  # Insert the output value rounded to 2 decimal places

        except ValueError:
            self.e8.delete(0, tk.END)  # Clear the output entry in case of error
            self.e8.insert(0, "Invalid input")  # Show error message

    # Function to convert power
    def convert_power(self):
        power_conversion_factors = {
        'Watts': 1,
        'Kilowatts': 1000,
        'Horsepower': 745.7
        }
        try:
            input_value = float(self.e9.get())  # Get input value (power)
            from_power_unit = self.from_power_combo.get()  # Get selected "from" power unit
            to_power_unit = self.to_power_combo.get()      # Get selected "to" power unit
            
            # Convert input value to watts
            input_in_watts = input_value * power_conversion_factors[from_power_unit]
            
            # Convert from watts to the desired output power unit
            output_value = input_in_watts / power_conversion_factors[to_power_unit]
            
            # Display the converted value
            self.e10.delete(0, tk.END)  # Clear the output entry
            self.e10.insert(0, str(round(output_value, 2)))  # Insert the output value rounded to 2 decimal places

        except ValueError:
            self.e10.delete(0, tk.END)  # Clear the output entry in case of error
            self.e10.insert(0, "Invalid input")  # Show error message

    def convert_pressure(self):
        pressure_conversion_factors = {
            'Pascals (Pa)': 1,
            'Bar': 100000,
            'Atmospheres (atm)': 101325,
            'Pounds per square inch (psi)': 6894.757
        }
        try:
            input_value = float(self.e11.get())
            from_pressure_unit = self.from_pressure_combo.get()
            to_pressure_unit = self.to_pressure_combo.get()

            # Convert input to pascals first
            input_in_pascals = input_value * pressure_conversion_factors[from_pressure_unit]
            output_value = input_in_pascals / pressure_conversion_factors[to_pressure_unit]

            self.e12.delete(0, tk.END)
            self.e12.insert(0, str(round(output_value, 2)))

        except ValueError:
            self.e12.delete(0, tk.END)
            self.e12.insert(0, "Invalid input")

    def convert_data(self):
        data_conversion_factors = {
            'Bytes (B)': 1,
            'Kilobytes (KB)': 1024,
            'Megabytes (MB)': 1024**2,
            'Gigabytes (GB)': 1024**3,
            'Terabytes (TB)': 1024**4
        }
        try:
            input_value = float(self.e13.get())
            from_data_unit = self.from_data_combo.get()
            to_data_unit = self.to_data_combo.get()

            # Convert input to bytes first
            input_in_bytes = input_value * data_conversion_factors[from_data_unit]
            output_value = input_in_bytes / data_conversion_factors[to_data_unit]

            self.e14.delete(0, tk.END)
            self.e14.insert(0, str(round(output_value, 4)))

        except ValueError:
            self.e14.delete(0, tk.END)
            self.e14.insert(0, "Invalid input")
            
    def convert_speed(self):
        speed_conversion_factors = {
            'Meters per second (m/s)': 1,
            'Kilometers per hour (km/h)': 1/3.6,
            'Miles per hour (mph)': 1/2.237
        }
        try:
            input_value = float(self.e15.get())
            from_speed_unit = self.from_speed_combo.get()
            to_speed_unit = self.to_speed_combo.get()

            # Convert input to m/s first
            input_in_mps = input_value * speed_conversion_factors[from_speed_unit]
            output_value = input_in_mps / speed_conversion_factors[to_speed_unit]

            self.e16.delete(0, tk.END)
            self.e16.insert(0, str(round(output_value, 4)))

        except ValueError:
            self.e16.delete(0, tk.END)
            self.e16.insert(0, "Invalid input")

    def convert_time(self):
        time_conversion_factors = {
            'Seconds': 1,
            'Minutes': 60,
            'Hours': 3600,
            'Days': 86400
        }
        try:
            input_value = float(self.e17.get())  # Get input value (time)
            from_time_unit = self.from_time_combo.get()  # Get selected "from" time unit
            to_time_unit = self.to_time_combo.get()      # Get selected "to" time unit
            
            # Convert input value to seconds
            input_in_seconds = input_value * time_conversion_factors[from_time_unit]
            
            # Convert from seconds to the desired output time unit
            output_value = input_in_seconds / time_conversion_factors[to_time_unit]
            
            # Display the converted value
            self.e18.delete(0, tk.END)  # Clear the output entry
            self.e18.insert(0, str(round(output_value, 2)))  # Insert the output value rounded to 2 decimal places

        except ValueError:
            self.e18.delete(0, tk.END)  # Clear the output entry in case of error
            self.e18.insert(0, "Invalid input")  # Show error message

    def convert_length(self):
        length_conversion_factors= {
            'Meters': 1,
            'Kilometers': 1000,
            'Centimeters': 0.01,
            'Miles': 1609.34,
            'Feet': 0.3048
            }
        try:
            input_value = float(self.e19.get())
            from_length_unit = self.from_length_combo.get()  
            to_length_unit = self.to_length_combo.get()      
            
            input_in_meters = input_value * length_conversion_factors[from_length_unit]
            
            output_value = input_in_meters / length_conversion_factors[to_length_unit]
            
            self.e20.delete(0, tk.END)  
            self.e20.insert(0, str(round(output_value, 4)))  

        except ValueError:
            self.e20.delete(0, tk.END)  
            self.e20.insert(0, "Invalid input")  

    def convert_weightmass(self):
        weightmass_conversion_factors= {
        'Grams': 1,
        'Kilograms': 1000,
        'Pounds': 453.592,
        'Ounces': 28.3495
        }
        try:
            input_value = float(self.e21.get())
            from_weightmass_unit = self.from_weightmass_combo.get()  
            to_weightmass_unit = self.to_weightmass_combo.get()      
            
            input_in_mm = input_value * weightmass_conversion_factors[from_weightmass_unit]
            
            output_value = input_in_mm / weightmass_conversion_factors[to_weightmass_unit]
            
            self.e22.delete(0, tk.END)  
            self.e22.insert(0, str(round(output_value, 2)))  

        except ValueError:
            self.e22.delete(0, tk.END)  
            self.e22.insert(0, "Invalid input")  

    def convert_volume(self):
        volume_conversion_factors= {
            'Milliliters': 1,
            'Liters': 1000,
            'Cubic meters': 1000000.0,
            'Cubic centimeters': 1
        }
        try:
            input_value = float(self.e23.get())
            from_volume_unit = self.from_volume_combo.get()  
            to_volume_unit = self.to_volume_combo.get()      
            
            input_in_ml = input_value * volume_conversion_factors[from_volume_unit]
            
            output_value = input_in_ml / volume_conversion_factors[to_volume_unit]
            
            self.e24.delete(0, tk.END)  
            self.e24.insert(0, str(round(output_value, 4)))  

        except ValueError:
            self.e24.delete(0, tk.END)  
            self.e24.insert(0, "Invalid input")  

    def convert_area(self):
        area_conversion_factors={
        'Square meters': 1,
        'Square kilometers': 1000000.0,
        'Square feet': 0.092903,
        'Acres': 4046.86
        }
        try:
            input_value = float(self.e25.get())
            from_area_unit = self.from_area_combo.get()  
            to_area_unit = self.to_area_combo.get()      
            
            input_in_sqm = input_value * area_conversion_factors[from_area_unit]
            
            output_value = input_in_sqm / area_conversion_factors[to_area_unit]
            
            self.e26.delete(0, tk.END)  
            self.e26.insert(0, str(round(output_value, 4)))  

        except ValueError:
            self.e26.delete(0, tk.END)  
            self.e26.insert(0, "Invalid input")  

    def convert_angle(self):
        angle_conversion_factors= {
            'Degrees': 1,
            'Radians': 57.2958,
            'Gradians': 0.9
        }
        try:
            input_value = float(self.e27.get())
            from_angle_unit = self.from_angle_combo.get()  
            to_angle_unit = self.to_angle_combo.get()      
            
            input_in_degree = input_value * angle_conversion_factors[from_angle_unit]
            
            output_value = input_in_degree / angle_conversion_factors[to_angle_unit]
            
            self.e28.delete(0, tk.END)  
            self.e28.insert(0, str(round(output_value, 4)))  

        except ValueError:
            self.e28.delete(0, tk.END)  
            self.e28.insert(0, "Invalid input")

window = tk.Tk()
calculator_app = CalculatorApp(window)
window.mainloop()
