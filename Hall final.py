
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

    def entry_show(self, id_show=0, name_show=0, time_show=0):
        self.seats_info = {id_show: [["A0", "A1", "A2"], ["B0", "B1", "B2"]]}
        self.seats.update(self.seats_info)
        self.show_list.append([id_show, name_show, time_show])
        return self.show_list

    def book_seats(self, person_name, phone_no, id_show, seat_no):
        a=self.entry_show()
        if (id_show == a[0][0]):
            for i in range (2):
                for j in range(3):
                    if (seat_no == self.seats[id_show][i][j]):
                        self.seats[id_show][i][j] = "X"
            return (self.seats[id_show])
        elif (id_show == a[1][0]):
            for i in range (2):
                for j in range(3):
                    if (seat_no == self.seats[id_show][i][j]):
                        self.seats[id_show][i][j] = "X"
            return (self.seats[id_show])
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
        if (id == a[0][0]):
            print(self.seats["ay0"])
        elif (id == a[1][0]):
            print(self.seats["sk0"])
        else:
            print("Invalid ID")

def showreplica():
    print("1.View all shows today")
    print("2.View available tickets")
    print("3.Book tickets")


hall = Hall(1, 2, 3)
hall.entry_show('ay0', 'Avengers', '10:00')
hall.entry_show('sk0', 'Spiderman', '12:00')

while True:
    showreplica()
    a=input("Enter option : ")
    if(a=="1"):
        hall.view_show_list()
    elif(a=="2"):
        id = input("Enter show id : ")
        hall.view_available_seats(id)
    elif(a=="3"):
        """id = input("Enter show id : ")
        seat_no = input("Enter seat no : ")
        hall.book_seats("A", 123, id, seat_no)"""
        name = input("Enter name : ")
        phone = input("Enter phone no : ")
        id = input("Enter show id : ")
        hall.view_available_seats(id)
        no_of_seats = int(input("Enter no of seats : "))
        for i in range(no_of_seats):
            seat_no = input("Enter seat no : ")
            hall.book_seats(name, phone, id, seat_no)
            hall.view_available_seats(id)
    else:
        print("Invalid option")