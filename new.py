def convert(s):
    listed = []
    tupled = ()
    if s[0].isalpha():
        tupled=(*tupled,str(ord(s[0].upper())-65),s[1])
        listed.append(tupled)
    return listed
#print(convert("A2"))
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
        r,c=seat_no[0]
        if (id == a[0][0]):
            self.seats[id][int(r)][int(c)] = '\033[1m' + '\033[31m' +'X' + '\033[0m'
            return (self.seats[id])
        elif (id == a[1][0]):
            self.seats[id][int(r)][int(c)] = '\033[1m' + '\033[31m' +'X' + '\033[0m'
            return (self.seats[id])

    def view_show_list(self):
        a = self.entry_show()
        print('\033[1m' + 'Movie Id' + '\033[0m',"       " ,'\033[1m' + 'Movie Name' + '\033[0m',"       " ,'\033[1m' + 'Time' + '\033[0m')
        print("_____________________________________________________")
        for i in range(2):
            print(a[i][0],"          " ,a[i][1],"          " ,a[i][2])
        print("_____________________________________________________")

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

def showreplica():
    print('\033[1m' + '\033[32m' + '1.View running show' + '\033[0m')
    print('\033[1m' + '\033[32m' + '2.View available seats' + '\033[0m')
    print('\033[1m' + '\033[32m' +'3.Book tickets' + '\033[0m')

col=4
row=3
hall_no="A10"
hall = Hall(row, col, hall_no)
hall.entry_show('ay0', 'Avengers', '10:00')
hall.entry_show('sk0', 'Spiderman', '12:00')
print(hall.seats)
print(convert("A2")[0])

while True:
    showreplica()
    a=input('\033[1m' + 'Enter your choice:' + '\033[0m')
    print()
    if(a=="1"):
        hall.view_show_list()
    elif(a=="2"):
        id = input("Enter show id : ")
        while id not in hall.show_list[0] and id not in hall.show_list[1]:
            print('\033[31m'+'\033[1m' + 'INVALID SHOW ID.PLEASE SELECT AGAIN.' + '\033[0m')
            id = input("Enter show id : ")
        print("_"*20*col)
        if (id == hall.show_list[0][0]):
            print(f"\033[1m Movie Name : \033[0m {hall.show_list[0][1]}        \033[1m Time : \033[0m {hall.show_list[0][2]}")
            print('\033[1m' + '\033[31m' +'X' + '\033[0m' + " for already Booked Seats.")
            hall.view_available_seats(id)
        elif (id == hall.show_list[1][0]):
            print(f"\033[1m Movie Name : \033[0m {hall.show_list[1][1]}       \033[1m Time : \033[0m {hall.show_list[1][2]}")
            print('\033[1m' + '\033[31m' +'X' + '\033[0m' + " for already Booked Seats.")
            hall.view_available_seats(id)
        print("_"*20*col)
    elif(a=="3"):
        name = input("Enter name : ")
        phone = input("Enter phone no : ")
        id = input("Enter show id : ")
        while id not in hall.show_list[0] and id not in hall.show_list[1]:
            print('\033[31m'+'\033[1m' + 'Invalid show id.please select again.' + '\033[0m')
            id = input("Enter show id : ")
        #hall.view_available_seats(id)
        no_of_seats = int(input("Enter no of seats : "))
        seat_list = []
        for i in range(no_of_seats):
            seat= input("Enter seat no : ")
            while int(convert(seat)[0][0])>=row or int(convert(seat)[0][0])<0 or int(convert(seat)[0][1])>=col or int(convert(seat)[0][1])<0:
                print('\033[31m'+'\033[1m' + 'Invalid seat.please select again.' + '\033[0m')
                seat= input("Enter seat no : ")
            while seat in seat_list:
                print('\033[31m'+'\033[1m' + 'Seat already booked.please try again.' + '\033[0m')
                seat = input("Enter seat no : ")
            seat_no = convert(seat)
            hall.book_seats(name, phone, id, seat_no)
            seat_list.append(seat)
            #print("_" * 20 * col)
            #hall.view_available_seats(id)
            #print("_" * 20 * col)
        print('\033[92m'+'\033[1m' + 'Tickets booked successfully' + '\033[0m')
        print('\033[92m'+'\033[1m' + 'Thank you & Enjoy' + '\033[0m')
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
        print('\033[31m'+'\033[1m' + 'Invalid option.Please select again.' + '\033[0m')
        print()
