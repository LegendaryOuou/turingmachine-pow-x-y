from controller import Controller
import time


class TuringMaching:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.control = Controller()
        self.start_status = 'q0'
        self.start_char = 'b'

    def init_papertape(self, x, y):
        paper_tape = "bb"
        for i in range(y):
            paper_tape += '1'
        paper_tape += '0'
        for i in range(x):
            paper_tape += '1'
        paper_tape += 'bb'
        return paper_tape

    def count_1(self, paper_tape):
        return len(paper_tape.replace('b', '').replace('0', ''))

    def main(self):
        paper_tape = self.init_papertape(self.x, self.y)
        t1 = time.time()
        paper_tape = self.control.pointer(paper_tape,self.start_status,self.start_char)
        t2=time.time()
        result = self.count_1(paper_tape)
        print(str(self.x)+'的'+str(self.y)+'次方的结果是:',result)
        print("用时：", t2-t1, 's.')


if __name__ == '__main__':
    print("程序实现了f(x)=x^y(x>=0,y>=0).")
    x = input("请输入x:")
    y = input("请输入y:")
    turing = TuringMaching(int(x),int(y))
    turing.main()
