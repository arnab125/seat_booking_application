
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

    def entry_show(self,id,movie_name,time):
        show_info = (str(id), str(movie_name), str(time))
        self.show_list.append(show_info)
        return self.show_list

    def book_seats(self,id_show,seat_no):
            self.seats = {"ay0": ["A0", "A1", "A2", "B0", "B1", "B2"], "sk0": ["A0", "A1", "A2", "B0", "B1", "B2"]}
            return self.seats


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
        bc=self.book_seats(idd,seat)
        # print(a)
        if (id == a[0][0]):
            for i in range(6):
                print(bc["ay0"][i],end="       ")
        elif (id == a[1][0]):
            for i in range(6):
                print(bc["sk0"][i], end="       ")

        #print(bc)


def showreplica():
    print("1.View all shows today")
    print("2.View available tickets")
    print("3.Book tickets")

a=Hall(1,2,3)
idd=input()
seat=input()
"""b=a.book_seats(idd,seat)
print(b)
c=a.entry_show("j","t","r")
print(c)

c=a.view_available_seats(idd)"""
m1=a.entry_show("ay0","aynabazi","12 ta")
m2=a.entry_show("sk0","skyfall","12 ta")
print(m1)
print(m2)

