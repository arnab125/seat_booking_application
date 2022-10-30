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

    def entry_show(self):
        self.movie1 = ("ay0", "Aynabazi", "12ta")
        self.movie2 = ("sk0", "Skyfall", "12ta")
        self.show_list.append(self.movie1)
        self.show_list.append(self.movie2)
        self.seats = {"ay0": [["A0", "A1", "A2"], ["B0", "B1", "B2"]], "sk0": [["A0", "A1", "A2"], ["B0", "B1", "B2"]]}
        return self.show_list

    def book_seats(self, person_name, phone_no, id_show):
            a=self.entry_show()
            b=self.movie1[0]
            c=self.movie2[0]
            #print(a)
            if (id_show == a[0][0]):
              print(self.seats["ay0"])
            elif (id_show == a[1][0]):
              print(self.seats["sk0"])


    def view_show_list(self):
        b = self.entry_show()
        print("------------------------------------------------------------------------------")
        print("running these shows successfully:")
        print("")
        #print("______________________________________________________________________________")
        print(f"Movie name: {b[0][1]}       Movie id : {b[0][0]}         Time: {b[0][2]}")
        print(f"Movie name: {b[1][1]}        Movie id : {b[1][0]}         Time: {b[1][2]}")
        print("------------------------------------------------------------------------------")


    def view_available_seats(self,id):
        a = self.entry_show()
        # print(a)
        if (id == a[0][0]):
            for i in range(3):
                print(self.seats["ay0"][0][i],end="       ")
            print()
            for i in range(3):
                print(self.seats["ay0"][1][i], end="       ")
        elif (id == a[1][0]):
            for i in range(3):
                print(self.seats["sk0"][0][i], end="       ")
            print()
            for i in range(3):
                print(self.seats["sk0"][1][i], end="       ")

def showreplica():
    print("1.View all shows today")
    print("2.View available tickets")
    print("3.Book tickets")


hall1=Hall(1, 2, 3).entry_show()
print(hall1)
hall2=Hall(1, 2, 3).book_seats("hf", "33", "ay0")
hall3=Hall(1,2,3).view_show_list()

showreplica()
a=input("Enter option : ")
if(a=="1"):
    hall3 = Hall(1, 2, 3).view_show_list()
elif(a=="2"):
    b=input("Enter show id :")
    if(b=="ay0"):
        print(f"Movie name : Aynabazi                      Time : 12 ta")
        print("X for already booked seats")
    elif(b=="sk0"):
        print(f"Movie name : Skyfall                       Time : 12 ta")
        print("X for already booked seats")
    print("------------------------------------------------------------------------------")
    hall3 = Hall(1, 2, 3).view_available_seats(b)
    print()
    print("------------------------------------------------------------------------------")
elif(a=="3"):
    customer_name=input("Enter customer name : ")
    phone_no=input("Enter phone no : ")
    len_phone=len(phone_no)
    show_id=input("Enter show id : ")
    no_of_ticket=int(input("No of ticket : "))
    seat_list = []
    for i in range(no_of_ticket):
        seat_no=input("Seat no : ")
        seat_list.append(seat_no)

    print("Ticket booked successfully")
    print("------------------------------------------------------------------------------")
    print("customer name : " + customer_name)
    print("Phone number : " + phone_no[0] + phone_no[1] + (len_phone-2)*("*"))
    if (show_id == "ay0"):
        print(f"Movie name : Aynabazi                      Time : 12 ta")
    elif (show_id == "sk0"):
        print(f"Movie name : Skyfall                       Time : 12 ta")
    print("Tickets : ",end="")
    for i in range(no_of_ticket):
        print(seat_list[i],end=" ")
    print()
    print("Hall : A10")
    print("------------------------------------------------------------------------------")