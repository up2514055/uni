import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime


class TypingLoggerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Logger (App-only, Focused Window)")
        self.root.geometry("700x450")

        self.is_logging = tk.BooleanVar(value=False)

        info = (
            "This app logs keys ONLY while this window is focused.\n"
            "Use Start/Stop to control logging."
        )
        tk.Label(self.root, text=info, justify="left").pack(anchor="w", padx=10, pady=8)

        controls = tk.Frame(self.root)
        controls.pack(fill="x", padx=10)

        tk.Button(controls, text="Start logging", command=self.start).pack(side="left")
        tk.Button(controls, text="Stop logging", command=self.stop).pack(side="left", padx=6)
        tk.Button(controls, text="Clear", command=self.clear).pack(side="left", padx=6)
        tk.Button(controls, text="Save to file", command=self.save).pack(side="left", padx=6)

        self.status = tk.Label(self.root, text="Status: NOT logging", fg="red")
        self.status.pack(anchor="w", padx=10, pady=(6, 0))

        self.text = tk.Text(self.root, wrap="word")
        self.text.pack(expand=True, fill="both", padx=10, pady=10)

        # Bind key events only for this window/widget
        self.text.bind("<Key>", self.on_key)

    def start(self):
        self.is_logging.set(True)
        self.status.config(text="Status: LOGGING (focused window only)", fg="green")
        self.text.focus_set()

    def stop(self):
        self.is_logging.set(False)
        self.status.config(text="Status: NOT logging", fg="red")

    def clear(self):
        self.text.delete("1.0", "end")

    def save(self):
        content = self.text.get("1.0", "end-1c")
        if not content.strip():
            messagebox.showinfo("Nothing to save", "There is no text to save.")
            return

        default_name = f"typing_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            initialfile=default_name,
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if not path:
            return

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        messagebox.showinfo("Saved", f"Saved to:\n{path}")

    def on_key(self, event):
        # Only log if the user pressed Start
        if not self.is_logging.get():
            return

        # This handler runs only when this app has focus
        # We let Tkinter insert the character naturally, so no extra action needed.
        # But we can optionally tag special keys:
        if event.keysym in ("Return", "BackSpace", "Tab", "Escape"):
            # Insert a readable marker (optional)
            # Comment out if you don't want markers
            marker = {
                "Return": "\n",
                "Tab": "\t",
                "BackSpace": "",  # backspace handled by widget
                "Escape": ""
            }.get(event.keysym, "")
            if marker:
                # Let Tk handle normal behavior; we don't override.
                pass

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    TypingLoggerApp().run()
