from methods.template import Template
from numpy import count_nonzero

class NakedCandidates(Template):
    def __init__(self, board, notes):
        super().__init__(board, notes, "Naked Candidates")

    def solve(self):
        change = False
        for i in range(9):
            # check row
            change = self.check_section(self.notes[i]) or change

            # check column
            change = self.check_section(self.notes[:,i]) or change

            # check box
            change = self.check_section(self.notes[3*(i//3):3*(i//3)+3, 3*(i%3):3*(i%3)+3]) or change

        return self.board, self.notes, change

    def check_section(self, section):
        change = False
        note_dicts = dict() # set: [indices]
        for i in range(9):
            note_set = frozenset(list(section.reshape(9,9)[i].nonzero()[0]))
            if not (1 < len(note_set) and len(note_set) < 5):
                continue

            found_subsuperset = False
            for j in note_dicts.copy():
                if note_set.issubset(j): # subset or same
                    if i in note_dicts[j]:
                        continue
                    note_dicts[j].append(i)
                    if len(j) == len(note_dicts[j]):
                        change = self.remove_notes(section, j, note_dicts[j]) or change
                    if note_set == j: # same
                        note_dicts[note_set] = [i]
                    found_subsuperset = True

                elif note_set.issuperset(j): # superset
                    if i in note_dicts[j]:
                        continue
                    note_dicts[note_set] = note_dicts[j] + [i]
                    if len(note_set) == len(note_dicts[note_set]):
                        change = self.remove_notes(section, note_set, note_dicts[note_set]) or change
                    found_subsuperset = True

                elif note_set.intersection(j): # intersection
                    both = note_set.union(j)
                    if not (1 < len(both) and len(both) < 5):
                        continue
                    if i in note_dicts[j]:
                        continue
                    note_dicts[both] = note_dicts[j] + [i]
                    if len(both) == len(note_dicts[both]):
                        change = self.remove_notes(section, both, note_dicts[both]) or change

            if not found_subsuperset:
                note_dicts[note_set] = [i] # new
        return change

    def remove_notes(self, section, notes, indices):
        change = False
        for i in range(9):
            if i in indices:
                continue

            if count_nonzero(section.reshape(9,9)[:,list(notes)][i]) > 0:
                change = True

            if section.shape[0] > 3:
                section[i][list(notes)] = 0
            else:
                col, row = divmod(i, 3)
                section[col][row][list(notes)] = 0
        return change
