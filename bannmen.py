import threading
import time
import random
import tkinter as tk
class Thread(threading.Thread):
    def __init__(self):
        super(Thread, self).__init__()
        self.is_running = True
        self.thlock = 1
        self.keylock = 0
        self.parent = None
        self.start()
    def __call__(self):
        self.keylock = 1
        self.unlock()
    def set_parent(self, parent):
        self.parent = parent
    def lock(self):
        self.thlock = 1
    def unlock(self):
        self.thlock = 0
    def is_lock(self):
        return self.thlock
    def random_choice(self):
        time.sleep(0.5)
        i = random.choice([i for i, v in enumerate(self.parent.board2info) if v == 0])
        tag = self.parent.alpstr[i]
        self.parent.update_board(i, tag)
        if self.parent.result:
            self.lock()
            return
        self.parent.playerTurn = 1
        self.lock()
        self.keylock = 0
    def alpha_zero(self):
        pass
    def run(self):
        while self.is_running:
            if self.is_lock():
                continue
            self.random_choice()
table = """
Turn {}
        |{:^3s}|{:^3s}|{:^3s}|
        -------------
        |{:^3s}|{:^3s}|{:^3s}|
        -------------
        |{:^3s}|{:^3s}|{:^3s}|
"""
table_r = """
        結果: {}
        |{:^3s}|{:^3s}|{:^3s}|
        -------------
        |{:^3s}|{:^3s}|{:^3s}|
        -------------
        |{:^3s}|{:^3s}|{:^3s}|
"""
def check(board):
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for i in range(len(wins)):
        if board[wins[i][0]]==board[wins[i][1]]==board[wins[i][2]]==1:
            return 1
        elif board[wins[i][0]]==board[wins[i][1]]==board[wins[i][2]]==-1:
            return 1
    return [2, 0][0 in board]
class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()
        # Window
        self.title("三目並べ")
        self.geometry("{}x{}+{}+{}".format(360, 400, 450, 100))
        # Set up some variables
        self.set_variables()
        # Set up game board
        self.set_board()
        # Set up some buttons
        self.set_button()
        # Set threading
        self.thread = Thread()
        self.thread.set_parent(self)
    def set_variables(self):
        self.result = 0
        self.playerTurn = 1
        self.board2info = [0] * 9
        self.symbol = " ox"
        self.alpstr = "abcdefghi"
        self.winner = ["", "あなた", "引き分け", "CPU"]
    def set_board(self):
        self.board = tk.Canvas(self, bg="white", width=340, height=340)
        self.tag2pos = {}
        position = [(20, 20, 120, 120), (120, 20, 220, 120), (220, 20, 320, 120),
                    (20, 120, 120, 220), (120, 120, 220, 220), (220, 120, 320, 220),
                    (20, 220, 120, 320), (120, 220, 220, 320), (220, 220, 320, 320)]
        for tag, pos in zip(self.alpstr, position):
            self.tag2pos[tag] = pos[:2]
            self.board.create_rectangle(*pos, fill='green yellow', outline='green yellow', tags=tag)
            self.board.tag_bind(tag, "<ButtonPress-1>", self.pressed)
        # Vertical line
        for x in range(120, 320, 100):
            self.board.create_line(x, 20, x, 320)
        # Horizontal line
        for y in range(120, 320, 100):
            self.board.create_line(20, y, 320, y)
        self.board.place(x=10, y=0)
    def set_button(self):
        self.reset = tk.Button(self, text="reset", relief="groove", command=self.clear)
        self.reset.place(x=170, y=360)
        self.quit_program = tk.Button(self, text="quit", relief="groove", command=self.close)
        self.quit_program.place(x=320, y=360)
    def clear(self):
        self.board.delete("all")
        self.set_variables()
        self.set_board()
        self.thread.keylock = 0
    def draw_symbol(self, tag):
        symbol = self.symbol[self.playerTurn]
        x, y = self.tag2pos[tag]
        self.board.create_text(x+50, y+50,
                               font=("Helvetica", 60),
                               text=symbol)
    def pressed(self, event):
        if self.thread.keylock:
            return
        item_id = self.board.find_closest(event.x, event.y)
        tag = self.board.gettags(item_id[0])[0]
        #print("Tag {} pressed...".format(tag))
        action = self.alpstr.index(tag)
        state = self.board2info[action]
        if state in [-1, 1]:
            return
        self.update_board(action, tag)
        if self.result:
            self.thread.keylock = 1
            return
        self.thread()
    def update_board(self, action, tag):
        self.board2info[action] = self.playerTurn
        self.draw_symbol(tag)
        self.check_result()
        self.playerTurn = -self.playerTurn
    def check_result(self):
        result = check(self.board2info)
        winner = "Turn {}".format("?")
        if result:
            winner = self.winner[result] if result == 2 else self.winner[self.playerTurn]
            print(table_r.format(winner, *[[" ", "o", "x"][i] for i in self.board2info]))
        else:
            print(table.format("?", *[[" ", "o", "x"][i] for i in self.board2info]))
        self.result = result
    def close(self):
        self.thread.is_running = 0
        self.quit()
    def run(self):
        self.mainloop()
if __name__ == "__main__":
    app = App()
    app.run()
    
