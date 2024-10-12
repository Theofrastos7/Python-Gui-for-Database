import matplotlib.pyplot as plt
import customtkinter
import csv
import mysql.connector

#graphs gia ola ta erothmata parakato
def hotel_cancel_graph():
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    fig.suptitle('Cancellation Percentage by Hotel Type', fontsize=16)
    # Pie chart for Resort
    axs[0].pie([resort_cancellation_percentage, 100 - resort_cancellation_percentage],
               labels=['Cancelled', 'Not Cancelled'], autopct='%1.1f%%', colors=['red', 'blue'])
    axs[0].set_title('Resort Cancellation Percentage')

    # Pie chart for City
    axs[1].pie([city_cancellation_percentage, 100 - city_cancellation_percentage],
               labels=['Cancelled', 'Not Cancelled'], autopct='%1.1f%%', colors=['red', 'green'])
    axs[1].set_title('City Cancellation Percentage')

    plt.show()


def hotel_average_graph():
    hotels = ['Resort', 'City']
    average_days = [resort_days_average, city_days_average]

    plt.figure(figsize=(8, 6))
    #bar graph opos kai ta upoloipa
    plt.bar(hotels, average_days, color=['blue', 'green'])

    plt.xlabel('Hotel Type')
    plt.ylabel('Average Days')
    plt.title('Average Days by Hotel Type')

    plt.show()


def month_graph():
    plt.figure(figsize=(10, 5))
    plt.bar(months_list, bookings_per_month.values(), color='skyblue')
    plt.xlabel('Month')
    plt.ylabel('Number of Bookings')
    plt.title('Hotel Bookings per Month')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def season_graph():
    seasons = ['Winter', 'Spring', 'Summer', 'Autumn']
    season_bookings = [winter_bookings, spring_bookings, summer_bookings, autumn_bookings]

    plt.figure(figsize=(6, 4))
    plt.bar(seasons, season_bookings, color='lightgreen')
    plt.xlabel('Season')
    plt.ylabel('Number of Bookings')
    plt.title('Hotel Bookings per Season')
    plt.tight_layout()
    plt.show()


def room_graph():
    plt.figure(figsize=(8, 6))
    plt.bar(room_bookings.keys(), room_bookings.values(), color='lightcoral')
    plt.xlabel('Room Type')
    plt.ylabel('Number of Bookings')
    plt.title('Room Bookings per Room Type')
    plt.tight_layout()
    plt.show()


def visitor_graph():
    visitor_types = ['Families', 'Singles', 'Couples', 'Other']
    visitor_counts = [families, singles, couples, rest]

    plt.figure(figsize=(6, 4))
    plt.bar(visitor_types, visitor_counts, color='lightblue')
    plt.xlabel('Visitor Type')
    plt.ylabel('Number of Bookings')
    plt.title('Bookings by Visitor Type')
    plt.tight_layout()
    plt.show()


def booking_tendencies():
    bookings_data = [bookings_per_month[month] for month in months_list]
    #gia kathe mhna apothykeuoyme tis plhrofories to bookings_data
    plt.figure(figsize=(10, 6))
    plt.plot(months_list, bookings_data, marker='o', linestyle='-')
    plt.title('Hotel Bookings per Month Over Time')
    plt.xlabel('Month')
    plt.ylabel('Number of Bookings')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def resort_season():
    seasons = ['Summer', 'Spring', 'Autumn', 'Winter']
    bookings_resort = [resort_summer, resort_spring, resort_autumn, resort_winter]
    cancellations_resort = [resort_summer_cancel, resort_spring_cancel, resort_autumn_cancel, resort_winter_cancel]

    plt.figure(figsize=(8, 6))

    #gia kathe mhna xrhsimopoioyme to season_labels
    season_labels = [season for season in seasons]

    plt.bar(season_labels, bookings_resort, color='lightblue', label='Bookings')
    plt.bar(season_labels, cancellations_resort, color='orange', label='Cancellations')

    plt.xlabel('Season')
    plt.ylabel('Bookings')
    plt.title('Resort Bookings and Cancellations by Season')
    plt.legend()
    plt.tight_layout()
    plt.show()


def city_season():
    seasons = ['Summer', 'Spring', 'Autumn', 'Winter']
    bookings_city = [city_summer, city_spring, city_autumn, city_winter]
    cancellations_city = [city_summer_cancel, city_spring_cancel, city_autumn_cancel, city_winter_cancel]

    plt.figure(figsize=(8, 6))

    season_labels = [season for season in seasons]

    plt.bar(season_labels, bookings_city, color='lightblue', label='Bookings')
    plt.bar(season_labels, cancellations_city, color='orange', label='Cancellations')

    plt.xlabel('Season')
    plt.ylabel('Bookings')
    plt.title('City Bookings and Cancellations by Season')
    plt.legend()
    plt.tight_layout()
    plt.show()

#synarthsh gia export enos csv. san orisma dexetai to titlo tou pinaka ths bashs kai to onoma tou arxeioy export
def export_to_csv(table_name, file_name):
    mycursor.execute(f"SELECT * FROM {table_name}") #select query
    result = mycursor.fetchall() #result = oles oi sthles
    #dhmiourgia arxeioy an den yparxei, kai write tous titlous ton sthlon kai ta periexomena tous
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([i[0] for i in mycursor.description])
        writer.writerows(result)
    print(f"\n{table_name} data exported to {file_name}")

#synarthsh gia ola ta export. kalei thn parapano synarthsh gia kathe pinaka
def export_all_csv():
    export_to_csv("cancellation_percentage", "cancellation_percentage.csv")
    export_to_csv("average_days", "average_days.csv")
    export_to_csv("month_bookings", "month_bookings.csv")
    export_to_csv("room_types", "room_types.csv")
    export_to_csv("visitor_types", "visitor_types.csv")
    export_to_csv("resort_season", "resort_season.csv")
    export_to_csv("city_season", "city_season.csv")

#epafh me thn customtkinter
def create_interface():
    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("dark-blue")
    #root sto opoio tha mpoun ta koumpia
    root = customtkinter.CTk()
    #titlos diepafhs
    root.title("Graph Options")
    #koumpi. orizoume to text tou koumpiou, thn synarthsh pou kalh kai ths syntetagmenes sto plaisio
    my_button0 = customtkinter.CTkButton(root, text="Hotel Cancel Graph", command=hotel_cancel_graph)
    my_button0.place(x=70, y=60)
    #omoios
    my_button1 = customtkinter.CTkButton(root, text="Average Days Graph", command=hotel_average_graph)
    my_button1.place(x=270, y=60)

    my_button2 = customtkinter.CTkButton(root, text="Month Graph", command=month_graph)
    my_button2.place(x=70, y=140)

    my_button3 = customtkinter.CTkButton(root, text="Season Graph", command=season_graph)
    my_button3.place(x=270, y=140)

    my_button4 = customtkinter.CTkButton(root, text="Visitor Graph", command=visitor_graph)
    my_button4.place(x=70, y=220)

    my_button5 = customtkinter.CTkButton(root, text="Booking Tendencies", command=booking_tendencies)
    my_button5.place(x=270, y=220)

    my_button6 = customtkinter.CTkButton(root, text="Resort Season", command=resort_season)
    my_button6.place(x=70, y=380)

    my_button7 = customtkinter.CTkButton(root, text="Room Graph", command=room_graph)
    my_button7.place(x=70, y=300)

    my_button8 = customtkinter.CTkButton(root, text="Export CSV", command=export_all_csv)
    my_button8.place(x=270, y=300)

    my_button9 = customtkinter.CTkButton(root, text="City Season", command=city_season)
    my_button9.place(x=270, y=380)
    #megethos plaisiou
    root.geometry("500x450")

    root.mainloop()


########### MAIN #############

#connect to database
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='12345theo',
    database="python_database"
)
#cursor gia thn bash
mycursor = mydb.cursor()

#create bash an den yparxei hdh
mycursor.execute("CREATE DATABASE IF NOT EXISTS python_database")

#filepath toy hotel_booking.csv
file_path = 'C:/Users/Theo/Downloads/sixth_semester/python/hotel_booking.csv'
data = []
#copy csv ston pinaka data
with open(file_path, 'r', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row)

############### A ###############


#metrhtes gia cancelation kai days gia to kathe jenadoxeio
resort_bookings = 0
resort_canceled_bookings = 0
resort_days = 0
city_bookings = 0
city_canceled_bookings = 0
city_days = 0

#for sto opoio ypologizoume toys parapano metrhtes
for row in data[1:]:
    if row[0] == 'Resort Hotel':
        resort_bookings += 1

        resort_days += int(row[7])
        resort_days += int(row[8])

        if row[1] == '1':
            resort_canceled_bookings += 1

    if row[0] == 'City Hotel':
        city_bookings += 1

        city_days += int(row[7])
        city_days += int(row[8])

        if row[1] == '1':
            city_canceled_bookings += 1

resort_cancellation_percentage = (resort_canceled_bookings / resort_bookings) * 100
city_cancellation_percentage = (city_canceled_bookings / city_bookings) * 100

resort_days_average = (resort_days / resort_bookings)
city_days_average = (city_days / city_bookings)

print("Cancellation percentage for Resort: {:.2f}%".format(resort_cancellation_percentage))
print("Average days for Resort: {:.2f}".format(resort_days_average))

print("\nCancellation percentage for City: {:.2f}%".format(city_cancellation_percentage))
print("Average days for City: {:.2f}".format(city_days_average))
#dhmiourgia pinaka gia ta apotelesmata + inserts ston pinaka
mycursor.execute("CREATE TABLE cancellation_percentage (hotel_name VARCHAR(20), percentage FLOAT)")
sql = "INSERT INTO cancellation_percentage (hotel_name, percentage) VALUES (%s, %s)"
val = [('Resort Hotel', resort_cancellation_percentage), ('City Hotel', city_cancellation_percentage)]

mycursor.executemany(sql, val)

mydb.commit()

mycursor.execute("CREATE TABLE average_days (hotel_name VARCHAR(20), average FLOAT)")
sql = "INSERT INTO average_days (hotel_name, average) VALUES (%s, %s)"
val = [('Resort Hotel', resort_days_average), ('City Hotel', city_days_average)]

mycursor.executemany(sql, val)

mydb.commit()

################## END OF A ##################
#dictionary month_list me kleidia toys mhnes
months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
               'November', 'December']
#arxikopoihsh dictionary me times 0
bookings_per_month = {booking_month: 0 for booking_month in months_list}
#enhmerosh dictionary
for row in data[1:]:
    month = row[4]

    bookings_per_month[month] += 1

print("\nHotel Bookings per Month:")
for month in months_list:
    print(str(month) + ": " + str(bookings_per_month[month]))
#ypologismos gia kathe epoxh
winter_bookings = bookings_per_month['January'] + bookings_per_month['February'] + bookings_per_month['December']

spring_bookings = bookings_per_month['March'] + bookings_per_month['April'] + bookings_per_month['May']

summer_bookings = bookings_per_month['June'] + bookings_per_month['July'] + bookings_per_month['August']

autumn_bookings = bookings_per_month['September'] + bookings_per_month['October'] + bookings_per_month['November']

print("\nHotel Bookings per season:")
print("Winter: ", winter_bookings)
print("Spring: ", spring_bookings)
print("Summer: ", summer_bookings)
print("Autumn: ", autumn_bookings)
#create kai insert sthn bash
mycursor.execute("CREATE TABLE month_bookings (month VARCHAR(20), bookings INT)")
sql = "INSERT INTO month_bookings (month, bookings) VALUES (%s, %s)"
val = [(month, bookings) for month, bookings in bookings_per_month.items()]
mycursor.executemany(sql, val)
mydb.commit()

mycursor.execute("CREATE TABLE season_bookings (season VARCHAR(20), bookings INT)")
sql = "INSERT INTO season_bookings (season, bookings) VALUES (%s, %s)"
val = [('Winter', winter_bookings), ('Spring', spring_bookings), ('Summer', summer_bookings),
       ('Autumn', autumn_bookings)]
mycursor.executemany(sql, val)
mydb.commit()

####################### END OF B ############

#dictionary gia ta domatia
room_types = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'}
#dictionary 0 gia kathe domatio arxika
room_bookings = {room_type: 0 for room_type in room_types}

for row in data[1:]:
    room_type = row[20]

    if room_type in room_types:
        room_bookings[room_type] += 1

print("\nRoom Bookings per Room Type:")
for room_type in room_types:
    print(str(room_type) + ": " + str(room_bookings[room_type]))
#create + insert
mycursor.execute("CREATE TABLE room_types (room VARCHAR(20), bookings INT)")
sql = "INSERT INTO room_types (room, bookings) VALUES (%s, %s)"
val = [(room_type, room_bookings[room_type]) for room_type in sorted(room_bookings.keys())]
mycursor.executemany(sql, val)
mydb.commit()

################### END OF C ################
#metrhtes gia kathe eidos pelaton
couples = 0
singles = 0
families = 0
rest = 0

line_number = 1
#enhmerosh ton parapano deikton
for row in data[1:]:
    adults = int(row[9])
    if row[10] == "": #problhma toy csv
        children = 0
    else:
        children = float(row[10])
    babies = int(row[11])

    if (adults == 1 and children == 0 and babies == 0):
        singles += 1

    elif (adults == 0 and children == 1 and babies == 0):
        singles += 1

    elif (adults == 2 and children == 0 and babies == 0):
        couples += 1


    elif (adults > 1 and (children > 0 or babies > 0)):
        families += 1

    else:
        rest += 1

print("\nBookings per type:")
print("Total Families: ", families)
print("Total Singles: ", singles)
print("Total Couples: ", couples)
print("Other: ", rest)
# create + insert
mycursor.execute("CREATE TABLE visitor_types (visitor VARCHAR(20), bookings INT)")
sql = "INSERT INTO visitor_types (visitor, bookings) VALUES (%s, %s)"
val = [('Families', families), ('Singles', singles), ('Couples', couples), ('Other', rest)]
mycursor.executemany(sql, val)
mydb.commit()

################# END OF D #########
resort_winter = 0
resort_spring = 0
resort_summer = 0
resort_autumn = 0
resort_winter_cancel = 0
resort_spring_cancel = 0
resort_summer_cancel = 0
resort_autumn_cancel = 0
#counters gia ths krathseis kai akyroseis kathe jenadoxeiou ana epoxh
city_winter = 0
city_spring = 0
city_summer = 0
city_autumn = 0
city_winter_cancel = 0
city_spring_cancel = 0
city_summer_cancel = 0
city_autumn_cancel = 0
#enhmerosh parapano counters
for row in data[1:]:
    if row[0] == 'Resort Hotel':
        if row[4] == 'June' or row[4] == 'July' or row[4] == 'August':
            resort_summer += 1
            if row[1] == '1':
                resort_summer_cancel += 1
        if row[4] == 'September' or row[4] == 'October' or row[4] == 'November':
            resort_autumn += 1
            if row[1] == '1':
                resort_autumn_cancel += 1
        if row[4] == 'December' or row[4] == 'January' or row[4] == 'February':
            resort_winter += 1
            if row[1] == '1':
                resort_winter_cancel += 1
        if row[4] == 'March' or row[4] == 'April' or row[4] == 'May':
            resort_spring += 1
            if row[1] == '1':
                resort_spring_cancel += 1
    if row[0] == 'City Hotel':
        if row[4] == 'June' or row[4] == 'July' or row[4] == 'August':
            city_summer += 1
            if row[1] == '1':
                city_summer_cancel += 1
        if row[4] == 'September' or row[4] == 'October' or row[4] == 'November':
            city_autumn += 1
            if row[1] == '1':
                city_autumn_cancel += 1
        if row[4] == 'December' or row[4] == 'January' or row[4] == 'February':
            city_winter += 1
            if row[1] == '1':
                city_winter_cancel += 1
        if row[4] == 'March' or row[4] == 'April' or row[4] == 'May':
            city_spring += 1
            if row[1] == '1':
                city_spring_cancel += 1

print("\nHotels per season: ")
print("Resort in Summer. Bookings: " + str(resort_summer) + ". Cancellations: " + str(resort_summer_cancel))
print("Resort in Spring. Bookings: " + str(resort_spring) + ". Cancellations: " + str(resort_spring_cancel))
print("Resort in Autumn. Bookings: " + str(resort_autumn) + ". Cancellations: " + str(resort_autumn_cancel))
print("Resort in Winter. Bookings: " + str(resort_winter) + ". Cancellations: " + str(resort_winter_cancel))

print("\nCity in Summer. Bookings: " + str(city_summer) + ". Cancellations: " + str(city_summer_cancel))
print("City in Spring. Bookings: " + str(city_spring) + ". Cancellations: " + str(city_spring_cancel))
print("City in Autumn. Bookings: " + str(city_autumn) + ". Cancellations: " + str(city_autumn_cancel))
print("City in Winter. Bookings: " + str(city_winter) + ". Cancellations: " + str(city_winter_cancel))
#create + inserts
mycursor.execute("CREATE TABLE resort_season (name VARCHAR(20), season VARCHAR(20), "
                 "bookings INT, cancellations INT)")
sql = "INSERT INTO resort_season (name, season, bookings, cancellations) VALUES (%s, %s, %s, %s)"
val = [
    ('Resort Hotel', 'Winter', resort_winter, resort_winter_cancel),
    ('Resort Hotel', 'Summer', resort_summer, resort_summer_cancel),
    ('Resort Hotel', 'Autumn', resort_autumn, resort_autumn_cancel),
    ('Resort Hotel', 'Spring', resort_spring, resort_spring_cancel)]
mycursor.executemany(sql, val)
mydb.commit()

mycursor.execute("CREATE TABLE city_season (name VARCHAR(20), season VARCHAR(20), "
                 "bookings INT, cancellations INT)")
sql = "INSERT INTO city_season (name, season, bookings, cancellations) VALUES (%s, %s, %s, %s)"
val = [
    ('City Hotel', 'Winter', city_winter, city_winter_cancel),
    ('City Hotel', 'Summer', city_summer, city_summer_cancel),
    ('City Hotel', 'Autumn', city_autumn, city_autumn_cancel),
    ('City Hotel', 'Spring', city_spring, city_spring_cancel)]
mycursor.executemany(sql, val)
mydb.commit()

#### INTERFACE ######
#create interface apo thn synarthsh pio pano
create_interface()
