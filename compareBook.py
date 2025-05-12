import tkinter as tk
from tkinter import messagebox
import urllib.parse
import webbrowser
import os

# 検索履歴リスト
HISTORY_FILE = "history.txt"
search_history = []

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            for line in f:
                keyword = line.strip()
                if keyword:
                    search_history.append(keyword)
                    history_listbox.insert(tk.END, keyword)  # 履歴をリストボックスに追加

def save_history():
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        for keyword in search_history:
            f.write(keyword + "\n")

def open_selected_searches():
    product_name = entry.get()
    if not product_name.strip():
        messagebox.showerror("エラー", "商品名を入力してください")
        return
    
    # 履歴に追加（重複回避）
    if product_name not in search_history:
        search_history.insert(0, product_name)  # 新しい履歴を先頭に
        history_listbox.insert(0, product_name)

    encoded_name = urllib.parse.quote(product_name)

    # チェックされたサイトのみ検索
    if site_vars["Amazon"].get():
        webbrowser.open(f"https://www.amazon.co.jp/s?k={encoded_name}")
    if site_vars["メルカリ"].get():
        webbrowser.open(f"https://jp.mercari.com/search?keyword={encoded_name}&status=on_sale")
    if site_vars["ヤフーフリマ"].get():
        webbrowser.open(f"https://paypayfleamarket.yahoo.co.jp/search/{encoded_name}?open=1")
    if site_vars["OPAC"].get():
        webbrowser.open(f"https://opac.library.osaka-u.ac.jp/opac/opac_search/?lang=0&amode=2&appname=Netscape&version=5&cmode=0&smode=0&kywd={encoded_name}&index_amazon_s=Books&node_s=")

# すべて選択
def select_all():
    for var in site_vars.values():
        var.set(True)

# すべて解除
def deselect_all():
    for var in site_vars.values():
        var.set(False)

def on_history_select(event):
    # 選択された履歴項目を入力欄にセット
    selected = history_listbox.curselection()
    if selected:
        entry.delete(0, tk.END)
        entry.insert(0, history_listbox.get(selected[0]))


# GUI構築
root = tk.Tk()
root.title("商品検索オープナー")
root.geometry("500x500")


tk.Label(root, text="商品名を入力してください：").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack()

# チェックボックス作成
site_vars = {
    "Amazon": tk.BooleanVar(value=True),
    "メルカリ": tk.BooleanVar(value=True),
    "ヤフーフリマ": tk.BooleanVar(value=True),
    "OPAC": tk.BooleanVar(value=False)
}

tk.Label(root, text="検索するサイトを選択：").pack(pady=10)
for name, var in site_vars.items():
    cb = tk.Checkbutton(root, text=name, variable=var)
    cb.pack(anchor='w', padx=20)

# すべて選択・解除ボタン
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

select_all_button = tk.Button(btn_frame, text="すべて選択", command=select_all)
select_all_button.pack(side='left', padx=10)

deselect_all_button = tk.Button(btn_frame, text="すべて解除", command=deselect_all)
deselect_all_button.pack(side='left', padx=10)

# 検索ボタン
search_button = tk.Button(root, text="選択したサイトで検索", command=open_selected_searches)
search_button.pack(pady=20)

# 履歴表示
tk.Label(root, text="検索履歴：").pack(pady=5)
history_listbox = tk.Listbox(root, height=8, width=50)
history_listbox.pack()
history_listbox.bind("<<ListboxSelect>>", on_history_select)

# 履歴の読み込み
load_history()

# 終了時に履歴保存
root.protocol("WM_DELETE_WINDOW", lambda: (save_history(), root.destroy()));

root.mainloop()
