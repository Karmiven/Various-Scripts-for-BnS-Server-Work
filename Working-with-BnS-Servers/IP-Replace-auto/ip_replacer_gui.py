import os
import socket
import re
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import threading

ENCODINGS = ['utf-8', 'utf-16', 'utf-8-sig', 'cp1251', 'iso-8859-1']

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def read_file_with_encodings(filepath):
    for enc in ENCODINGS:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                return f.read(), enc
        except Exception:
            continue
    raise UnicodeDecodeError("Unable to decode with known encodings.")

def write_file_with_encoding(filepath, content, encoding):
    with open(filepath, 'w', encoding=encoding) as f:
        f.write(content)

def replace_ips_in_files(folder, old_ips, new_ip, progress_callback, done_callback):
    log_lines = []
    replaced_files = 0
    replaced_total = 0

    all_files = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(('.xml', '.ini')):
                all_files.append(os.path.join(root, file))

    total_files = len(all_files)

    for i, filepath in enumerate(all_files):
        try:
            content, encoding = read_file_with_encodings(filepath)
            original_lines = content.splitlines()
            new_lines = []
            changed = False
            replaced_in_file = 0

            for line in original_lines:
                original_line = line
                for old_ip in old_ips:
                    if old_ip in line:
                        line = line.replace(old_ip, new_ip)
                if line != original_line:
                    new_lines.append(f">>> {line}")
                    replaced_in_file += 1
                    changed = True
                else:
                    new_lines.append(line)

            if changed:
                write_file_with_encoding(filepath, "\n".join([l[4:] if l.startswith(">>> ") else l for l in new_lines]), encoding)
                replaced_files += 1
                replaced_total += replaced_in_file
                log_lines.append(f"✅ {os.path.basename(filepath)} — replaced {replaced_in_file} lines (encoding: {encoding})")
                log_lines.extend([line for line in new_lines if line.startswith(">>> ")])
            else:
                log_lines.append(f"— {os.path.basename(filepath)} — no matches found")

        except Exception as e:
            log_lines.append(f"❌ Error in file {filepath}: {e}")

        progress = int((i + 1) / total_files * 100)
        progress_callback(progress)

    log_lines.append(f"\n🟢 Done: IP replaced in {replaced_files} file(s)")
    log_lines.append(f"📌 Total IP lines replaced: {replaced_total}")
    done_callback("\n".join(log_lines))

def browse_folder():
    selected = filedialog.askdirectory()
    if selected:
        folder_path.set(selected)

def start_replacement():
    folder = folder_path.get()
    if not folder or not os.path.isdir(folder):
        messagebox.showerror("Error", "Select a valid folder.")
        return

    input_text = old_ips_entry.get().strip()
    if not input_text:
        messagebox.showerror("Error", "Enter at least one IP address to replace.")
        return

    old_ips = [ip.strip() for ip in re.split(r'[,\s]+', input_text) if ip.strip()]
    if not old_ips:
        messagebox.showerror("Error", "Invalid IP format.")
        return

    # Получить IP
    new_ip = ip_var.get()
    if ip_mode.get() == "manual":
        if not re.match(r'^\d{1,3}(\.\d{1,3}){3}$', new_ip):
            messagebox.showerror("Error", "Invalid manual IP format.")
            return

    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"🔍 Starting replacement to {new_ip}...\n")

    progress_bar["value"] = 0
    progress_bar.update()

    def update_progress(p):
        progress_bar["value"] = p
        progress_bar.update()

    def show_result(log):
        output_text.after(0, lambda: output_text.insert(tk.END, f"\n{log}"))

    threading.Thread(
        target=replace_ips_in_files,
        args=(folder, old_ips, new_ip, update_progress, show_result),
        daemon=True
    ).start()

def update_ip_mode():
    if ip_mode.get() == "auto":
        ip_var.set(get_local_ip())
        ip_entry.configure(state="readonly")
    else:
        ip_entry.configure(state="normal")

# === GUI ===
root = tk.Tk()
root.title("IP Address Replacer")
root.geometry("760x580")
root.resizable(False, False)

ip_var = tk.StringVar(value=get_local_ip())
folder_path = tk.StringVar()
ip_mode = tk.StringVar(value="auto")

frame_top = tk.Frame(root)
frame_top.pack(pady=10)

tk.Label(frame_top, text="Replacement IP address:").grid(row=0, column=0, sticky="w")
ip_entry = tk.Entry(frame_top, textvariable=ip_var, width=20, state="readonly")
ip_entry.grid(row=0, column=1, padx=5)

tk.Radiobutton(frame_top, text="Auto (from PC)", variable=ip_mode, value="auto", command=update_ip_mode).grid(row=0, column=2, padx=5)
tk.Radiobutton(frame_top, text="Manual", variable=ip_mode, value="manual", command=update_ip_mode).grid(row=0, column=3)

tk.Label(frame_top, text="Old IP(s) to replace (separated by space or comma):").grid(row=1, column=0, columnspan=4, sticky="w", pady=(10, 0))
old_ips_entry = tk.Entry(frame_top, width=60)
old_ips_entry.grid(row=2, column=0, columnspan=4, padx=5, pady=(0, 10))

frame_folder = tk.Frame(root)
frame_folder.pack(pady=5)
tk.Label(frame_folder, text="Selected folder:").pack(side="left", padx=(0, 5))
tk.Entry(frame_folder, textvariable=folder_path, width=60, state="readonly").pack(side="left", padx=(0, 5))
tk.Button(frame_folder, text="Choose Folder", command=browse_folder).pack(side="left")

tk.Button(root, text="Start Replacement", command=start_replacement, width=25).pack(pady=(5, 10))

progress_bar = ttk.Progressbar(root, orient="horizontal", length=730, mode="determinate")
progress_bar.pack(pady=(0, 10), padx=10)

output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=20)
output_text.pack(padx=10, pady=10)

update_ip_mode()
root.mainloop()
