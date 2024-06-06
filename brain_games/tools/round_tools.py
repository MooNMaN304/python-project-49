def beatiful_question(text):
    abs1 = ""
    for i in text:
        abs1 += str(i) + " "
    j = 0
    beatiful_result = ""
    while j <= len(abs1) - 1:
        if abs1[j] == "[":
            beatiful_result += ""
            j += 1
        if abs1[j] == "]":
            beatiful_result += ""
            j += 1
        if abs1[j] == "'":
            beatiful_result += ""
            j += 1
        else:
            beatiful_result += abs1[j]
            j += 1
    return beatiful_result


SIGNS = ["*", "-", "+"]
