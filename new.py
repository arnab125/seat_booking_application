
class Star_Cinema:
    def __init__(self):
        self.hall_list = []

    def entry_hall(self, rows, cols, hall_no):
        new_hall = Hall(rows, cols, hall_no)
        self.hall_list.append(new_hall)
        return self.hall_list


class Hall(Star_Cinema):

    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []
        super().__init__()

    def __repr__(self):
        return f"{self.rows} {self.cols} {self.hall_no}"

    def entry_show(self, id=0, movie_name=0, time=0):
        row = []
        for i in range(self.rows):
            col = []
            for j in range(self.cols):
                col.append(f"{i},{j}")
            row.append(col)

        seats_info = {id: row}
        self.seats.update(seats_info)
        self.show_list.append([id, movie_name, time])
        return self.show_list

    def book_seats(self, person_name, phone_no, id, seat_no):
        a=self.entry_show()
        r,c=seat_no.split(",")
        if (id == a[0][0]):
            self.seats[id][int(r)][int(c)] = '\033[1m' + 'X' + '\033[0m'
            return (self.seats[id])
        elif (id == a[1][0]):
            self.seats[id][int(r)][int(c)] = '\033[1m' + 'X' + '\033[0m'
            return (self.seats[id])
        else:
            print("Invalid ID")

    def view_show_list(self):
        a = self.entry_show()
        print("Show ID","       " ,"Show Name","       " ,"Show Time")
        print("-----------------------------------------------------")
        for i in range(2):
            print(a[i][0],"          " ,a[i][1],"          " ,a[i][2])
        print("-----------------------------------------------------")


    def view_available_seats(self,id):
        a = self.entry_show()
        value=65
        if (id == a[0][0]):
            for i in range(self.rows):
                for j in range(self.cols):
                    print("(",self.seats["ay0"][i][j],")",f"{chr(value)}{j}", end="            ")
                print()
                value+=1
            #print(self.seats["ay0"])
        elif (id == a[1][0]):
            for i in range(self.rows):
                for j in range(self.cols):
                    print("(",self.seats["sk0"][i][j],")", f"{chr(value)}{j}", end="            ")
                print()
                value += 1
        else:
            print("Invalid ID")

def showreplica():
    print("1.View all shows today")
    print("2.View available tickets")
    print("3.Book tickets")

col=4
row=3
hall_no="A10"
hall = Hall(row, col, hall_no)
hall.entry_show('ay0', 'Avengers', '10:00')
hall.entry_show('sk0', 'Spiderman', '12:00')

while True:
    showreplica()
    a=input("Enter option : ")
    if(a=="1"):
        hall.view_show_list()
    elif(a=="2"):
        id = input("Enter show id : ")
        print("_"*20*col)
        if (id == hall.show_list[0][0]):
            print(f"Movie name: {hall.show_list[0][1]}        Time: {hall.show_list[0][2]}")
            print("x for already booked seats")
            hall.view_available_seats(id)
        elif (id == hall.show_list[1][0]):
            print(f"Movie name: {hall.show_list[1][1]}        Time: {hall.show_list[1][2]}")
            print("x for already booked seats")
            hall.view_available_seats(id)
        print("_"*20*col)
    elif(a=="3"):
        name = input("Enter name : ")
        phone = input("Enter phone no : ")
        id = input("Enter show id : ")
        hall.view_available_seats(id)
        no_of_seats = int(input("Enter no of seats : "))
        seat_list = []
        for i in range(no_of_seats):
            seat_no = input("Enter seat no : ")
            hall.book_seats(name, phone, id, seat_no)
            seat_list.append(seat_no)
            print("_" * 20 * col)
            hall.view_available_seats(id)
            print("_" * 20 * col)
        print("Tickets booked successfully")
        print("Thank you for booking with us")
        print("_"*50)
        print("Name : ",name)
        print("Phone no : ",phone)
        print()
        if (id == hall.show_list[0][0]):
            print(f"Movie name: {hall.show_list[0][1]}        Time: {hall.show_list[0][2]}")
        elif (id == hall.show_list[1][0]):
            print(f"Movie name: {hall.show_list[1][1]}        Time: {hall.show_list[1][2]}")
        print("seat no : ",end = " ")
        for i in range(no_of_seats):
            print("(",seat_list[i],")", end = " ")
        print()
        print("Hall no : ",hall.hall_no)
        print("_"*50)
    else:
        print("Invalid option")