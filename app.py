import tkinter as tk
import csv
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyALYC2hBTuwMVw3yXoGrSV_8MTwoIqdEZ0')

from datetime import datetime
from tkinter import messagebox

save_trip = True
root = tk.Tk()
employee_name_entry = tk.Entry(root)
employee_name_entry.pack()
trip_count = 0



def add_trip():
    # Retrieve the values from the input fields
    departure_address = departure_entry.get()
    arrival_address = arrival_entry.get()
    reason = reason_entry.get()
    odometer_start = float(odometer_start_entry.get())
    odometer_end_text = odometer_end_entry.get()
    odometer_end = float(odometer_end_text) if odometer_end_text else 0
    tolls = float(tolls_entry.get() or "0")
    parking = float(parking_entry.get() or "0")

    # Calculate the total miles
    total_miles = calculate_miles(departure_address, arrival_address)

    # Update the miles display label
    miles_display.config(text=f"{total_miles:.2f}")

    # Calculate the total expenses
    expenses = (total_miles * 0.59) + tolls + parking

    # define the reason_entry variable before referencing it
   
    reason_entry.grid(row=2, column=1)

    # the rest of the code
    reason = reason_entry.get()
    trip_count = trip_count + 1


    # add trip data to dictionary
    date = datetime.now().strftime("%Y-%m-%d")
    trips[date] = {
        "departure_address": departure_address,
        "arrival_address": arrival_address,
        "odometer_start": odometer_start,
        "odometer_end": odometer_end,
        "miles": total_miles,
        "tolls": tolls,
        "parking": parking,
        "reason": reason,
        "expenses": expenses
    }
    # create new window for adding trip
    trip_window = tk.Toplevel(root)
    trip_window.title("Add Trip")

    def get_trip_count():
    # count number of trips
        trip_count = len(trips)
        return trip_count

    # create entry fields for trip details
    departure_address_entry = tk.Entry(trip_window)
    arrival_address_entry = tk.Entry(trip_window)
    departure_time_entry = tk.Entry(trip_window)
    arrival_time_entry = tk.Entry(trip_window)
    reason_entry = tk.Entry(trip_window)
    odometer_beginning_entry = tk.Entry(trip_window)
    odometer_ending_entry = tk.Entry(trip_window)
    tolls_entry = tk.Entry(trip_window)
    parking_entry = tk.Entry(trip_window)

    # create labels for entry fields
    departure_address_label = tk.Label(trip_window, text="Departure Address:")
    arrival_address_label = tk.Label(trip_window, text="Arrival Address:")
    departure_time_label = tk.Label(trip_window, text="Departure Time:")
    arrival_time_label = tk.Label(trip_window, text="Arrival Time:")
    reason_label = tk.Label(trip_window, text="Reason for Trip:")
    odometer_beginning_label = tk.Label(trip_window, text="Odometer Reading at Beginning of Trip:")
    odometer_ending_label = tk.Label(trip_window, text="Odometer Reading at End of Trip:")
    tolls_label = tk.Label(trip_window, text="Tolls:")
    parking_label = tk.Label(trip_window, text="Parking:")

    # add labels and entry fields to window
    departure_address_label.grid(row=0, column=0)
    departure_address_entry.grid(row=0, column=1)
    arrival_address_label.grid(row=1, column=0)
    arrival_address_entry.grid(row=1, column=1)
    departure_time_label.grid(row=2, column=0)
    departure_time_entry.grid(row=2, column=1)
    arrival_time_label.grid(row=3, column=0)
    arrival_time_entry.grid(row=3, column=1)
    reason_label.grid(row=4, column=0)
    reason_entry.grid(row=4, column=1)
    odometer_beginning_label.grid(row=5, column=0)
    odometer_beginning_entry.grid(row=5, column=1)
    odometer_ending_label.grid(row=6, column=0)
    odometer_ending_entry.grid(row=6, column=1)
    tolls_label.grid(row=7, column=0)
    tolls_entry.grid(row=7, column=1)
    parking_label.grid(row=8, column=0)
    parking_entry.grid(row=8, column=1)

    # create button to submit trip details
    submit_button = tk.Button(trip_window, text="Submit", command=lambda: save_trip(departure_address_entry.get(), arrival_address_entry.get(), departure_time_entry.get(), arrival_time_entry.get(), reason_entry.get(), odometer_beginning_entry.get(), odometer_ending_entry.get(), tolls_entry.get(), parking_entry.get()))

    # add submit button to window
    submit_button.grid(row=9, column=0, columnspan=2)

    # create employee name entry field
    employee_name_entry = tk.Entry(trip_window)

    # create employee name label
    employee_name_label = tk.Label(trip_window, text="Employee Name:")

    # add employee name label and entry field to window
    employee_name_label.grid(row=10, column=0)
    employee_name_entry.grid(row=10, column=1)

    # update trip data display
    row = len(trips) + 1
    date_label = tk.Label(middle_frame, text=date)
    date_label.grid(row=row, column=0)

    departure_label = tk.Label(middle_frame, text=departure_address)
    departure_label.grid(row=row, column=1)

    arrival_label = tk.Label(middle_frame, text=arrival_address)
    arrival_label.grid(row=row, column=2)

    odometer_start_label = tk.Label(middle_frame, text=odometer_start)
    odometer_start_label.grid(row=row, column=3)

    odometer_end_label = tk.Label(middle_frame, text=odometer_end)
    odometer_end_label.grid(row=row, column=4)

    miles_label = tk.Label(middle_frame, text=total_miles)
    miles_label.grid(row=row, column=5)

    tolls_label = tk.Label(middle_frame, text=tolls)
    tolls_label.grid(row=row, column=6)

    parking_label = tk.Label(middle_frame, text=parking)
    parking_label.grid(row=row, column=7)

    reason_label = tk.Label(middle_frame, text=reason)
    reason_label.grid(row=row, column=8)

    expenses_label = tk.Label(middle_frame, text=expenses)
    expenses_label.grid(row=row, column=9)

    # update total miles driven display
    total_miles = sum(trip['miles'] for trip in trips.values())
    miles_display.config(text=total_miles)

    # clear input fields
    date_entry.delete(0, tk.END)
    departure_entry.delete(0, tk.END)
    arrival_entry.delete(0, tk.END)
    odometer_start_entry.delete(0, tk.END)
    odometer_end_entry.delete(0, tk.END)
    tolls_entry.delete(0, tk.END)
    parking_entry.delete(0, tk.END)
    reason_entry.delete(0, tk.END)

def export_to_excel():
    import pandas as pd

    # create pandas DataFrame from trips dictionary
    df = pd.DataFrame.from_dict(trips, orient='index', columns=['departure_address', 'arrival_address', 'departure_time', 'arrival_time', 'reason', 'odometer_beginning', 'odometer_ending', 'total_miles', 'tolls', 'parking'])

    # add header row for mileage report
    mileage_report = ["MILEAGE EXPENSE REPORT", "", ""]
    mileage_report.extend([""] * 5)
    mileage_report.append("TOTAL MILES")
    mileage_report.append("")
    mileage_report.append("Rate @ .59")
    mileage_report.append("0.59")
    mileage_report.append("Mileage Expense")
    mileage_report.append("")
    mileage_report.append("Tolls")
    mileage_report.append("")
    mileage_report.append("Parking")
    mileage_report.append("")
    mileage_report.append("")
    mileage_report.append("")
    mileage_report.append("")
    mileage_report.append("")
    mileage_report.append("")
    mileage_report.append("")
    mileage_report.append("")
    mileage_report.append("")
    mileage_report.append("")

    # add employee name and date to mileage report
    employee_name = employee_name_entry.get()
    if not employee_name:
        messagebox.showerror("Error", "Please enter employee name.")
        return
    mileage_report.insert(0, "")
    mileage_report.insert(0, f"EMPLOYEE NAME: {employee_name}")
    mileage_report.insert(0, "")
    mileage_report.insert(0, f"DATE: {datetime.now().strftime('%m/%d/%Y')}")

    # add mileage report header row to DataFrame
    df.loc[''] = mileage_report

    # re-order DataFrame columns
    df = df[['departure_address', 'arrival_address', 'reason', 'odometer_beginning', 'odometer_ending', 'total_miles', 'tolls', 'parking']]

    # calculate total miles
    total_miles = df['total_miles'].sum()

    # calculate total expenses
    total_expenses = round((total_miles * 0.59) + df['tolls'].sum() + df['parking'].sum(), 2)

    # add total row to DataFrame
    df.loc['TOTAL'] = ['', '', '', '', '', total_miles, df['tolls'].sum(), df['parking'].sum()]

    # add empty row to DataFrame
    df.loc[''] = ['', '', '', '', '', '', '', '']

    # add expense report footer to DataFrame
    df.loc[''] = ['', '', '', '', '', '', '', '']
    df.loc[''] = ['', '', '', '', '', '', '', '']
    df.loc[''] = ['', '', '', '', '', '', '', '']
    df.loc[''] = ['', '', '', '', '', '', '', '']
    df.loc[''] = ['', '', '', '', '', '', '', '']
    df.loc[''] = ['', '', '', '', '', '', '', '']
    df.loc['I VERIFY THIS EXPENSE REPORT TO BE TRUE AND CORRECT:', '', '', '', '', '', '', '']
    df.loc[''] = ['Total Miles', '-', '', '', '', total_miles, 'Rate @ .59', 0.59, 'Mileage Expense', '', 'Tolls', '', 'Parking', '', '', '', '', '', '', '', '', '']
    df.loc[''] = ['', '', '', '', '', '', '', '']
    df.loc[''] = ['', '', '', '', '', '', '', '']
    df.loc['EMPLOYEE SIGNATURE:', '', '', '', '', '', '', '']
    df.loc[''] = ['', '', '', '', '', '', '', '']

    # export DataFrame to Excel
    filename = f"{employee_name_entry.get()}_{datetime.now().strftime('%m_%d_%Y')}.xlsx"
    df.to_excel(filename)

    # clear trips dictionary and reset trip counter
    trips.clear()
    trip_count.set(0)

    # show success message
    messagebox.showinfo("Export to Excel", f"Mileage report has been exported to {filename}.")


def calculate_miles(departure_address, arrival_address):
    # Use the Google Maps Distance Matrix API to retrieve the distance between the departure and arrival addresses
    directions_result = gmaps.directions(departure_address, arrival_address, mode="driving")

    # Extract the distance value from the API response
    total_distance_meters = directions_result[0]['legs'][0]['distance']['value']

    # Convert the distance from meters to miles
    total_miles = total_distance_meters * 0.000621371

    # Return the total miles
    return total_miles


# create main window
root = tk.Tk()
root.title("Mileage Tracker")

# create header frame
header_frame = tk.Frame(root)
header_frame.pack(pady=10)

header_label = tk.Label(header_frame, text="Mileage Tracker", font=("Arial", 24))
header_label.pack()

# create input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

date_label = tk.Label(input_frame, text="Date (MM/DD/YYYY):", font=("Arial", 12))
date_label.grid(row=0, column=0)

date_entry = tk.Entry(input_frame, font=("Arial", 12))
date_entry.grid(row=0, column=1)

departure_label = tk.Label(input_frame, text="Departure Address:", font=("Arial", 12))
departure_label.grid(row=1, column=0)

departure_entry = tk.Entry(input_frame, font=("Arial", 12))
departure_entry.grid(row=1, column=1)

arrival_label = tk.Label(input_frame, text="Arrival Address:", font=("Arial", 12))
arrival_label.grid(row=2, column=0)

arrival_entry = tk.Entry(input_frame, font=("Arial", 12))
arrival_entry.grid(row=2, column=1)

odometer_start_label = tk.Label(input_frame, text="Odometer Start:", font=("Arial", 12))
odometer_start_label.grid(row=3, column=0)

odometer_start_entry = tk.Entry(input_frame, font=("Arial", 12))
odometer_start_entry.grid(row=3, column=1)

odometer_end_label = tk.Label(input_frame, text="Odometer End:", font=("Arial", 12))
odometer_end_label.grid(row=4, column=0)

odometer_end_entry = tk.Entry(input_frame, font=("Arial", 12))
odometer_end_entry.grid(row=4, column=1)

tolls_label = tk.Label(input_frame, text="Tolls:", font=("Arial", 12))
tolls_label.grid(row=5, column=0)

tolls_entry = tk.Entry(input_frame, font=("Arial", 12))
tolls_entry.grid(row=5, column=1)

parking_label = tk.Label(input_frame, text="Parking:", font=("Arial", 12))
parking_label.grid(row=6, column=0)

parking_entry = tk.Entry(input_frame, font=("Arial", 12))
parking_entry.grid(row=6, column=1)

reason_label = tk.Label(input_frame, text="Reason for Trip:", font=("Arial", 12))
reason_label.grid(row=7, column=0)

reason_entry = tk.Entry(input_frame, font=("Arial", 12))
reason_entry.grid(row=7, column=1)



add_button = tk.Button(input_frame, text="Add Trip", font=("Arial", 12), command=add_trip)
add_button.grid(row=8, column=1, pady=10)

# create middle frame
middle_frame = tk.Frame(root)
middle_frame.pack()

# create trip data labels
date_label = tk.Label(middle_frame, text="Date", font=("Arial", 12, "bold"))
date_label.grid(row=0, column=0)

departure_label = tk.Label(middle_frame, text="Departure Address", font=("Arial", 12, "bold"))
departure_label.grid(row=0, column=1)

arrival_label = tk.Label(middle_frame, text="Arrival Address", font=("Arial", 12, "bold"))
arrival_label.grid(row=0, column=2)

odometer_start_label = tk.Label(middle_frame, text="Odometer Start", font=("Arial", 12, "bold"))
odometer_start_label.grid(row=0, column=3)

odometer_end_label = tk.Label(middle_frame, text="Odometer End", font=("Arial", 12, "bold"))
odometer_end_label.grid(row=0, column=4)

miles_label = tk.Label(middle_frame, text="total_miles", font=("Arial", 12, "bold"))
miles_label.grid(row=0, column=5)

tolls_label = tk.Label(middle_frame, text="Tolls", font=("Arial", 12, "bold"))
tolls_label.grid(row=0, column=6)

parking_label = tk.Label(middle_frame, text="Parking", font=("Arial", 12, "bold"))
parking_label.grid(row=0, column=7)

reason_label = tk.Label(middle_frame, text="Reason", font=("Arial", 12, "bold"))
reason_label.grid(row=0, column=8)

expenses_label = tk.Label(middle_frame, text="Expenses", font=("Arial", 12, "bold"))
expenses_label.grid(row=0, column=9)

# create footer frame
footer_frame = tk.Frame(root)
footer_frame.pack(pady=10)

total_miles_label = tk.Label(footer_frame, text="Total Miles Driven:", font=("Arial", 12))
total_miles_label.pack(side=tk.LEFT)

miles_display = tk.Label(footer_frame, text="0", font=("Arial", 12))
miles_display.pack(side=tk.LEFT, padx=10)

export_button = tk.Button(footer_frame, text="Export to Excel", font=("Arial", 12), command=export_to_excel)
export_button.pack(side=tk.LEFT)

status_message = tk.Label(footer_frame, text="", font=("Arial", 12))
status_message.pack(side=tk.LEFT, padx=10)

# create dictionary to hold trip data
trips = {}

# start main loop
root.mainloop()
