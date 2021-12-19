#!/usr/bin/python3

import json
import random
import sha_hash


# Iterating through the json
# list
#for i in data['chapters']:
#	for x in i['verses']:
#		print(i['chapter'] + ':' + x['verse'] + ' ' + x['text'])
# Closing file


def quote(json_path, original_hash):
    #random.choice(quote_list(json_path, original_hash)[0])
    q_list, rand_index = quote_list(json_path, original_hash)    
    return q_list[rand_index]

def quote_list(json_path, original_hash):
    if not sha_hash.sha512_ok(json_path, original_hash):
        return (['Quote File Checksum Incorrect.'], 0)

    with open(json_path) as f:
        # returns JSON object as
        # a dictionary
        data = json.load(f)
        quotes = [ f"{x['text']} ({i['chapter']}:{x['verse']})" for i in data['chapters'] for x in i['verses'] ]

    return (quotes, random.randint(0, len(quotes) - 1))

def main():
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Proverbs", quote('/home/amir/Documents/proverbs.json', 'fef08fec8be3919359bb0780c0e3320d37f49997f6dcd3e2cbf54ecc45a8c912eec80abcec9f394a295b0b16889bfbe2a90a2ca6530ab3a79a45c222168a46d9'))
    root.destroy()


if __name__ == '__main__':
    main()

