import sqlite3;
import re;

def regxforOther(ch):
    if ch == '.':
        return "[\\.]"
    if ch == '&':
        return "[&]"
    if ch == "-":
        return "[-]"


def rgxForAlphabetAndDigit(ch):
    if ch >= 'a' and ch <= 'z':
        return "[a-z]"

    elif ch >= 'A' and ch <= 'Z':
        return "[A-Z]"

    elif ch >= '0' and ch <= '9':
        return "[d]"
    return "None"


def patternGrouping(str):
    import re;
    import sqlite3
    set1 = set();
    for ch in str:
        rgx = rgxForAlphabetAndDigit(ch);
        if rgx is None:
            rgx = regxforOther(ch)
        set1.add(rgx);
    finalRxg = "";
    for rec in set1:
        if rec is not None:
            rec = rec.replace("[", "").replace("]", "")
            finalRxg = finalRxg + rec
    finalRxg = "[" + finalRxg + "]+";
    return "^" + finalRxg + "$";