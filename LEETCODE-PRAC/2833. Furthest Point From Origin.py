class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        pos = 0
        blanks = 0
        for ch in moves:
            if ch == 'L':
                pos -= 1
            elif ch == 'R':
                pos += 1
            else:
                blanks += 1
        return abs(pos) + blanks
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        c = 0
        if moves.count("L") > moves.count("R"):
            moves = moves.replace("_","L")
        else:
            moves = moves.replace("_","R")
        return(abs(moves.count("R")-moves.count("L")))