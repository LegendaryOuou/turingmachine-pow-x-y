class Controller:
    def __init__(self):
        self.rules = self.init_rules('rule.txt')

    def init_rules(self, path):
        rules = []
        with open(path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                # print(line)
                line = line.strip('\n')
                head, tail = line.split('->')
                head = head[1:][:-1]
                tail = tail[1:][:-1]
                head = head.split(',')
                tail = tail.split(',')
                rules.append({'status': head[0], 'input': head[1],
                              'next_step': {'replace': tail[0], 'direction': tail[1], 'status': tail[2]}})
        return rules

    def add_ch_to_paper_tape(self,paper_tape):
        return paper_tape+'b'*10

    def modify_ch(self, string, position, ch):
        new = []
        for s in string:
            new.append(s)
        new[position] = ch
        return ''.join(new)

    def pointer(self, paper_tape, start_status, start_char):
        current_status = start_status
        current_char = start_char
        current_index = 0
        while True:
            try:
                paper_tape[current_index+1]
            except IndexError:
                paper_tape = self.add_ch_to_paper_tape(paper_tape)

            next_step = None
            for rule in self.rules:
                if rule['status'] == current_status and rule['input'] == current_char:
                    next_step = rule['next_step']

            paper_tape = self.modify_ch(paper_tape, current_index, next_step['replace'])
            if next_step['direction'] == 'R':
                current_index += 1
            elif next_step['direction'] == 'L':
                current_index -= 1
            else:
                pass

            current_status = next_step['status']

            current_char = paper_tape[current_index]
            if current_status == 'qend1' or current_status == 'qend2':
                break
        return paper_tape
