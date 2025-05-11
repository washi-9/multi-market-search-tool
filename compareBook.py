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


# GUI構築
root = tk.Tk()
root.title("Amazon商品検索オープナー")
root.geometry("400x150")

label = tk.Label(root, text="Amazonで検索したい商品名を入力してください：")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack()

amazon_search_button = tk.Button(root, text="Amazonで検索ページを開く", command=open_amazon_search)
amazon_search_button.pack(pady=10)

mercari_search_button = tk.Button(root, text="メルカリで検索ページを開く", command=open_mercali_search)
mercari_search_button.pack(pady=10)

root.mainloop()
