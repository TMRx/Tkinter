import tkinter as tk
from tkinter import ttk
# import sqlite3
# import os
import requests
import json
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# root = tk.Tk()
window = tk.Tk()
window.title("Chart Application")

# window.geometry('500x500')
# window.minsize(400, 400)


# frame_add_form = tk.Frame(window, width=200, height=200, bg='green')
# frame_statistic = tk.Frame(window, width=200, height=200, bg='yellow')
# frame_list = tk.Frame(window, width=400, height=200, bg='red')
frame_add_form = tk.Frame(window, bg='green')
frame_statistic = tk.Frame(window, bg='yellow')
frame_list = tk.Frame(window)

frame_add_form.grid(column=0, row=0, sticky='ns')
frame_statistic.grid(column=1, row=0)
frame_list.grid(column=0, row=1, columnspan=2, sticky='we')

fig = plt.Figure()
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=frame_add_form)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def update_plot():
    url = 'https://api.coinbase.com/v2/prices/BTC-USD/spot'
    response = requests.get(url)
    data = json.loads(response.text)
    btc_price = float(data['data']['amount'])
    
    url = 'https://api.coinbase.com/v2/prices/ETH-USD/spot'
    response = requests.get(url)
    data = json.loads(response.text)
    eth_price = float(data['data']['amount'])
    
    now = time.strftime("%H:%M:%S")
    ax.scatter(now, btc_price, color='orange')
    ax.scatter(now, eth_price, color='blue')
    
    ax.set_title('Bitcoin & Ethereum Price (USD)')
    ax.set_xlabel('Time')
    ax.set_ylabel('Price (USD)')
    ax.set_xlim(left=max(0, ax.get_xlim()[1]-10), right=ax.get_xlim()[1]+5)
    ax.grid()
    
    canvas.draw()
    
    frame_add_form.after(5000, update_plot)
    
update_plot()
    
    


l_most_common_text= tk.Label(frame_statistic, text='Most common item')
l_most_common_value= tk.Label(frame_statistic, text='Food', font='Arial, 15')
l_exp_item_text= tk.Label(frame_statistic, text='Most Expensive item')
l_exp_item_value= tk.Label(frame_statistic, text='Gift', font='Arial, 15')
l_exp_day_text= tk.Label(frame_statistic, text='Most expensive day')
l_exp_day_value= tk.Label(frame_statistic, text='Friday', font='Arial, 15')
l_exp_month_text= tk.Label(frame_statistic, text='Most expensive month')
l_exp_month_value= tk.Label(frame_statistic, text='August', font='Arial, 15')

l_most_common_text.grid(row=0, column=0, sticky='w', padx=10, pady=10)
l_most_common_value.grid(row=0, column=1, sticky='e', padx=10, pady=10)
l_exp_item_text.grid(row=1, column=0, sticky='w', padx=10, pady=10)
l_exp_item_value.grid(row=1, column=1, sticky='e', padx=10, pady=10)
l_exp_day_text.grid(row=2, column=0, sticky='w', padx=10, pady=10)
l_exp_day_value.grid(row=2, column=1, sticky='e', padx=10, pady=10)
l_exp_month_text.grid(row=3, column=0, sticky='w', padx=10, pady=10)
l_exp_month_value.grid(row=3, column=1, sticky='e', padx=10, pady=10)

l_temp_add_form = tk.Label(frame_add_form, text='frame_add_form')
# l_temp_frame_list = tk.Label(frame_list, text='frame_list')
l_temp_add_form.pack(expand=True, padx=20, pady=20)
# l_temp_frame_list.pack(expand=True, padx=20, pady=20)

table = ttk.Treeview(frame_list, show='headings')
table['columns'] = ['Name', 'Age', 'Gender']
table.heading('#0', text='ID')
table.heading('Name', text='Name')
table.heading('Age', text='Age')
table.heading('Gender', text='Gender')
# table.heading('Quantity', text='Quantity')
table.insert(parent='', index='end', iid='0', text='1', values=('John', 28))
table.insert(parent='', index='end', iid='1', text='2', values=('Alice', 24))
table.insert(parent='', index='end', iid='2', text='3', values=('Bob', 32))
table.insert(parent='', index='end', iid='3', text='4', values=('Charlie', 18))
table.insert(parent='', index='end', iid='4', text='5', values=('John', 28))
table.insert(parent='', index='end', iid='5', text='6', values=('Alice', 24))
table.insert(parent='', index='end', iid='6', text='7', values=('Bob', 32))
table.insert(parent='', index='end', iid='7', text='8', values=('Charlie', 18))
table.insert(parent='', index='end', iid='8', text='9', values=('John', 28))
table.insert(parent='', index='end', iid='9', text='10', values=('Alice', 24))
table.insert(parent='', index='end', iid='10', text='11', values=('Bob', 32))
table.insert(parent='', index='end', iid='11', text='12', values=('Charlie', 18))

scroll_panel = ttk.Scrollbar(frame_list, command=table.yview, orient='vertical')
table.configure(yscrollcommand=scroll_panel.set)
scroll_panel.pack(side=tk.RIGHT, fill=tk.Y)
table.pack()


def delete_row():
    for selection in table.selection():
        table.delete(selection)
         
delete_button = tk.Button(frame_list, text='Видалити рядок', command=delete_row)
delete_button.pack(side=tk.RIGHT, padx=10, pady=10)




window.mainloop()


    