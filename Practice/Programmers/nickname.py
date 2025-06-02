def solution(nickname):
    answer = ""
    for letter in nickname:
        if letter == "l":
            answer += "I"
        elif letter == "w":
            answer += "vv"
        elif letter == "W":
            answer += "VV"
        elif letter == "O":
            answer += "0"
        else:
            answer += letter
    if len(answer) < 3:
        while len(answer) < 4 : answer += "o"
        # answer += "o"
    if len(answer) > 8:
        answer = answer[:8]
    return answer

if __name__ == "__main__" :
    answer = solution("WORLDworld")
    print(answer)
    
    answer = solution("VV0RLDvv")
    print(answer)