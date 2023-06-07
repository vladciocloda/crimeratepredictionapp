import csv
import tempfile
from tkinter import messagebox
import win32api
import win32print
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as filedialog


class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Title
        self.wm_title("CrimeRatePredictionApp")

        # Disable resize the window
        self.resizable(False, False)

        # Icon
        self.iconbitmap("logo.ico")

        # Center window
        self.update_idletasks()
        width = 1000
        height = 500
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

        # Create objects
        self.label_crime_rate_app = tk.Label(self, text="CRIME RATE PREDICTION APP", font=("Helvetica", 36, "bold"),
                                             bg="#3498db", fg="white")
        self.label_username = tk.Label(self, text="Username")
        self.entry_username = tk.Entry(self)
        self.label_password = tk.Label(self, text="Password")
        self.entry_password = tk.Entry(self, show="*")
        self.button_login = tk.Button(self, text="Log In", command=self.login)

        # Title label
        self.label_title = tk.Label(self, text="Login Page")
        self.label_title.place(x=500, y=100, anchor="center")

        # Set colors
        self.button_login.configure(bg="#3498db")

        # Set fonts
        self.label_username.configure(font=("Arial", 10))
        self.label_password.configure(font=("Arial", 10))
        self.button_login.configure(font=("Arial", 10))
        self.label_title.configure(font=("Verdana", 20))

        # Place objects
        self.label_username.place(x=500, y=180, anchor="center")
        self.entry_username.place(x=500, y=200, anchor="center")
        self.label_password.place(x=500, y=230, anchor="center")
        self.entry_password.place(x=500, y=250, anchor="center")
        self.button_login.place(x=500, y=280, anchor="center")
        self.label_crime_rate_app.pack(side="top", fill="x")

        # Create PhotoImage for Romanian flag
        self.image_ro = tk.PhotoImage(file="image.png")

        # Create a label to display Romanian flag
        self.image_ro_label = tk.Label(image=self.image_ro)
        self.image_ro_label.place(x=850, y=340)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "test" and password == "12345":
            tk.messagebox.showinfo("Login", "Successful login")
            self.destroy()
            MainWindow()
        else:
            tk.messagebox.showerror("Login", "Invalid username or password")


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        # Title
        self.wm_title("CrimeRatePredictionApp")

        # Disable resize the window
        self.resizable(False, False)

        # Icon
        self.iconbitmap("logo.ico")

        # Create style with blue background
        style = ttk.Style()
        style.configure("Blue.TFrame", background="#3498db")

        # Center window
        self.update_idletasks()
        width = 1000
        height = 500
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

        # Main frame
        self.frame_main = ttk.Frame(self, padding=20)
        self.frame_main.pack(side="top", fill="both", expand=True)

        # Title label
        self.label_title = tk.Label(self.frame_main, text="CRIME RATE PREDICTION APP", font=("Helvetica", 36, "bold"),
                                    bg="#3498db", fg="white")
        self.label_title.pack(side="top", anchor="center")

        # Left frame
        self.frame_left = ttk.Frame(self.frame_main, style="Blue.TFrame", width=100)
        self.frame_left.pack(side="left", fill="y")

        # Menu and labels
        self.label_main_text = tk.Label(self.frame_left, text="Menu Bar", font=("Helvetica", 12, "bold", "underline"),
                                        bg="#3498db", fg="white", padx=15, pady=15)
        self.label_main_text.pack()
        self.button_home = ttk.Button(self.frame_left, text="Home", command=self.open_home, width=10)
        self.button_logout = ttk.Button(self.frame_left, text="Logout", command=self.logout, width=10)
        self.button_home.pack(side="top", anchor="w", pady=(75, 10), padx=(20, 0))
        self.button_logout.pack(side="top", anchor="w", pady=(0, 10), padx=(20, 0))

        # Display frame
        self.frame_display = ttk.Frame(self.frame_main, padding=20)
        self.frame_display.pack(side="right", fill="both", expand=True)
        self.frame_buttons = ttk.Frame(self.frame_main)
        self.frame_buttons.place(x=370, y=200)

        # Create welcome text
        self.welcome_text = ttk.Label(self.frame_main, text="Crime Statistics Page", font=("Helvetica", 16))
        self.welcome_text.place(x=400, y=75)

        # Create two main buttons
        self.button_see_crime_rate = ttk.Button(self.frame_buttons, text="See Crime Rate",
                                                command=self.openselectgraphtype, width=20)
        self.button_see_crime_rate.pack(side="left", padx=10)
        self.button_predict_crime_rate = ttk.Button(self.frame_buttons, text="Predict Crime Rate",
                                                    command=self.openpredictcrimerate, width=20)
        self.button_predict_crime_rate.pack(side="left")

        # Create PhotoImage for Romanian flag
        self.image_ro = tk.PhotoImage(file="image.png")

        # Create a label to display Romanian flag
        self.image_ro_label = tk.Label(image=self.image_ro)
        self.image_ro_label.place(x=850, y=340)

    def openselectgraphtype(self):
        self.destroy()
        SelectGraphType()

    def openpredictcrimerate(self):
        self.destroy()
        SelectPredictionType()

    def logout(self):
        tk.messagebox.showinfo("Logout", "You logged out")
        self.destroy()
        LoginWindow()

    def open_home(self):
        pass


class SelectGraphType(tk.Tk):
    def __init__(self):
        super().__init__()

        # Title for window
        self.wm_title("CrimeRatePredictionApp")

        # Disable resize the window
        self.resizable(False, False)

        # Icon
        self.iconbitmap("logo.ico")

        # Create style with blue background color
        style = ttk.Style()
        style.configure("Blue.TFrame", background="#3498db")

        # Center window
        self.update_idletasks()
        width = 1000
        height = 500
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

        # Main frame
        self.frame_main = ttk.Frame(self, padding=20)
        self.frame_main.pack(side="top", fill="both", expand=True)

        # Label for title
        self.label_title = tk.Label(self.frame_main, text="CRIME RATE PREDICTION APP",
                                    font=("Helvetica", 36, "bold"),
                                    bg="#3498db", fg="white")
        self.label_title.pack(side="top", anchor="center")

        # Left frame for menu
        self.frame_left = ttk.Frame(self.frame_main, style="Blue.TFrame", width=100)
        self.frame_left.pack(side="left", fill="y")

        # Menu buttons and labels
        self.label_main_text = tk.Label(self.frame_left, text="Menu Bar",
                                        font=("Helvetica", 12, "bold", "underline"), bg="#3498db", fg="white",
                                        padx=15, pady=15)
        self.label_main_text.pack()
        self.button_home = ttk.Button(self.frame_left, text="Home", command=self.open_home, width=10)
        self.button_logout = ttk.Button(self.frame_left, text="Logout", command=self.logout, width=10)
        self.button_home.pack(side="top", anchor="w", pady=(75, 10), padx=(20, 0))
        self.button_logout.pack(side="top", anchor="w", pady=(0, 10), padx=(20, 0))

        # Center frame for radio buttons and continue button
        self.frame_center = ttk.Frame(self.frame_main)
        self.frame_center.pack(side="left", fill="both", expand=True)

        # Label for radio buttons
        self.label_graph_type = tk.Label(self.frame_center, text="Select the graph type",
                                         font=("Helvetica", 16), pady=20)
        self.label_graph_type.pack()

        # Radio buttons for graph type
        self.graph_type = tk.StringVar(value="line")
        self.radiobutton_line = ttk.Radiobutton(self.frame_center, text="Line Graph", value="line",
                                                variable=self.graph_type)
        self.radiobutton_bar = ttk.Radiobutton(self.frame_center, text="Bar Graph", value="bar",
                                               variable=self.graph_type)
        self.radiobutton_line.pack(pady=10)
        self.radiobutton_bar.pack(pady=10)

        # Radio buttons for prediction database

        # Label for radio buttons
        self.label_graph_database = tk.Label(self.frame_center, text="Select database",
                                         font=("Helvetica", 16), pady=20)
        self.label_graph_database.pack()

        self.graph_database = tk.StringVar(value="INS")
        self.radiobutton_ins = ttk.Radiobutton(self.frame_center, text="INS data", value="INS",
                                                variable=self.graph_database)
        self.radiobutton_manual = ttk.Radiobutton(self.frame_center, text="Manual Data", value="Manual Predictions",
                                               variable=self.graph_database)
        self.radiobutton_ins.pack(pady=10)
        self.radiobutton_manual.pack(pady=10)

        # Get county
        # Load the CSV data
        data = []
        with open('crime_rates_manual.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)

        # Create a list of counties
        counties = sorted(set(row["County"] for row in data))

        # Create a dropdown menu for the counties
        self.selected_county = tk.StringVar(self.frame_center)
        self.selected_county.set(counties[0])
        self.dropdown_county = tk.OptionMenu(self.frame_center, self.selected_county, *counties)
        self.dropdown_county.pack()

        # Continue button
        self.button_continue = ttk.Button(self.frame_center, text="Continue", command=self.open_seecrimeratepage)
        self.button_continue.pack(pady=20)

    def open_home(self):
        self.destroy()
        MainWindow()

    def logout(self):
        tk.messagebox.showinfo("Logout", "You logged out")
        self.destroy()
        LoginWindow()

    def open_seecrimeratepage(self):
        self.destroy()
        SeeCrimeRatePage(self.graph_type.get(),self.graph_database.get(),self.selected_county.get())


def print_graph(fig):
    try:
        # Create temporary file for the figure
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp_file:
            fig.savefig(tmp_file.name, dpi=300, format='png')

        # Get the default printer
        printer_name = win32print.GetDefaultPrinter()

        # Start a new print job
        handle = win32print.OpenPrinter(printer_name)

        # Send the file to the printer
        win32api.ShellExecute(0, "print", tmp_file.name, None, ".", 0)

        # End the print job
        win32print.EndDocPrinter(handle)
        win32print.ClosePrinter(handle)

        print("Printing completed!")
    except Exception as e:
        print(f"Error occurred while printing: {e}")

def export_to_excel(df):
    # Prompt the user to choose a filename for the exported Excel file
    filename = filedialog.asksaveasfilename(defaultextension=".xlsx")

    # If a filename was chosen, export the data to an Excel file
    if filename:
        # Create a new DataFrame with only the columns we want to export
        export_df = df[['Year', 'Crime Rate']]

        # Write the DataFrame to an Excel file using Pandas
        export_df.to_excel(filename, index=False)

        # Display a message to the user that the export was successful
        messagebox.showinfo("Export successful", f"The data was exported to {filename} successfully.")

def save_graph(fig):
    # Saves the given matplotlib figure to a file.
    filetypes = [("PNG", "*.png"), ("PDF", "*.pdf")]
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=filetypes)
    if filename:
        fig.savefig(filename)
        messagebox.showinfo("Downloaded successfully", "Graph saved successfully!")
    else:
        messagebox.showerror("Error", "Something went wrong...")


class SeeCrimeRatePage(tk.Tk):
    def __init__(self, graph_type, graph_database, selected_county):
        super().__init__()
        self.graph_type = graph_type
        self.graph_database = graph_database
        self.selected_county = selected_county

        # Title for window
        self.wm_title("CrimeRatePredictionApp")

        # Disable resize the window
        self.resizable(False, False)

        # Icon
        self.iconbitmap("logo.ico")

        # Create style with blue background color
        style = ttk.Style()
        style.configure("Blue.TFrame", background="#3498db")

        # Center window
        self.update_idletasks()
        width = 1000
        height = 500
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

        # Main frame
        self.frame_main = ttk.Frame(self, padding=20)
        self.frame_main.pack(side="top", fill="both", expand=True)

        # Label for title
        self.label_title = tk.Label(self.frame_main, text="CRIME RATE PREDICTION APP",
                                    font=("Helvetica", 36, "bold"),
                                    bg="#3498db", fg="white")
        self.label_title.pack(side="top", anchor="center")

        # Left frame for menu
        self.frame_left = ttk.Frame(self.frame_main, style="Blue.TFrame", width=100)
        self.frame_left.pack(side="left", fill="y")

        # Menu buttons and labels
        self.label_main_text = tk.Label(self.frame_left, text="Menu Bar",
                                        font=("Helvetica", 12, "bold", "underline"), bg="#3498db", fg="white",
                                        padx=15, pady=15)
        self.label_main_text.pack()
        self.button_home = ttk.Button(self.frame_left, text="Home", command=self.open_home, width=10)
        self.button_logout = ttk.Button(self.frame_left, text="Logout", command=self.logout, width=10)
        self.button_home.pack(side="top", anchor="w", pady=(75, 10), padx=(20, 0))
        self.button_logout.pack(side="top", anchor="w", pady=(0, 10), padx=(20, 0))

        # Frames
        self.frame_display = ttk.Frame(self.frame_main, padding=20)
        self.frame_display.pack(side="right", fill="both", expand=True)

        # # Labels
        # self.welcome_text = ttk.Label(self.frame_display, text="Current crime rate in Romania (Macrotrends stats)",
        #                               font=("Helvetica", 16, "underline "))
        # self.welcome_text.pack(side="top", anchor="center")

###########################################################################################################################
#       If user goes for INS database
###########################################################################################################################
        if self.graph_database == 'INS':
            # Labels
            self.welcome_text = ttk.Label(self.frame_display, text="Current crime rate in Romania (Macrotrends stats)",
                                          font=("Helvetica", 16, "underline "))
            self.welcome_text.pack(side="top", anchor="center")

            # Read from CSV
            df = pd.read_csv('crime_rates.csv')

            # Graph frame
            self.frame_graph = ttk.Frame(self.frame_display)
            self.frame_graph.pack(side="right", fill="both", expand=True)

            # Create graph/plot

            # Size of plot
            fig = plt.figure(figsize=(5, 3))

            # Add new subplot to the plot; 111 = subplot can occupy whole plot
            ax = fig.add_subplot(111)

            if self.graph_type == 'bar':
                # Create plot based on isAppended from CSV file
                for i, row in df.iterrows():
                    if row['isAppended'] == 'x':
                        ax.bar(row['Year'], row['Crime Rate'], width=0.5, color='red')
                        # Display value of crime rate on top of the bar (2f = 2 decimals)
                        ax.text(row['Year'], row['Crime Rate'], f"{row['Crime Rate']:.2f}", ha='center', va='bottom',
                                fontsize=8)
                    else:
                        ax.bar(row['Year'], row['Crime Rate'], width=0.5, color='blue')
                        # Display value of crime rate on top of the bar (2f = 2 decimals)
                        ax.text(row['Year'], row['Crime Rate'], f"{row['Crime Rate']:.2f}", ha='center', va='bottom',
                                fontsize=8)

                # Sets location of Year (oX)
                ax.set_xticks(df['Year'])

                # Set values for oX
                ax.set_xticklabels(df['Year'])

                # Apply a logarithmic transformation to the y-axis
                # ax.set_yscale('log')

                # Title of the plot
                plt.title('Crime Rate')

                # Set label of oY to Values
                plt.ylabel('Values')

                # Sets values of oY from 0 to 10
                plt.ylim([0, 10])

                # Rotates oX years
                plt.xticks(rotation=90)

                # Spacing of subplot such that all values will fit correctly
                plt.tight_layout()

                # Change background of graph/plot
                fig.patch.set_facecolor('#dcdcdc')

                # Create Canvas widget
                canvas = FigureCanvasTkAgg(fig, master=self.frame_graph)

                # Draw the plot into Canvas
                canvas.draw()

                # Places Canvas in Tkinter
                canvas.get_tk_widget().pack(side='top', fill='both', expand=True)

                # Button for saving the graph
                button_save = tk.Button(self.frame_display, text="Save", command=lambda: save_graph(fig))
                button_save.place(x=780, y=350)

                # Button for printing the graph
                button_print = tk.Button(self.frame_display, text="Print", command=lambda: print_graph(fig))
                button_print.place(x=740, y=350)

                # Button for exporting the graph
                button_export = tk.Button(self.frame_display, text="Export", command=lambda: export_to_excel(df))
                button_export.place(x=690, y=350)


            # for line graph
            else:
                # Create plot based on isAppended from CSV file
                for i, row in df.iterrows():
                    if row['isAppended'] == 'x':
                        ax.plot(row['Year'], row['Crime Rate'], color='red', marker='o')
                        # Display value of crime rate on top of the bar (2f = 2 decimals)
                        ax.text(row['Year'], row['Crime Rate'], f"{row['Crime Rate']:.2f}", ha='center', va='bottom',
                                fontsize=8)
                    else:
                        ax.plot(row['Year'], row['Crime Rate'], color='blue', marker='o')
                        # Display value of crime rate on top of the bar (2f = 2 decimals)
                        ax.text(row['Year'], row['Crime Rate'], f"{row['Crime Rate']:.2f}", ha='center', va='bottom',
                                fontsize=8)

                # Plot a line connecting the dots
                ax.plot(df['Year'], df['Crime Rate'], color='black')

                # Apply a logarithmic transformation to the y-axis
                # ax.set_yscale('log')

                # Sets location of Year (oX)
                ax.set_xticks(df['Year'])

                # Set values for oX
                ax.set_xticklabels(df['Year'])

                # Title of the plot
                plt.title('Crime Rate')

                # Set label of oY to Values
                plt.ylabel('Values')

                # Sets values of oY from 0 to 10
                plt.ylim([0, 10])

                # Rotates oX years
                plt.xticks(rotation=90)

                # Spacing of subplot such that all values will fit correctly
                plt.tight_layout()

                # Change background of graph/plot
                fig.patch.set_facecolor('#dcdcdc')

                # Create Canvas widget
                canvas = FigureCanvasTkAgg(fig, master=self.frame_graph)

                # Draw the plot into Canvas
                canvas.draw()

                # Places Canvas in Tkinter
                canvas.get_tk_widget().pack(side='top', fill='both', expand=True)

                # Button for saving the graph
                button_save = tk.Button(self.frame_display, text="Save", command=lambda: save_graph(fig))
                button_save.place(x=780, y=350)

                # Button for printing the graph
                button_print = tk.Button(self.frame_display, text="Print", command=lambda: print_graph(fig))
                button_print.place(x=740, y=350)

                # Button for exporting the graph
                button_export = tk.Button(self.frame_display, text="Export", command=lambda: export_to_excel(df))
                button_export.place(x=690, y=350)

###########################################################################################################################
#       If user goes for manual database
###########################################################################################################################

        else:
            # Read from CSV and filter for County selected
            df = pd.read_csv('crime_rates_manual.csv')
            df_county = df[df['County'] == selected_county]

            # Graph frame
            self.frame_graph = ttk.Frame(self.frame_display)
            self.frame_graph.pack(side="right", fill="both", expand=True)

            # Create graph/plot

            # Size of plot
            fig = plt.figure(figsize=(5, 3))

            # Add new subplot to the plot; 111 = subplot can occupy whole plot
            ax = fig.add_subplot(111)

            if self.graph_type == 'bar':
                # Create plot based on isAppended from CSV file
                for i, row in df_county.iterrows():
                    if row['isAppended'] == 'x':
                        ax.bar(row['Year'], row['Crime Rate'], width=0.5, color='red')
                        # Display value of crime rate on top of the bar (2f = 2 decimals)
                        ax.text(row['Year'], row['Crime Rate'], f"{row['Crime Rate']:.2f}", ha='center', va='bottom',
                                fontsize=8)
                    else:
                        ax.bar(row['Year'], row['Crime Rate'], width=0.5, color='blue')
                        # Display value of crime rate on top of the bar (2f = 2 decimals)
                        ax.text(row['Year'], row['Crime Rate'], f"{row['Crime Rate']:.2f}", ha='center', va='bottom',
                                fontsize=8)

                # Sets location of Year (oX)
                ax.set_xticks(df_county['Year'])

                # Set values for oX
                ax.set_xticklabels(df_county['Year'])

                # Title of the plot
                plt.title('Crime Rate in county ' + selected_county)

                # Set label of oY to Values
                plt.ylabel('Values')

                # Apply a logarithmic transformation to the y-axis
                # ax.set_yscale('log')

                # Set the minimum value of the y-axis to 0.1
                # ax.set_ylim(bottom=0.1)

                # Rotates oX years
                plt.xticks(rotation=90)

                # Spacing of subplot such that all values will fit correctly
                plt.tight_layout()

                # Change background of graph/plot
                fig.patch.set_facecolor('#dcdcdc')

                # Create Canvas widget
                canvas = FigureCanvasTkAgg(fig, master=self.frame_graph)

                # Draw the plot into Canvas
                canvas.draw()

                # Places Canvas in Tkinter
                canvas.get_tk_widget().pack(side='top', fill='both', expand=True)

                # Button for saving the graph
                button_save = tk.Button(self.frame_display, text="Save", command=lambda: save_graph(fig))
                button_save.place(x=780, y=350)

                # Button for printing the graph
                button_print = tk.Button(self.frame_display, text="Print", command=lambda: print_graph(fig))
                button_print.place(x=740, y=350)

                # Button for exporting the graph
                button_export = tk.Button(self.frame_display, text="Export", command=lambda: export_to_excel(df_county))
                button_export.place(x=690, y=350)

            else:
                # Create plot based on isAppended from CSV file
                for i, row in df_county.iterrows():
                    if row['isAppended'] == 'x':
                        ax.bar(row['Year'], row['Crime Rate'], width=0.5, color='red')
                        # Display value of crime rate on top of the bar (2f = 2 decimals)
                        ax.text(row['Year'], row['Crime Rate'], f"{row['Crime Rate']:.2f}", ha='center', va='bottom',
                                fontsize=8)
                    else:
                        ax.plot(row['Year'], row['Crime Rate'], color='blue', marker='o')
                        # Display value of crime rate on top of the bar (2f = 2 decimals)
                        ax.text(row['Year'], row['Crime Rate'], f"{row['Crime Rate']:.2f}", ha='center', va='bottom',
                                fontsize=8)

                # Plot a line connecting the dots
                ax.plot(df_county['Year'], df_county['Crime Rate'], color='black')

                # Sets location of Year (oX)
                ax.set_xticks(df_county['Year'])

                # Set values for oX
                ax.set_xticklabels(df_county['Year'])

                # Title of the plot
                plt.title('Crime Rate in county ' + selected_county)

                # Set label of oY to Values
                plt.ylabel('Values')

                # Apply a logarithmic transformation to the y-axis
                # ax.set_yscale('log')

                # Set the minimum value of the y-axis to 0.1
                # ax.set_ylim(bottom=0.1)

                # Rotates oX years
                plt.xticks(rotation=90)

                # Spacing of subplot such that all values will fit correctly
                plt.tight_layout()

                # Change background of graph/plot
                fig.patch.set_facecolor('#dcdcdc')

                # Create Canvas widget
                canvas = FigureCanvasTkAgg(fig, master=self.frame_graph)

                # Draw the plot into Canvas
                canvas.draw()

                # Places Canvas in Tkinter
                canvas.get_tk_widget().pack(side='top', fill='both', expand=True)

                # Button for saving the graph
                button_save = tk.Button(self.frame_display, text="Save", command=lambda: save_graph(fig))
                button_save.place(x=780, y=350)

                # Button for printing the graph
                button_print = tk.Button(self.frame_display, text="Print", command=lambda: print_graph(fig))
                button_print.place(x=740, y=350)

                # Button for exporting the graph
                button_export = tk.Button(self.frame_display, text="Export", command=lambda: export_to_excel(df_county))
                button_export.place(x=690, y=350)

    def open_home(self):
        self.destroy()
        MainWindow()

    def logout(self):
        tk.messagebox.showinfo("Logout", "You logged out")
        self.destroy()
        LoginWindow()


class SelectPredictionType(tk.Tk):
    def __init__(self):
        super().__init__()

        # Title
        self.wm_title("CrimeRatePredictionApp")

        # Disable resize the window
        self.resizable(False, False)

        # Icon
        self.iconbitmap("logo.ico")

        # Create style with blue background
        style = ttk.Style()
        style.configure("Blue.TFrame", background="#3498db")

        # Center window
        self.update_idletasks()
        width = 1000
        height = 500
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

        # Main frame
        self.frame_main = ttk.Frame(self, padding=20)
        self.frame_main.pack(side="top", fill="both", expand=True)

        # Title label
        self.label_title = tk.Label(self.frame_main, text="CRIME RATE PREDICTION APP",
                                    font=("Helvetica", 36, "bold"),
                                    bg="#3498db", fg="white")
        self.label_title.pack(side="top", anchor="center")

        # Left frame
        self.frame_left = ttk.Frame(self.frame_main, style="Blue.TFrame", width=100)
        self.frame_left.pack(side="left", fill="y")

        # Menu and labels
        self.label_main_text = tk.Label(self.frame_left, text="Menu Bar",
                                        font=("Helvetica", 12, "bold", "underline"), bg="#3498db", fg="white",
                                        padx=15, pady=15)
        self.label_main_text.pack()
        self.button_home = ttk.Button(self.frame_left, text="Home", command=self.open_home, width=10)
        self.button_logout = ttk.Button(self.frame_left, text="Logout", command=self.logout, width=10)
        self.button_home.pack(side="top", anchor="w", pady=(75, 10), padx=(20, 0))
        self.button_logout.pack(side="top", anchor="w", pady=(0, 10), padx=(20, 0))

        # Display frame
        self.frame_display = ttk.Frame(self.frame_main, padding=20)
        self.frame_display.pack(side="right", fill="both", expand=True)

        # Center frame for radio buttons and continue button
        self.frame_center = ttk.Frame(self.frame_main)
        self.frame_center.pack(side="left", fill="both", expand=True)

        # Label for radio buttons
        self.label_pred_type = tk.Label(self.frame_center, text="Select the prediction type",
                                        font=("Helvetica", 16), pady=20)
        self.label_pred_type.pack()

        # Radio buttons
        self.pred_type = tk.StringVar(value="automatic")
        self.radiobutton_auto = ttk.Radiobutton(self.frame_center, text="Automatic", value="automatic",
                                                variable=self.pred_type)
        self.radiobutton_man = ttk.Radiobutton(self.frame_center, text="Manual", value="manual",
                                               variable=self.pred_type)
        self.radiobutton_auto.place(x=250, y=120)
        self.radiobutton_man.place(x=250, y=150)

        # Continue button
        self.button_continue = ttk.Button(self.frame_center, text="Continue", command=self.open_predictcrimeratepage)
        self.button_continue.place(x=250, y=200)

    def open_home(self):
        self.destroy()
        MainWindow()

    def logout(self):
        tk.messagebox.showinfo("Logout", "You logged out")
        self.destroy()
        LoginWindow()

    def open_predictcrimeratepage(self):
        self.destroy()
        PredictCrimeRatePage(self.pred_type.get())


class PredictCrimeRatePage(tk.Tk):
    def __init__(self, pred_type):
        super().__init__()

        self.pred_type = pred_type

        # Title
        self.wm_title("CrimeRatePredictionApp")

        # Disable resize the window
        self.resizable(False, False)

        # Icon
        self.iconbitmap("logo.ico")

        # Create style with blue background
        style = ttk.Style()
        style.configure("Blue.TFrame", background="#3498db")

        # Center window
        self.update_idletasks()
        width = 1000
        height = 500
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

        # Main frame
        self.frame_main = ttk.Frame(self, padding=20)
        self.frame_main.pack(side="top", fill="both", expand=True)

        # Title label
        self.label_title = tk.Label(self.frame_main, text="CRIME RATE PREDICTION APP",
                                    font=("Helvetica", 36, "bold"),
                                    bg="#3498db", fg="white")
        self.label_title.pack(side="top", anchor="center")

        # Left frame
        self.frame_left = ttk.Frame(self.frame_main, style="Blue.TFrame", width=100)
        self.frame_left.pack(side="left", fill="y")

        # Menu and labels
        self.label_main_text = tk.Label(self.frame_left, text="Menu Bar",
                                        font=("Helvetica", 12, "bold", "underline"), bg="#3498db", fg="white",
                                        padx=15, pady=15)
        self.label_main_text.pack()
        self.button_home = ttk.Button(self.frame_left, text="Home", command=self.open_home, width=10)
        self.button_logout = ttk.Button(self.frame_left, text="Logout", command=self.logout, width=10)
        self.button_home.pack(side="top", anchor="w", pady=(75, 10), padx=(20, 0))
        self.button_logout.pack(side="top", anchor="w", pady=(0, 10), padx=(20, 0))

        # Display frame
        self.frame_display = ttk.Frame(self.frame_main, padding=20)
        self.frame_display.pack(side="right", fill="both", expand=True)

        # Display label
        self.welcome_text = ttk.Label(self.frame_display, text="Predict new Crime Rate",
                                      font=("Helvetica", 16, "underline "))
        self.welcome_text2 = ttk.Label(self.frame_display, text="Enter parameters:", font=("Helvetica", 10))
        self.welcome_text.pack(side="top", anchor="center")
        self.welcome_text2.pack(anchor="nw")

        # Text to specify that country is Romania
        self.econ_text = ttk.Label(text="Country: Romania", font=("Arial", 10, "bold"))
        self.econ_text.place(x=200, y=150)

        # Get county
        # Load the CSV data
        data = []
        with open('crime_rates_manual.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)

        # Create a list of counties
        counties = sorted(set(row["County"] for row in data))

        if self.pred_type == 'manual':
            label_county = tk.Label(self.frame_display, text="Select county:")
            label_county.place(x=280, y=55)
            # Create a dropdown menu for the counties
            self.selected_county = tk.StringVar(self.frame_display)
            self.selected_county.set(counties[0])
            self.dropdown_county = tk.OptionMenu(self.frame_display, self.selected_county, *counties)
            self.dropdown_county.pack()
        else:
            self.selected_county = tk.StringVar(self.frame_display)
            self.selected_county.set(counties[0])
        #######################################################################################################
        # --> Begin Titles

        self.econ_text = ttk.Label(text="Economic parameters", font=("Arial", 10, "underline"))
        self.econ_text.place(x=200, y=180)
        self.education_text = ttk.Label(text="Socio-cultural parameters", font=("Arial", 10, "underline"))
        self.education_text.place(x=500, y=180)
        self.education_text = ttk.Label(text="Demographic parameters", font=("Arial", 10, "underline"))
        self.education_text.place(x=775, y=180)

        # <-- End Titles
        #######################################################################################################

        #######################################################################################################
        # --> Begin input fields and text for economic parameters + placement

        self.text_econ_pib = tk.Label(text="PIB (increase rate):")
        self.text_econ_ght = tk.Label(text="Gross Household Income:")
        self.text_econ_poverty = tk.Label(text="Poverty rate:")
        self.text_econ_unemp = tk.Label(text="Unemployment rate:")
        self.econ_pib = tk.Entry()
        self.econ_ght = tk.Entry()
        self.econ_poverty = tk.Entry()
        self.econ_unemp = tk.Entry()
        self.econ_pib.place(x=300, y=210)
        self.econ_ght.place(x=300, y=240)
        self.econ_poverty.place(x=300, y=270)
        self.econ_unemp.place(x=300, y=300)
        self.text_econ_pib.place(x=150, y=210)
        self.text_econ_ght.place(x=150, y=240)
        self.text_econ_poverty.place(x=150, y=270)
        self.text_econ_unemp.place(x=150, y=300)

        # Create input fields and text for socio-cultural parameters + placement
        self.text_socio_divorce = tk.Label(text="Divorce rate:")
        self.socio_divorce = tk.Entry()
        self.socio_divorce.place(x=575, y=210)
        self.text_socio_divorce.place(x=450, y=210)
        self.text_socio_school = tk.Label(text="School dropout rate:")
        self.socio_school = tk.Entry()
        self.socio_school.place(x=575, y=240)
        self.text_socio_school.place(x=450, y=240)

        # Create input fields and text for demographic parameters + placement
        self.text_demographic_urban = tk.Label(text="Urbanization rate:")
        self.demographic_urban = tk.Entry()
        self.demographic_urban.place(x=850, y=210)
        self.text_demographic_urban.place(x=725, y=210)

        # <-- End input fields
        #######################################################################################################

        # Predict button
        self.button_predict = tk.Button(text="Predict", command=self.predict_crime_rate)
        self.button_predict.configure(bg="#3498db")
        self.button_predict.configure(font=("Arial", 10))
        self.button_predict.place(x=550, y=450, anchor="center")

    def predict_crime_rate(self):
        try:
            # Get the input values from the entries + compute crime rate

            # Economic parameters
            input_pib = float(self.econ_pib.get())
            input_ght = float(self.econ_ght.get())
            input_poverty = float(self.econ_poverty.get())
            input_unemp = float(self.econ_unemp.get())

            # Socio-cultural parameters
            input_divorce = float(self.socio_divorce.get())
            input_school = float(self.socio_school.get())

            # Demographic parameters
            input_urban = float(self.demographic_urban.get())

            # Variable to store new crime rate
            new_crime_rate = (0.78 / 100 * input_pib) + (0.8 / 100 * input_ght) + (1.36 / 100 * input_poverty) + (
                    3.56 / 100 * input_unemp) + (1.64 / 100 * input_school) + (15.3 / 100 * input_divorce) + (
                                     0.57 / 100 * input_urban)

            self.destroy()
            CrimeAnalysis(PredictCrimeRatePage, input_pib, input_ght, input_unemp, input_urban, input_school,
                          input_divorce, input_poverty, new_crime_rate, self.pred_type, self.selected_county.get())

        except:
            print("Fields cannot be empty, negative or characters!")

    def open_home(self):
        self.destroy()
        MainWindow()

    def logout(self):
        tk.messagebox.showinfo("Logout", "You logged out")
        self.destroy()
        LoginWindow()


class CrimeAnalysis(tk.Tk):
    def __init__(self, parent, pib, unemp, divorce, school, poverty, ght, urban, crime_rate, pred_type, selected_county):
        super().__init__()

        self.pred_type = pred_type
        self.selected_county = selected_county

        self.parent = parent
        self.pib = pib
        self.unemp = unemp
        self.divorce = divorce
        self.school = school
        self.poverty = poverty
        self.ght = ght
        self.urban = urban
        self.crime_rate = crime_rate

        # Title
        self.wm_title("CrimeRatePredictionApp")

        # Disable resize the window
        self.resizable(False, False)

        # Icon
        self.iconbitmap("logo.ico")

        # Create style with blue background
        style = ttk.Style()
        style.configure("Blue.TFrame", background="#3498db")

        # Center window
        self.update_idletasks()
        width = 1000
        height = 500
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

        # Main frame
        self.frame_main = ttk.Frame(self, padding=20)
        self.frame_main.pack(side="top", fill="both", expand=True)

        # Title label
        self.label_title = tk.Label(self.frame_main, text="CRIME RATE PREDICTION APP",
                                    font=("Helvetica", 36, "bold"),
                                    bg="#3498db", fg="white")
        self.label_title.pack(side="top", anchor="center")

        # Left frame
        self.frame_left = ttk.Frame(self.frame_main, style="Blue.TFrame", width=100)
        self.frame_left.pack(side="left", fill="y")

        # Menu and labels
        self.label_main_text = tk.Label(self.frame_left, text="Menu Bar",
                                        font=("Helvetica", 12, "bold", "underline"), bg="#3498db", fg="white",
                                        padx=15, pady=15)
        self.label_main_text.pack()
        self.button_home = ttk.Button(self.frame_left, text="Home", command=self.open_home, width=10)
        self.button_logout = ttk.Button(self.frame_left, text="Logout", command=self.logout, width=10)
        self.button_home.pack(side="top", anchor="w", pady=(75, 10), padx=(20, 0))
        self.button_logout.pack(side="top", anchor="w", pady=(0, 10), padx=(20, 0))

        # Display frame
        self.frame_display = ttk.Frame(self.frame_main, padding=20)
        self.frame_display.pack(side="right", fill="both", expand=True)

        # Display label
        self.welcome_text = ttk.Label(self.frame_display, text="Predict new Crime Rate",
                                      font=("Helvetica", 16, "underline "))
        self.welcome_text.pack(side="top", anchor="center")

        self.econ_text = ttk.Label(text="Country: Romania", font=("Arial", 10, "bold"))
        self.econ_text.place(x=150, y=150)
        self.econ_text = ttk.Label(text="Parameters you have enetered", font=("Arial", 10, "underline"))
        self.econ_text.place(x=150, y=180)

        self.text_econ_pib = tk.Label(text="PIB (increase rate):      " + str(self.pib))
        self.text_econ_pib.place(x=150, y=210)
        self.value_econ_pib = tk.Label()
        self.value_econ_pib.place(x=250, y=210)
        self.text_econ_ght = tk.Label(text="Gross Household Income:     " + str(self.ght))
        self.text_econ_ght.place(x=150, y=240)
        self.text_econ_poverty = tk.Label(text="Poverty rate:       " + str(self.poverty))
        self.text_econ_poverty.place(x=150, y=270)
        self.text_econ_unemp = tk.Label(text="Unemployment rate:        " + str(self.unemp))
        self.text_econ_unemp.place(x=150, y=300)
        self.text_socio_divorce = tk.Label(text="Divorce rate:      " + str(self.divorce))
        self.text_socio_divorce.place(x=150, y=330)
        self.text_socio_school = tk.Label(text="School dropout rate:        " + str(self.school))
        self.text_socio_school.place(x=150, y=360)
        self.text_demographic_urban = tk.Label(text="Urbanization rate:     " + str(self.urban))
        self.text_demographic_urban.place(x=150, y=390)
        self.text_demographic_urban = tk.Label(text="Predicted Crime Rate:     " + str(self.crime_rate),
                                               font=("Helvetica", 10, "bold"))
        self.text_demographic_urban.place(x=150, y=450)

        # Predict button
        self.button_predict = tk.Button(text="Predict for one more year", command=self.openSelectPredictionType)
        self.button_predict.configure(bg="#3498db")
        self.button_predict.configure(font=("Arial", 10))
        self.button_predict.place(x=550, y=480, anchor="center")

        if pred_type == 'automatic':
            # Read from CSV
            df = pd.read_csv('crime_rates.csv')

            # Compute next year based on last year from CSV
            last_year = df['Year'].iloc[-1]
            new_year = last_year + 1

            # new row with user input
            new_row = {'Year': new_year, 'Crime Rate': self.crime_rate, 'isAppended': 'x'}

            # new structure with new row
            new_df = pd.DataFrame(new_row, index=[0])
            df = pd.concat([df, new_df], ignore_index=True)

            # Rewrite the csv file appending new data
            df.to_csv('crime_rates.csv', index=False)

            # Graph frame
            self.frame_graph = ttk.Frame(self.frame_display)
            self.frame_graph.pack(side="right", fill="both", expand=True)

            # Create graph/plot

            # Size of plot
            fig = plt.figure(figsize=(2, 3))

            # Add new subplot to the plot; 111 = subplot can occupy whole plot
            ax = fig.add_subplot(111)

            # Create plot based on isAppended from CSV file
            for i, row in df.iterrows():
                if row['isAppended'] == 'x':
                    ax.bar(row['Year'], row['Crime Rate'], width=0.5, color='red')
                    # Display value of crime rate on top of the bar (2f = 2 decimals)
                    ax.text(row['Year'], row['Crime Rate'], f"{row['Crime Rate']:.2f}", ha='center', va='bottom',
                            fontsize=8)
                else:
                    ax.bar(row['Year'], row['Crime Rate'], width=0.5, color='blue')
                    # Display value of crime rate on top of the bar (2f = 2 decimals)
                    ax.text(row['Year'], row['Crime Rate'], f"{row['Crime Rate']:.2f}", ha='center', va='bottom',
                            fontsize=8)

            # Sets location of Year (oX)
            ax.set_xticks(df['Year'])

            # Set values for oX
            ax.set_xticklabels(df['Year'])

            # Apply a logarithmic transformation to the y-axis
            # ax.set_yscale('log')

            # Title of the plot
            plt.title('Crime Rate')

            # Set label of oY to Values
            plt.ylabel('Values')

            # Sets values of oY from 0 to 10
            plt.ylim([0, 10])

            # Rotates oX years
            plt.xticks(rotation=90)

            # Spacing of subplot such that all values will fit correctly
            plt.tight_layout()

            # Change background of graph/plot
            fig.patch.set_facecolor('#dcdcdc')

            # Create Canvas widget
            canvas = FigureCanvasTkAgg(fig, master=self.frame_graph)

            # Draw the plot into Canvas
            canvas.draw()

            # Places Canvas in Tkinter
            canvas.get_tk_widget().pack(side='top', fill='both', expand=True)
        else:
            # Read from CSV and filter for County selected
            df = pd.read_csv('crime_rates_manual.csv')

            # Compute next year based on last year from CSV
            # Get the last year for the selected county
            last_year = df[df['County'] == self.selected_county]['Year'].max()
            new_year = last_year + 1

            # new row with user input
            new_row = {'Year': new_year, 'Crime Rate': self.crime_rate, 'County': self.selected_county, 'isAppended': 'x'}

            # new structure with new row
            new_df = pd.DataFrame(new_row, index=[0])
            df = pd.concat([df, new_df], ignore_index=True)

            # Rewrite the csv file appending new data
            df.to_csv('crime_rates_manual.csv', index=False)

            df_county = df[df['County'] == self.selected_county]

            # Graph frame
            self.frame_graph = ttk.Frame(self.frame_display)
            self.frame_graph.pack(side="right", fill="both", expand=True)

            # Create graph/plot

            # Size of plot
            fig = plt.figure(figsize=(2, 3))

            # Add new subplot to the plot; 111 = subplot can occupy whole plot
            ax = fig.add_subplot(111)

            # Create plot based on isAppended from CSV file
            for i, row in df_county.iterrows():
                if row['isAppended'] == 'x':
                    ax.bar(row['Year'], row['Crime Rate'], width=0.5, color='red')
                    # Display value of crime rate on top of the bar (2f = 2 decimals)
                    ax.text(row['Year'], row['Crime Rate'], f"{row['Crime Rate']:.2f}", ha='center', va='bottom',
                            fontsize=8)
                else:
                    ax.bar(row['Year'], row['Crime Rate'], width=0.5, color='blue')
                    # Display value of crime rate on top of the bar (2f = 2 decimals)
                    ax.text(row['Year'], row['Crime Rate'], f"{row['Crime Rate']:.2f}", ha='center', va='bottom',
                            fontsize=8)

            # Sets location of Year (oX)
            ax.set_xticks(df_county['Year'])

            # Set values for oX
            ax.set_xticklabels(df_county['Year'])

            # Title of the plot
            plt.title('Crime Rate for County ' + self.selected_county)

            # Set label of oY to Values
            plt.ylabel('Values')

            # Apply a logarithmic transformation to the y-axis
            # ax.set_yscale('log')

            # Set the minimum value of the y-axis to 1
            # ax.set_ylim(bottom=0.1)

            # Rotates oX years
            plt.xticks(rotation=90)

            # Spacing of subplot such that all values will fit correctly
            plt.tight_layout()

            # Change background of graph/plot
            fig.patch.set_facecolor('#dcdcdc')

            # Create Canvas widget
            canvas = FigureCanvasTkAgg(fig, master=self.frame_graph)

            # Draw the plot into Canvas
            canvas.draw()

            # Places Canvas in Tkinter
            canvas.get_tk_widget().pack(side='top', fill='both', expand=True)

    def open_home(self):
        self.destroy()
        MainWindow()

    def logout(self):
        tk.messagebox.showinfo("Logout", "You logged out")
        self.destroy()
        LoginWindow()

    def openSelectPredictionType(self):
        self.destroy()
        SelectPredictionType()


if __name__ == "__main__":
    window = LoginWindow()
    window.mainloop()
