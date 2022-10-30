class Star_Cinema:
    def __init__(self):
        self.hall_list = []

    def entry_hall(self, rows, cols, hall_no):
        new_hall = Hall(rows, cols, hall_no)
        self.hall_list.append(new_hall)
        #return self.hall_list


class Hall(Star_Cinema):

    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []
        super(Hall, self).__init__()

    def __repr__(self):
        return f"{self.rows} {self.cols} {self.hall_no}"

    def entry_show(self):
        movie1 = ("123", "A", "12ta")
        movie2 = ("3", "Ab", "12ta")
        self.show_list.append(movie1)
        self.show_list.append(movie2)
        self.seats = {movie1: [["a", "b", "c"], ["d", "e", "f"]], movie2: [["a", "b", "c"], ["d", "e", "f"]]}
        return self.show_list

    def book_seats(self,person_name, phone_no , id_show):
        person_name = input("name")
        phone_no = input("phone")
        id_show = input("id")
        print(self.show_list)
        if(id_show == self.show_list[0][0]):
            print(self.seats[0])
        else:
            print(self.seats[0])



hall = Star_Cinema()
hall.entry_hall(5, 8, 9)
hall.entry_hall(54, 88, 95)
print(hall.hall_list)
print(Hall(1, 2, 3).entry_show())
Hall(1,2,3).entry_show()
Hall(1,2,3).book_seats("a","15","123")
