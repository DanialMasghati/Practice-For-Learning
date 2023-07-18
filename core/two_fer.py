# def two_fer(name):
#     like_cookie = True
#     if name == "Do-yun" and like_cookie:
#         return (f"One for {name}, one for me.")
#     elif like_cookie:
#         return (f"One for {name}, one for me.")
#     else:
#         return "One for you, one for me."

def two_fer(name="you"):
    return f"One for {name}, one for me."


print(two_fer())
