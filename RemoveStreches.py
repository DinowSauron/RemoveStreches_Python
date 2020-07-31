def clearStrech(txt: str, Start: str, End=None):
    """
    :param txt: (str) Text to remove the strech
    :param Start: (str) Initial stretch of removal
    :param End: (str) Final strech of removal
    :return: (str) Text Processed

    Example to use:
    Your text is: txt = str(' "<Conserpts>": Text:Him rendered(or released) may attended concerns jennings reserved now')
    You just want the text, or you need to remove it: "<Conserpts>": Text:
    And you also don't want what's in brackets
    So call this method:
    txt = clearStreches(txt,' "<Con','Text:')
    txt = clearStreches(txt,'(',')')
    print(txt)
    # 'Him rendered may attended concerns jennings reserved now'
    now your text is clear of unwanted characters
    """
    # always included the space and add an extra parameter. Example: (-/+.!#%&*Âºª)
    IncludeParam = (" ,", " .", " :")

    if (End is None):
        End = str(Start)
    while txt.find(End) != -1:
        pri = txt.find(Start)
        seg = txt.find(End, pri + 1)
        if (pri == -1 or txt.find(Start) == txt.rfind(End)):
            break
        for param in IncludeParam:
            if (txt[seg + 1] in param and txt[pri - 1] in param[0]):
                try:
                    if (txt[seg + 1] in param[1]):
                        txt = txt[:pri - 1] + txt[seg + len(End):]
                        break
                    else:
                        if (txt[seg + 2] == param[0]):
                            seg += 1
                        txt = txt[:pri] + txt[seg + len(End) + 1:]
                        break
                except:
                    # necessary to pass to continue the for
                    pass
            if(param == IncludeParam[len(IncludeParam) - 1]):
                txt = txt[:pri] + txt[seg + len(End):]

    return txt


"""
# Example of use: remove the "" and execute the code
# from RemoveStreches import clearStrech  # utilize this in your code to import
txt = '<wiki>/<div>/<option:en-us>/MainText:Michael Joseph Jackson (August 29, 1958 – June 25, 2009) was an American ' \
      'singer (usa), and dancer. Dubbed the "King of Pop". Its awesome!'
print(txt)
txt = clearStrech(txt, "<wiki>", "MainText:")
txt = clearStrech(txt, "(", ")")
txt = clearStrech(txt, '"', '"')
print(txt)
"""


# Credits

"""
Any error that the code has / actions to add send an issue on github
GitHub: https://github.com/DinowSauron/RemoveStreches_Python/upload/master

Versions:
-clearStrech: 0.1.2



Creators:
-Luiz Claudio.
"""