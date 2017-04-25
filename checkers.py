from tkinter import *
import math
import red_utility


# ******************* variables  **********************************************
# game board
square_size = 50
light_square_color = "khaki2"
dark_square_color = "green4"
piece_dist = 50


initial_board_list = [0, 3, 0, 3, 0, 3, 0, 3,
                      3, 0, 3, 0, 3, 0, 3, 0,
                      0, 3, 0, 3, 0, 3, 0, 3,
                      1, 0, 1, 0, 1, 0, 1, 0,
                      0, 1, 0, 1, 0, 1, 0, 1,
                      2, 0, 2, 0, 2, 0, 2, 0,
                      0, 2, 0, 2, 0, 2, 0, 2,
                      2, 0, 2, 0, 2, 0, 2, 0]


# *****************************************************************************

# ******************* utility functions ***************************************


def draw_board(self):
    for i in range(8):
        for j in range(8):

            # create the tan squares
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                x0 = j * square_size + 40
                y0 = i * square_size + 40
                x1 = j * square_size + 90
                y1 = i * square_size + 90
                self.canvas.create_rectangle(x0, y0, x1, y1,
                                             outline=light_square_color,
                                             fill=light_square_color,
                                             tags="khaki2")

            # create the green squares
            else:
                x0 = j * square_size + 40
                y0 = i * square_size + 40
                x1 = j * square_size + 90
                y1 = i * square_size + 90
                self.canvas.create_rectangle(x0, y0, x1, y1,
                                             outline=dark_square_color,
                                             fill=dark_square_color,
                                             tags="green4")


def draw_red_pieces(self):
    for i in range(3):
        for j in range(8):

            if (i % 2 == 0 and j % 2 == 1) or (
                                i % 2 == 1 and j % 2 == 0):
                x0 = j * piece_dist + 50
                y0 = i * piece_dist + 50
                x1 = j * piece_dist + 80
                y1 = i * piece_dist + 80
                self.canvas.create_oval(x0, y0, x1, y1, outline="red",
                                        fill="red",
                                        tags=("piece", "red"))


def draw_white_pieces(self):
    for i in range(5, 8):
        for j in range(8):

            # create the tan squares
            if (i % 2 == 0 and j % 2 == 1) or (
                                i % 2 == 1 and j % 2 == 0):
                x0 = j * piece_dist + 50
                y0 = i * piece_dist + 50
                x1 = j * piece_dist + 80
                y1 = i * piece_dist + 80
                self.canvas.create_oval(x0, y0, x1, y1, outline="white",
                                        fill="white", tags=("piece", "white"))


def get_piece_center(coords):
    # input list of coords [x1, y1, x2, y2]
    # returns an x,y that approximates the center of the piece

    x_center = (coords[2] + coords[0])/2
    y_center = (coords[3] + coords[1])/2

    return x_center, y_center


def get_row_or_col(x_or_y_board_position):

    if 40 < x_or_y_board_position <= 90:
        return 0
    elif 90 < x_or_y_board_position <= 140:
        return 1
    elif 140 < x_or_y_board_position <= 190:
        return 2
    elif 190 < x_or_y_board_position <= 240:
        return 3
    elif 240 < x_or_y_board_position <= 290:
        return 4
    elif 290 < x_or_y_board_position <= 340:
        return 5
    elif 340 < x_or_y_board_position <= 390:
        return 6
    elif 390 < x_or_y_board_position <= 440:
        return 7


def reshape_list(original_list):
    # assumes original_list is a perfect square length (e.g. 9 or 16)
    i = 0
    new_list = []
    while i < len(original_list):
        new_list.append(original_list[i:i+int(math.sqrt(len(original_list)))])
        i += int(math.sqrt(len(original_list)))
    return new_list


def unravel_board_array(board_array):
    board_state_list = []
    for row in range(len(board_array[0])):
        for col in range(len(board_array[0])):
            board_state_square = board_array[row][col]
            board_state_list.append(board_state_square)

    return board_state_list

def get_coords_from_row_col(row,col, piece_dist=50):
    x0 = col * piece_dist + 50
    y0 = row * piece_dist + 50
    x1 = col * piece_dist + 80
    y1 = row * piece_dist + 80

    return x0,y0,x1,y1


def draw_pieces_from_list(self, board_state_list):

    # convert list to array
    board_state_array = reshape_list(board_state_list)

    # draw pieces for each square for the following state codes
        # 0 : empty illegal
        # 1 : empty legal
        # 2: white man
        # 3: red man
        # 4: white crown
        # 5: red crown

        # NOTE: states 0 and 1 require no action

    for row in range(8):
        for col in range(8):

            state = board_state_array[row][col]

            x0, y0, x1, y1 = get_coords_from_row_col(row,col)

            if state == 2:
                self.canvas.create_oval(x0,y0,x1,y1,
                                        outline="white",
                                        fill="white",
                                        tags=("piece", "white"))

            elif state == 3:
                self.canvas.create_oval(x0,y0,x1,y1,
                                        outline="red",
                                        fill="red",
                                        tags=("piece", "red"))

            elif state == 4:
                self.canvas.create_oval(x0,y0,x1,y1,
                                        outline="white",
                                        fill="gold",
                                        tags=("piece", "white", "crowned"))

            elif state == 5:
                self.canvas.create_oval(x0,y0,x1,y1,
                                        outline="red",
                                        fill="MediumOrchid3",
                                        tags=("piece", "red", "crowned"))


def reset_game():

    # draw the board
    draw_board(self)
    # draw red pieces
    draw_red_pieces(self)
    # draw white pieces
    draw_white_pieces(self)
    # reset captured counters
    self.red_captured = 0
    self.white_captured = 0

    # reset current player
    self.current_ply = "Player 1 (red)"

    # reset drag/init_data
    drag_data = {"x": 0, "y": 0, "coords": None, "tags": None, "item": None}
    init_data = {"x": 0, "y": 0, "coords": None, "tags": None, "item": None}

# *****************************************************************************


class App():

    def __init__(self, master, width=480, height=480, root_bg = "grey67",can_bg='gray53'):

        # set size and parameters for the main app window
        master.configure(background=root_bg)
        master.geometry("1200x530")
        master.resizable(0, 0)
        master.title("Checkers")

        drag_data = {"x": 0, "y": 0, "coords": None, "tags": None, "item": None}
        init_data = {"x": 0, "y": 0, "coords": None, "tags": None, "item": None}

        self.legal_move =BooleanVar()
        self.legal_move = False

        self.red_captured = IntVar()
        self.red_captured = 12

        self.white_captured = IntVar()
        self.white_captured = 12

        self.red_crowns = IntVar()
        self.white_crowns = IntVar()

        self.red_moves = IntVar()
        self.red_moves = 0

        self.white_moves = IntVar()
        self.white_moves = 0

        self.current_ply = StringVar()
        self.current_ply = "Player 1 (white)"

        # labels (i.e. text boxes) reporting game stats

        # red captured label
        self.red_cap_label = Label(master)
        self.red_cap_label.configure(background=root_bg)
        self.red_cap_label["text"] = "Number of red pieces remaining: "+str(self.red_captured)
        self.red_cap_label.place(x=540, y=40)

        # white captured label
        self.white_cap_label = Label(master)
        self.white_cap_label.configure(background=root_bg)
        self.white_cap_label["text"] = "Number of white pieces remaining:"+str(self.white_captured)
        self.white_cap_label.place(x=840, y=40)

        # red crowns label
        #self.red_crowns_label = Label(master)
        #self.red_crowns_label.configure(background=root_bg)
        #self.red_crowns_label["text"] = "Number of red crowns:"
        #self.red_crowns_label.place(x=540, y=90)

        # white crowns label
        #self.white_crowns_label = Label(master)
        #self.white_crowns_label.configure(background=root_bg)
        #self.white_crowns_label["text"] = "Number of white crowns:"
        #self.white_crowns_label.place(x=840, y=90)

        # current player label
        self.current_ply_label = Label(master)
        self.current_ply_label.configure(background=root_bg)
        self.current_ply_label["text"] = "Current player: " + self.current_ply
        self.current_ply_label.place(x=690, y=140)

        frame = Frame(master)
        frame.pack()

        self.canvas = Canvas(master, width=width, height=height, bg=can_bg)
        self.canvas.pack(side=LEFT)

        # button: quit the game
        self.quit = Button(master, text='Quit!', command=master.quit)
        self.quit.configure(bg=root_bg)
        self.quit.place(x=540, y=480)

        # button: reset the game
        self.new_game = Button(master, text='Start New Game', command=lambda: reset_game)
        self.new_game.configure(bg=root_bg)
        self.new_game.place(x=600, y=480)

        # simulation parameters

        # Entry Label: enter the number of game simulations
        self.num_sims = Entry(master, text='Start Simulation')
        self.num_sims.configure(bg='white')
        self.num_sims.insert(10, "10")
        self.num_sims.place(x=840, y=440)

        # button: start a simulation (AI vs. AI)
        def sim_start():
            print(self.num_sims.get())
        self.start_sim = Button(master,
                                text='Start Simulation',
                                command=sim_start)
        self.start_sim.configure(bg=root_bg)
        self.start_sim.place(x=840, y=480)

        #
        ply_type = ['Human', 'MiniMax AI']

        # picker red: select human or AI player (default: human)
        self.pick_red_ply_type = Listbox(master, selectmode=SINGLE)
        self.pick_red_ply_type.place(x=540, y=340)
        self.pick_red_ply_type.configure(height=2)
        for item in ply_type:
            self.pick_red_ply_type.insert(END, item)

        # picker white: select human or AI player (default: human)
        self.pick_white_ply_type = Listbox(master, selectmode=SINGLE)
        self.pick_white_ply_type.place(x=840, y=340)
        self.pick_white_ply_type.configure(height=2)
        for item in ply_type:
            self.pick_white_ply_type.insert(END, item)


        # create the game board
        draw_board(self)

        # create game pieces centered in the rectangles
        #draw_red_pieces(self)

        #draw_white_pieces(self)

        # create pieces from initial board list



        draw_pieces_from_list(self, initial_board_list)

        # ********** utility functions ****************************************

        def increment_red_counter():
            self.red_captured += 1
            self.red_cap_label.config(text="Number of red pieces remaining: "+str(self.red_captured))

        def increment_white_counter():
            self.white_captured += 1
            self.white_cap_label.config(text="Number of white pieces remaining: "+str(self.white_captured))

        def get_jump_target_info():
            # identify piece jumped
            x_location_jumped = init_data["x"] + (drag_data["x"] - init_data[
                "x"]) / 2.0
            y_location_jumped = init_data["y"] + (drag_data["y"] - init_data[
                "y"]) / 2.0

            jumped_item = \
                self.canvas.find_closest(x_location_jumped, y_location_jumped)[0]

            jumped_item_tags = self.canvas.gettags(jumped_item)

            return x_location_jumped, y_location_jumped, jumped_item_tags, jumped_item

        def delete_pieces():
            # deletes all the pieces on the board
            # currently assigned to a button, but this will be part of the
            # board update function

            list_pieces_to_delete = self.canvas.find_withtag("piece")
            for piece in list_pieces_to_delete:
                self.canvas.delete(piece)

        def draw_pieces_from_list_button():


            board_state_list = [0, 3, 0, 3, 0, 3, 0, 3,
                                  3, 0, 3, 0, 3, 0, 3, 0,
                                  0, 3, 0, 3, 0, 3, 0, 3,
                                  1, 0, 1, 0, 1, 0, 1, 0,
                                  0, 1, 0, 1, 0, 1, 0, 1,
                                  2, 0, 2, 0, 2, 0, 2, 0,
                                  0, 2, 0, 2, 0, 2, 0, 2,
                                  2, 0, 2, 0, 2, 0, 2, 0]


            # convert list to array
            board_state_array = reshape_list(board_state_list)

            # draw pieces for each square for the following state codes
            # 0 : empty illegal
            # 1 : empty legal
            # 2: white man
            # 3: red man
            # 4: white crown
            # 5: red crown

            # NOTE: states 0 and 1 require no action

            for row in range(8):
                for col in range(8):

                    state = board_state_array[row][col]

                    x0, y0, x1, y1 = get_coords_from_row_col(row, col)

                    if state == 2:
                        self.canvas.create_oval(x0, y0, x1, y1,
                                                outline="white",
                                                fill="white",
                                                tags=("piece", "white"))

                    elif state == 3:
                        self.canvas.create_oval(x0, y0, x1, y1,
                                                outline="red",
                                                fill="red",
                                                tags=("piece", "red"))

                    elif state == 4:
                        self.canvas.create_oval(x0, y0, x1, y1,
                                                outline="white",
                                                fill="white",
                                                tags=("piece", "white",
                                                      "crowned"))

                    elif state == 5:
                        self.canvas.create_oval(x0, y0, x1, y1,
                                                outline="red",
                                                fill="red",
                                                tags=(
                                            "piece", "red", "crowned"))

        def create_baseline_board():
            _board_list = [None for _ in range(64)]

            init_array = reshape_list(_board_list)

            for row in range(8):
                for col in range(8):
                    if (row % 2 == 0 and col % 2 == 0) or (
                                row % 2 == 1 and col % 2 == 1):
                        init_array[row][col] = 0
                    else:
                        init_array[row][col] = 1

            return init_array

        def get_board_state_array():
            # gets the state of every piece on the board
            # returns it as a array/list to be passed to AI

            _board_state_array = create_baseline_board()

            #print("board: {}".format(_board_state_array))

            _list_of_pieces = self.canvas.find_withtag("piece")

            #print("piece list: {}".format(_list_of_pieces))

            for piece in _list_of_pieces:

                _coords = self.canvas.coords(piece)
                #print("coords: {}".format(_coords))

                _x_center, _y_center = get_piece_center(_coords)
                #print("center(x,y): {}, {}".format(_x_center, _y_center))

                _row = get_row_or_col(_y_center)
                _col = get_row_or_col(_x_center)

                #print("(r,c): {}, {}".format(_row, _col))

                _tags = self.canvas.gettags(piece)
                #print("tags: {}".format(_tags))

                if "red" in _tags and "crowned" not in _tags:
                    _code = 3

                elif "white" in _tags and "crowned" not in _tags:
                    _code = 2

                elif "red" in _tags and "crowned" in _tags:
                    _code = 5

                elif "white" in _tags and "crowned" in _tags:
                    _code = 4

                #print("code: {}".format(_code))

                _board_state_array[_row][_col] = _code

            #print(_board_state_array)

            return _board_state_array

        def print_piece_attributes():

            list_of_pieces = self.canvas.find_withtag("piece")

            for piece in list_of_pieces:
                _coords = self.canvas.coords(piece)
                _x_center, _y_center = get_piece_center(_coords)

                _row = get_row_or_col(_y_center)
                _col = get_row_or_col(_x_center)

                _tags = self.canvas.gettags(piece)

                print("coords: {}".format(_coords))
                print("x_center: {}".format(_x_center))
                print("y_center: {}".format(_y_center))
                print("row: {}".format(_row))
                print("col: {}".format(_col))
                print("tags: {}".format(_tags))

                if "red" in _tags and "crowned" not in _tags:
                    print("code: {}".format("3"))

                elif "white" in _tags and "crowned" not in _tags:
                    print("code: {}".format("2"))

                elif "red" in _tags and "crowned" in _tags:
                    print("code: {}".format("5"))

                elif "red" in _tags and "crowned" in _tags:
                    print("code: {}".format("4"))

        def end_human_ply_turn():

            # pass turn to red
            change_current_player()

            # get current board state
            _board_state_array = get_board_state_array()
            print("board after white move: {}".format(_board_state_array))

            # change to list
            _board_state_list = unravel_board_array(_board_state_array)
            print("brd 2 list: {}".format(_board_state_list))

            # send to AI, get updated board state
            _new_board_state = red_utility.minimax(_board_state_list)

            if _new_board_state != []:

                print("new board: {}".format(reshape_list(_new_board_state)))

                # delete pieces
                delete_pieces()

                # redraw pieces
                draw_pieces_from_list(self, _new_board_state)



                # change player state back to human
                change_current_player()

                # update ply indicator variables

                self.red_captured = red_utility.number_of_pieces(_new_board_state)[1]

                self.white_captured = red_utility.number_of_pieces((_new_board_state))[0]

                # update the scores
                self.red_cap_label.config(text="Number of red pieces captured: " + str(self.red_captured))
                self.white_cap_label.config(text="Number of white pieces captured: " + str(self.white_captured))

                _new_board_state = None



        # ********** functions that check whether a move is legal *************
        def check_if_turn(piece_tags):
            # returns True (if turn) False o.w.

            # get the color of the player
            if self.current_ply == "Player 1 (red)":
                _color = "red"
            else:
                _color = "white"

            # compare to the color of the player
            if _color in piece_tags:
                return True
            else:
                return False

        def check_piece_direction(y, piece_tags):

            # if color=="red" and crowned==False:
            _crowned = False

            if "red" in piece_tags:
                _color = "red"
            else:
                _color = "white"

            if "crowned" in piece_tags:
                _crowned = True

            if _color == "red" and _crowned == False and init_data["y"] > y:
                return False

            elif _color == "white" and _crowned == False and init_data["y"] < y:
                return False

            elif _crowned:
                return True

            else:
                return True

        def check_outside_gameboard(x, y):
            if x < 40 or x > 440 or y < 40 or y > 440:
                return False
            else:
                return True

        def check_if_square_permitted():
            # returns True of square is permitted
            # get tuple of ObjectIDs of all objects below game piece
            _item_below = self.canvas.find_overlapping(drag_data["x"],
                                           drag_data["y"],
                                           drag_data["x"]+30,
                                           drag_data["y"]+30)

            # get tags of item below and check if green
            for items in _item_below:
                if "green4" in self.canvas.gettags(items):
                    return True
                else:
                    return False

        def check_if_square_empty():
            # returns True if square is empty
            _piece_counter = 0
            # get tuple of ObjectIDs of all objects below game piece
            _item_below = self.canvas.find_overlapping(drag_data["x"],
                                           drag_data["y"],
                                           drag_data["x"]+30,
                                           drag_data["y"]+30)

            # get tags of item below and check if empty
            for items in _item_below:
                if "piece" in self.canvas.gettags(items):
                    _piece_counter += 1

            if _piece_counter == 1:
                return True

        def should_get_crown(y, piece_tags):

            if "white" in piece_tags:
                _color = "white"
            else:
                _color = "red"

            if "crowned" in piece_tags:
                _crowned = True

            else:
                _crowned = False

            if _color == "white" and y < 90 and _crowned is not True:
                print("White should get a crown")
                return True

            elif _color == "red" and y > 390 and _crowned is not True:
                print("Red should get a crown")
                return True

            else:
                return False

        def crown(obj, piece_tags):

            if "red" in piece_tags:
                _color = "red"

            else:
                _color = "white"

            if _color == "red":
                self.canvas.itemconfig(obj, fill="MediumOrchid3")
                self.canvas.addtag_withtag(newtag="crowned", tagOrId="current")

            elif _color == "white":
                self.canvas.itemconfig(obj, fill="gold")
                self.canvas.addtag_withtag(newtag="crowned", tagOrId="current")

        def check_max_movement_distance():
            _abs_x_delta = abs(drag_data["x"] - init_data["x"])
            _abs_y_delta = abs(drag_data["y"] - init_data["y"])

            if _abs_x_delta < 150 and _abs_y_delta < 150:
                return True
            else:
                return False

        def check_required_jump_condition():

            #check current player

            #for piece in pieces
                # if crowned, check whether 4 jump position are allowed
                    # if move allowed, check whether opponent piece can be jumped
                        # if yes, tag piece as "must jump"
                # if not crowned, check whether 2 jump positions are allowed
                    # if move allowed, check whether opponent piece can be jumped
                        # if yes, tag piece as "must jump"

                # check if any pieces tagged "must jump"
                    # if yes, check whether this piece has tag "must jump"
                        # if yes, condition met
                        # if no, condition not met
                    # if no, condition globally met, this restrics no pieces

                # check whether opponent in

            pass

        def check_legality_of_jump(piece_tags):
            x, y, tags, jumped_item = get_jump_target_info()

            if (("red" in piece_tags and "red" in tags) or
                    ("white" in piece_tags and "white" in tags)):
                return False

            if (abs(drag_data["x"] - init_data["x"]) > 70 and
                abs(drag_data["y"] - init_data["y"]) > 70 and 'piece' in tags):

                return True

            if (abs(drag_data["x"] - init_data["x"]) < 70 and
                abs(drag_data["y"] - init_data["y"]) < 70):
                return True

            else:
                return False

        def jump_and_capture():
            # comes after conditions check, so no need to check piece color

            x, y, tags, jumped_item = get_jump_target_info()

            if "piece" in tags:
                #if "red" in tags:
                #    increment_red_counter()
                #else:
                #    increment_white_counter()

                self.canvas.delete(jumped_item)

            # increment the right counter

        # ********** Mouse Event Handling ***************
        def on_button_press(event):
            # record the item and its location
            drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
            drag_data["coords"] = self.canvas.coords(drag_data["item"])
            drag_data["tags"] = self.canvas.gettags(drag_data["item"])
            drag_data["x"] = event.x
            drag_data["y"] = event.y
            init_data["x"] = event.x
            init_data["y"] = event.y
            self.legal_move = False

            #print("clicked at: {}, {}".format(drag_data["x"], drag_data["y"]))
            #print("coords: {}".format(drag_data["coords"]))
            #print("item: {}".format(drag_data["tags"]))

        def on_piece_click_and_drag(event):
            # print("released at: {}, {}".format(event.x, event.y))
            # compute how much this object has moved
            delta_x = event.x - drag_data["x"]
            delta_y = event.y - drag_data["y"]

            # move the object the appropriate amount
            self.canvas.move(drag_data["item"], delta_x, delta_y)

            # record the new position
            drag_data["x"] = event.x
            drag_data["y"] = event.y

        def on_button_release(event):

            # ALL of the following conditions must be met
            is_turn = check_if_turn(drag_data["tags"])

            is_allowed_direction = check_piece_direction(drag_data["y"],
                                                         drag_data["tags"])

            is_on_board = check_outside_gameboard(drag_data["x"],
                                                  drag_data["y"])

            is_allowed_space = check_if_square_permitted()

            is_empty = check_if_square_empty()

            #required_jump_condition_satisfied = check_required_jump_condition()

            if (is_turn and
                    is_allowed_direction and
                    is_on_board and
                    is_allowed_space and
                    check_legality_of_jump(drag_data["tags"]) and
                    check_max_movement_distance() and
                    # required_jump_condition_satisfied and
                    is_empty):

                self.legal_move = True

                jump_and_capture()

                # if crowned, add tag and change color
                if should_get_crown(drag_data["y"], drag_data["tags"]):
                    crown(drag_data["item"], drag_data["tags"])

            if not self.legal_move:
                total_delta_x = drag_data["x"] - init_data["x"]
                total_delta_y = drag_data["y"] - init_data["y"]
                # move the object the appropriate amount
                self.canvas.move(drag_data["item"], -total_delta_x, -total_delta_y)

            else:
                drag_data["item"] = None
                drag_data["coords"] = None
                drag_data["tags"] = None
                drag_data["x"] = 0
                drag_data["y"] = 0
                init_data["x"] = 0
                init_data["y"] = 0
                self.legal_move = False

        self.canvas.tag_bind(["piece"], "<ButtonPress-1>", on_button_press)
        self.canvas.tag_bind("piece", "<B1-Motion>", on_piece_click_and_drag)
        self.canvas.tag_bind("piece", "<ButtonRelease-1>", on_button_release)
        # self.canvas.pack(fill=BOTH, expand=1)

        # ***********************************************

        # ********** Experimental Section ***************
        # button: update the red captured counter

        def change_current_player():
            if self.current_ply == "Player 1 (white)":
                self.current_ply = "Player 2 (red)"
                self.current_ply_label.config(text="Current player: " + self.current_ply)

            elif self.current_ply == "Player 2 (red)":
                self.current_ply = "Player 1 (white)"
                self.current_ply_label.config(text="Current player: " + self.current_ply)

        # switch turn button
        self.test = Button(master, text='Switch Turn',
                           command=end_human_ply_turn)
        self.test.configure(bg=root_bg)
        self.test.place(x=1050, y=480)

        # delete all pieces button

        self.delete_pieces = Button(master, text='Delete All Pieces',
                           command=delete_pieces)
        self.delete_pieces.configure(bg=root_bg)
        self.delete_pieces.place(x=1050, y=450)

        # draw initial board state
        self.delete_pieces = Button(master, text='Draw initial boar',
                           command=draw_pieces_from_list_button)
        self.delete_pieces.configure(bg=root_bg)
        self.delete_pieces.place(x=1050, y=420)

        # print the board state (array)
        self.delete_pieces = Button(master, text='print brd state',
                           command=get_board_state_array)
        self.delete_pieces.configure(bg=root_bg)
        self.delete_pieces.place(x=1050, y=390)
        # ************************************************


def main():

    root = Tk()

    app = App(root)

    root.mainloop()
    root.destroy()

if __name__ == '__main__':
    main()

# 0 : empty illegal
#1 : empty legal

# 2: white man
# 3: red man
# 4: white crown
# 5: red crown