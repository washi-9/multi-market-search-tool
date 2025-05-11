import tkinter as tk
from tkinter import messagebox
import urllib.parse
import webbrowser

def open_amazon_search():
    product_name = entry.get()
    if not product_name.strip():
        messagebox.showerror("エラー", "商品名を入力してください")
        return
    # 商品名をURLエンコードして検索URL作成
    encoded_name = urllib.parse.quote(product_name)
    search_url = f"https://www.amazon.co.jp/s?k={encoded_name}"
    webbrowser.open(search_url)

def open_mercali_search():
    product_name = entry.get()
    if not product_name.strip():
        messagebox.showerror("エラー", "商品名を入力してください")
        return
    # 商品名をURLエンコードして検索URL作成
    encoded_name = urllib.parse.quote(product_name)
    search_url = f"https://jp.mercari.com/search?keyword={encoded_name}&status=on_sale"
    webbrowser.open(search_url)

def open_opac_search():
    product_name = entry.get()
    if not product_name.strip():
        messagebox.showerror("エラー", "商品名を入力してください")
        return
    # 商品名をURLエンコードして検索URL作成
    encoded_name = urllib.parse.quote(product_name)
    search_url = f"https://opac.library.osaka-u.ac.jp/opac/opac_search/?lang=0&amode=2&appname=Netscape&version=5&cmode=0&smode=0&kywd={encoded_name}&index_amazon_s=Books&node_s="
    webbrowser.open(search_url)

def open_yahoo_search():
    product_name = entry.get()
    if not product_name.strip():
        messagebox.showerror("エラー", "商品名を入力してください")
        return
    # 商品名をURLエンコードして検索URL作成
    encoded_name = urllib.parse.quote(product_name)
    search_url = f"https://paypayfleamarket.yahoo.co.jp/search/{encoded_name}?open=1"
    webbrowser.open(search_url)

# GUI構築
root = tk.Tk()
root.title("商品検索オープナー")
root.geometry("500x300")

label = tk.Label(root, text="Amazonで検索したい商品名を入力してください：")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack()

sites = {
    "Amazon": open_amazon_search,
    "メルカリ": open_mercali_search,
    "ヤフーフリマ": open_yahoo_search,
    "OPAC": open_opac_search
}

for name, func in sites.items():
    btn = tk.Button(root, text=f"{name}で検索ページを開く", command=func)
    btn.pack(pady=10)
root.mainloop()
