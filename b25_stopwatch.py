import tkinter
import time


class Stopper:

    def __init__(self):
        self.counter = 0
        self.running = False

        self.root = tkinter.Tk()
        self.root.title('Stopwatch')

        self.root.minsize(width=250, height=70)

        self.box1 = tkinter.Label(self.root, fg='red', font='Verdana 30 bold')
        self.box1.pack()

        self.box2 = tkinter.Frame(self.root)
        self.start = tkinter.Button(self.box2, text='Start', width=6, command=self.Start)
        self.stop = tkinter.Button(self.box2, text='Stop', width=6, state='disabled', command=self.Stop)
        self.reset = tkinter.Button(self.box2, text='Reset', width=6, state='disabled', command=self.Reset)

        self.box2.pack(anchor='center', pady=5)
        self.start.pack(side='left')
        self.stop.pack(side='left')
        self.reset.pack(side='left')

        self.root.mainloop()

    def count(self):
        if self.running:
            self.box1['text'] = time.strftime('%H:%M:%S', time.gmtime(self.counter))
            self.counter += 1
            self.root.after(1000, self.count)

    def Start(self):
        self.running = True
        self.count()
        self.start['state'] = 'disabled'
        self.stop['state'] = 'normal'
        self.reset['state'] = 'normal'

    def Stop(self):
        self.running = False
        self.start['state'] = 'normal'
        self.stop['state'] = 'disabled'
        self.reset['state'] = 'normal'

    def Reset(self):
        self.running = True
        self.counter = 0


if __name__ == '__main__':
    Stopper()

# https://www.geeksforgeeks.org/create-stopwatch-using-python/