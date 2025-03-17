

tk.Label(root, text="Ievadiet e-pasta adresi:").pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)
tk.Button(root, text="Pārbaudīt", command=paarbaude_email).pack(pady=5)


tk.Label(root, text="Ievadiet vārdu:").pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)
tk.Button(root, text="Pārbaudīt", command=paarbaude_email).pack(pady=5)

tk.Label(root, text="Ievadiet uzvārdu:").pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)
tk.Button(root, text="Pārbaudīt", command=paarbaude_email).pack(pady=5)

tk.Label(root, text="Ievadiet personas kodu:").pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)
tk.Button(root, text="Pārbaudīt", command=paarbaude_email).pack(pady=5)

tk.Label(root, text="Ievadiet adresi:").pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)
tk.Button(root, text="Pārbaudīt", command=paarbaude_email).pack(pady=5)

tk.Label(root, text="Ievadiet tālruni:").pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)
tk.Button(root, text="Pārbaudīt", command=paarbaude_email).pack(pady=5)
root.mainloop()
