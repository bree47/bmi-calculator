import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt


def calculate_bmi():
    try:
        height = float(height_entry.get()) / 100  # convert height from cm to meters
        weight = float(weight_entry.get())

        if height <= 0 or weight <= 0:
            messagebox.showerror("Error", "Please enter valid height and weight.")
            return

        bmi = weight / (height * height)
        bmi_result.set(f"Your BMI: {bmi:.2f}")

        if bmi < 18.5:
            bmi_category.set("Underweight")
        elif bmi < 25:
            bmi_category.set("Normal weight")
        elif bmi < 30:
            bmi_category.set("Overweight")
        else:
            bmi_category.set("Obesity")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for height and weight.")


def save_details():
    try:
        name = name_entry.get()
        age = int(age_entry.get())
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        bmi = float(bmi_result.get().split(":")[1].strip())
        category = bmi_category.get()

        with open("bmi_details.txt", "a") as file:
            file.write(
                f"Name: {name}, Age: {age}, Height: {height} cm, Weight: {weight} kg, BMI: {bmi:.2f}, Category: {category}\n")

        messagebox.showinfo("Saved", "BMI details saved successfully!")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for age, height, and weight.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def show_pie_chart():
    try:
        categories = {"Underweight": 0, "Normal weight": 0, "Overweight": 0, "Obesity": 0}

        with open("bmi_details.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if "Category: " in line:
                    category = line.split("Category: ")[1].strip()
                    categories[category] += 1

        labels = list(categories.keys())
        values = list(categories.values())

        plt.figure(figsize=(8, 6))
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('BMI Category Distribution')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

    except FileNotFoundError:
        messagebox.showerror("Error", "No BMI details found. Save some details first.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")



root = tk.Tk()
root.title("BMI Calculator")


name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

age_label = tk.Label(root, text="Age:")
age_label.grid(row=1, column=0, padx=10, pady=10)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=10)

height_label = tk.Label(root, text="Height (cm):")
height_label.grid(row=2, column=0, padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.grid(row=2, column=1, padx=10, pady=10)

weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=3, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=3, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

bmi_result = tk.StringVar()
bmi_label = tk.Label(root, textvariable=bmi_result, font=("Arial", 14, "bold"))
bmi_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

bmi_category = tk.StringVar()
category_label = tk.Label(root, textvariable=bmi_category)
category_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

save_button = tk.Button(root, text="Save Details", command=save_details)
save_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

show_chart_button = tk.Button(root, text="Show Pie Chart", command=show_pie_chart)
show_chart_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()
