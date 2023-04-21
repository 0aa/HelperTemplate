import tkinter as tk
from tkinter import ttk, messagebox


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("QA Helper")

        # Create main frame to hold notebook, start button, and output text
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(expand=True, fill="both")

        # Create notebook, start button, and output text
        self.create_notebook()
        self.create_start_button()
        self.create_output_text()

    def create_notebook(self):
        # Create Notebook widget (tab container)
        self.notebook = ttk.Notebook(self.main_frame)

        # Create tab frames
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)

        # Add tab frames to notebook
        self.notebook.add(self.tab1, text="New Test Case")
        self.notebook.add(self.tab2, text="New Report")
        self.notebook.add(self.tab3, text="Settings")

        # Create and place widgets on the first tab
        self.create_tab1_widgets()

        self.create_tab3_widgets()

        # Place the notebook on the main frame using grid
        self.notebook.grid(row=0, column=0, sticky="nsew")

    def create_tab1_widgets(self):
        # Create widgets for the first tab
        self.label1 = tk.Label(self.tab1, text="Title:")
        self.entry1 = tk.Entry(self.tab1)
        self.label2 = tk.Label(self.tab1, text="Steps:")
        self.text2 = tk.Text(self.tab1, wrap="word", height=5)
        self.submit_button = tk.Button(self.tab1, text="Submit", command=self.on_submit)

        # Place widgets on the first tab using grid
        self.label1.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry1.grid(row=0, column=1, sticky="we", padx=5, pady=5)
        self.label2.grid(row=1, column=0, sticky="nw", padx=5, pady=5)
        self.text2.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
        self.submit_button.grid(row=2, column=0, columnspan=2, pady=5)

        # Configure the row and column weights (resizing behavior)
        self.tab1.columnconfigure(0, weight=1)
        self.tab1.columnconfigure(1, weight=3)
        self.tab1.rowconfigure(1, weight=1)

    def create_tab2_widgets(self):
        pass

    def create_tab3_widgets(self):
        self.label3 = tk.Label(self.tab3, text="Organization:")
        self.entry3 = tk.Entry(self.tab3)
        self.submit_button3 = tk.Button(self.tab3, text="Submit", command=self.on_submit)


        self.label3.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry3.grid(row=0, column=1, sticky="we", padx=5, pady=5)
        self.submit_button3.grid(row=2, column=0, columnspan=2, pady=5)



    def create_start_button(self):
        # Create Start button and place it in the bottom right corner using grid
        self.start_button = tk.Button(self.tab1, text="Start", command=self.on_start)
        self.start_button.grid(row=5, column=5, sticky="se", padx=5, pady=5)

    def create_output_text(self):
        # Create output text widget and place it below the Start button
        self.output_text = tk.Text(self.main_frame, wrap="word", height=10)
        self.output_text.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

        # Configure the main frame row and column weights
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.rowconfigure(2, weight=2)

    def on_submit(self):
        # Get input data and insert it into the output text widget
        input_data1 = self.entry1.get()
        input_data2 = self.text2.get("1.0", "end-1c")

        # Check if the mandatory field is empty
        if not input_data1.strip():
            messagebox.showerror("Error", "Data 1 field is mandatory.")
            return
        if not input_data2.strip():
            messagebox.showerror("Error", "Data 2 field is mandatory.")
            return


        self.output_text.insert("end", f"Title: {input_data1}\n")
        self.output_text.insert("end", f"Steps: {input_data2}\n")

    def on_start(self):
        # Insert a message into the output text widget when the Start button is pressed
        self.output_text.insert("end", "Start button pressed\n")


if __name__ == "__main__":
    app = Application()
    app.mainloop()
