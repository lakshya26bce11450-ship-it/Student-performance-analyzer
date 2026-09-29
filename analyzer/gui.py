"""Tkinter user interface. Layout and colours are the same as the original app."""
import tkinter as tk
from tkinter import messagebox, ttk

from analyzer import config, history
from analyzer.calculator import calculate_result, format_result
from analyzer.logger_setup import get_logger
from analyzer.validators import ValidationError, parse_marks

log = get_logger()


class AnalyzerApp:
    def __init__(self, window):
        self.window = window
        self.entries = []
        self.last_marks = None
        self.last_result = None
        self._setup_window()
        self._build_widgets()

    # ---------- window & widgets ----------
    def _setup_window(self):
        w = self.window
        w.title(config.APP_TITLE)
        width, height = 520, 760
        x = (w.winfo_screenwidth() - width) // 2
        y = (w.winfo_screenheight() - height) // 2
        w.geometry(f"{width}x{height}+{x}+{y}")
        w.config(bg=config.APP_BG)

    def _build_widgets(self):
        w = self.window
        tk.Label(w, text="Performance Analyzer", font=("Arial", 20, "bold"),
                 bg=config.TITLE_BG, fg=config.TITLE_FG, padx=14, pady=10
                 ).pack(pady=20)
        tk.Label(w, text="Enter marks out of 100\nPass marks in every subject: "
                 + str(config.PASS_MARK), font=("Arial", 13, "bold"),
                 bg=config.APP_BG, fg=config.TEXT_COLOR).pack(pady=5)

        form = tk.Frame(w, bg=config.APP_BG)
        form.pack(pady=10)
        self.name_entry = self._make_row(form, "Student Name", 0)
        for i, subject in enumerate(config.SUBJECTS, start=1):
            self.entries.append(self._make_row(form, subject, i))

        self._button("Calculate Result", self.calculate, config.PRIMARY_BUTTON,
                     "#1D4ED8", 14, 20).pack(pady=10)
        self._button("Clear", self.clear, config.SECONDARY_BUTTON,
                     "#475569", 13, 12).pack(pady=2)

        self.result_label = tk.Label(
            w, text="", font=("Arial", 15, "bold"), bg=config.RESULT_BG,
            fg=config.RESULT_FG, padx=14, pady=8, justify="left")
        self.result_label.pack(pady=15)

        row = tk.Frame(w, bg=config.APP_BG)
        row.pack(pady=5)
        self._button("Save Record", self.save, config.PRIMARY_BUTTON,
                     "#1D4ED8", 12, 14, row).grid(row=0, column=0, padx=6)
        self._button("View History", self.show_history, config.SECONDARY_BUTTON,
                     "#475569", 12, 14, row).grid(row=0, column=1, padx=6)

    def _make_row(self, form, text, row):
        tk.Label(form, text=text, font=("Arial", 14, "bold"), bg=config.APP_BG,
                 fg=config.TEXT_COLOR, width=14, anchor="w"
                 ).grid(row=row, column=0, padx=12, pady=9)
        entry = tk.Entry(form, font=("Arial", 14, "bold"), width=14,
                         justify="center", bg=config.INPUT_BG, fg=config.TEXT_COLOR)
        entry.grid(row=row, column=1, padx=12, pady=9)
        return entry

    def _button(self, text, command, bg, active_bg, size, width, parent=None):
        return tk.Button(parent or self.window, text=text, command=command,
                         font=("Arial", size, "bold"), bg=bg, fg="white",
                         activebackground=active_bg, activeforeground="white",
                         width=width)

    # ---------- actions ----------
    def calculate(self):
        """Runs when the Calculate button is clicked."""
        try:
            marks = parse_marks([e.get() for e in self.entries])
        except ValidationError as err:
            log.warning("Validation failed: %s", err.message)
            messagebox.showerror(err.title, err.message)
            return
        res = calculate_result(marks)
        self.last_marks, self.last_result = marks, res
        self.result_label.config(text=format_result(res))
        log.info("Calculated: marks=%s -> %s (%s)", marks, res.result, res.grade)

    def clear(self):
        for entry in [self.name_entry] + self.entries:
            entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.last_marks = self.last_result = None

    def save(self):
        if self.last_result is None:
            messagebox.showwarning("Nothing to save", "Please calculate a result first.")
            return
        name = self.name_entry.get().strip() or "Unknown"
        try:
            history.save_record(name, self.last_marks, self.last_result)
        except OSError as err:
            log.error("Could not save record: %s", err)
            messagebox.showerror("Save failed", "Could not write to the data file.")
            return
        log.info("Record saved for %s", name)
        messagebox.showinfo("Saved", "Record saved for " + name + ".")

    def show_history(self):
        try:
            records = history.load_records()
        except (OSError, KeyError) as err:
            log.error("Could not read history: %s", err)
            messagebox.showerror("Error", "Could not read the data file.")
            return

        top = tk.Toplevel(self.window)
        top.title("History & Class Report")
        top.geometry("900x420")
        top.config(bg=config.APP_BG)

        columns = ("name",) + tuple(config.SUBJECTS) + ("percentage", "grade", "result")
        table = ttk.Treeview(top, columns=columns, show="headings", height=12)
        for col in columns:
            table.heading(col, text=col.capitalize())
            table.column(col, width=90, anchor="center")
        for r in records:
            table.insert("", tk.END, values=[r[c] for c in columns])
        table.pack(fill="both", expand=True, padx=10, pady=10)

        s = history.summarize(records)
        summary = (f"Students: {s['count']}   Passed: {s['passed']}   "
                   f"Pass rate: {s['pass_rate']}%   Average: {s['average']}%   "
                   f"Topper: {s['topper'] or '-'}")
        tk.Label(top, text=summary, font=("Arial", 12, "bold"),
                 bg=config.RESULT_BG, fg=config.RESULT_FG, padx=10, pady=6
                 ).pack(pady=5)

        def clear_all():
            if messagebox.askyesno("Confirm", "Delete all saved records?", parent=top):
                history.clear_history()
                log.info("History cleared")
                top.destroy()

        self._button("Clear History", clear_all, config.SECONDARY_BUTTON,
                     "#475569", 12, 14, top).pack(pady=5)


def run():
    window = tk.Tk()
    AnalyzerApp(window)
    window.mainloop()
