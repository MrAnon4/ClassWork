from tkinter import Tk, Label, Entry, Button, RAISED, Text
from tkinter.messagebox import showinfo


# class creates Node objects
class ListNode():
    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt

# class stores the linked list and defines its head
class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0
        self.num_Icons = None
        self.round = 1

    # creates linked list according to size n, and then calls deletion function with size and k steps
    def playPotato(self, n, k):
        new_Node = None # node to be created during each iteration
        prev_Node = None # node from previous iteration
        size = 0    # keep track of total list size
        num_Icons = [] # list of all GUI number icons
        for i in range(n):
            if (not self.head):     # set up Linked List head (first iteration)
                new_Node = ListNode(i) # always zero
                label = Label(root, relief=RAISED, padx=10, text=i) # create a new player icon
                num_Icons.append(label) # add to array of icons
                label.grid(row=7, column=4+i) # place icon
                self.head = new_Node
                print(f"Head Created: {self.head.data}")
                prev_Node = self.head   # previous node automatically is head (since size is now 1)
                size +=1
                continue
            if (i + 1 == n): # Last Node to be added, which occurs right before i equals n size parameter
                new_Node = ListNode(i) # will be one less than n
                label = Label(root, relief=RAISED, padx=10, text=i)
                num_Icons.append(label)
                label.grid(row=7, column=4 + i)
                print(f"New Node Created: {new_Node.data}")
                prev_Node.nxt = new_Node  # previous node reference set to last node
                new_Node.nxt = self.head  # last node reference set to head, making the LL circular
                print(f"Final Link: Last Node {new_Node.data} connects to Head {self.head.data}")
                size += 1
                continue
            # every other iteration case (body nodes)
            new_Node = ListNode(i)
            label = Label(root, relief=RAISED, padx=10, text=i)
            num_Icons.append(label)
            label.grid(row=7, column=4 + i)
            print(f"New Node Created: {new_Node.data}")
            prev_Node.nxt = new_Node # previous node reference set to new node
            print(f"New Link: Node {prev_Node.data} connects to {new_Node.data}")
            prev_Node = new_Node
            size +=1 # size always increases with every addition to linked list regardless of node type

        self.size = size # total size of the linked list saved
        self.num_Icons = num_Icons # icon array saved to LL instance

    # helper function called when Eliminate Button is pressed
    def deleteNodeButton(self, steps, size, button):

        head = self.head # find head
        print("Eliminate Button Pressed")


        if (self.size == 1): # end condition: only one node left in linked list
            print("Winner Inbound")
            showinfo(message=f"Game Winner: {head.data - 1}") # Game Winner notification pop-up (accounts for position shift)
            self.num_Icons[0].after(0, self.num_Icons[0].destroy)   #  Remove the last two icons displayed in the game
            self.num_Icons[1].after(0, self.num_Icons[1].destroy)
            button.after(0, button.destroy)     # destroy Eliminate Button
            txt.delete(1.0, 12.0)   # clear text
            return print(f"Linked List Size: {self.size}; Game Winner: {head.data - 1}")  # print winner and account for position skip

        for i in range(steps-1): # go up until the last step
            print(f"Game Iteration: {i}")
            head = head.nxt # move onto next node
        cur_Node = head  # save the node just before deletion target
        nxt_head = head.nxt  # go the next node (to be deleted)
        after_Node = nxt_head.nxt  # the next node after the one to be deleted
        cur_Node.nxt = after_Node  # connect previous node to node after deletion target.

        print(f"Node Removed: {nxt_head.data}")  # Node is taken out of linked list instead of actually being deleted
        # for removing the applicable player icon
        for x in self.num_Icons: # iterate over the array of player icons for given instance
            if nxt_head.data-1 == x.cget("text"):  # icon label equals the data attribute of the deleted node
                x.after(0, x.destroy())     # destroy label
                self.num_Icons.remove(x)    # remove it from the list
                print(f"Icon Removed: {nxt_head.data}")
                txt.insert(2.0, f"Round: {self.round} Player {nxt_head.data-1} Eliminated!\n") # elimination pop-up in the game

        self.round += 1 # increase round count
        self.size -= 1  # reduce linked list size and reset count in prep for next "deletion"
        self.head = head # sets/changes starting position for next round

def startGame():
    global sizeEnt # this will be our n iA
    global stepEnt # this will be our k iA
    global txt
    n = int(sizeEnt.get()) # convert entry into n
    k = int(stepEnt.get()) # convert entry into k

    if (n <= 1 or n > 12):
        # if n condition net met, displays pop-up and kicks out of function (game doesn't start)
        showinfo(message="Please enter a list size between 1 and 12 such that 1<N<12")
        return
    if (k < 1):
        # if k condition net met, displays pop-up and kicks out of function (game doesn't start)
        showinfo(message="Please enter a step count such that K>=1")
        return

    LL1 = LinkedList()  # create new linked list instance
    LL1.playPotato(n, k) # build linked list according to size n

    button_Elim = Button(root, text="Eliminate", command= lambda: LL1.deleteNodeButton(k, n, button_Elim)) # display eliminate button (now active)
    button_Elim.grid(row=7, column=3) # place on grid

    # display entered n and k values
    txt.insert(1.0, f"Game Started: N = {n} K = {k} \n")


# checks the size (n) input before playing
def sizeInput():
    global sizeEnt # this will be our n iA
    n = int(sizeEnt.get())

    if (n <= 1 or n > 12):
        showinfo(message="Please enter a list size between 1 and 12 such that 1<N<12")

# checks the step (k) input before playing
def stepInput():
    global stepEnt # this will be our n iA
    k = int(stepEnt.get())

    if (k < 1):
        showinfo(message="Please enter a step count such that K>=1")

#root call
root = Tk()

#label
label = Label(master=root, text="Welcome to Hot Potato Game! Please Enter a List Number (n) and a Step Number (k)")
label.grid(row=0, column=3)

#Entry for n (size)
label_N = Label(root, text="n")
label_N.grid(row=3, column=1)
sizeEnt = Entry(root)
sizeEnt.grid(row=3, column=2)
button_N = Button(root, text="Check List Size", command= sizeInput) # check button
button_N.grid(row=3, column=3)

#Entry for k (step)
label_K = Label(root, text="k")
label_K.grid(row=4, column=1)
stepEnt = Entry(root)
stepEnt.grid(row=4, column=2)
button_K = Button(root, text="Check Game Step", command= stepInput) # check button
button_K.grid(row=4, column=3)

#start game
button_Start = Button(root, text="Start", command=startGame) # button that starts game
button_Start.grid(row=6, column=2) # placement

# text (displayed at bottom of window and is updated throughout the game
txt = Text(master=root, width=40, height=10) # set position and size
txt.grid(row=9, column=3) # place

root.title("MyStupidPotatoGame")
root.mainloop()


