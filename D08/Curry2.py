#admin可以得到指定的100元
#hacker因為登入失敗,只可以得到0元
def login(username):
    def loginPass(money):
        return 100 if money > 100 else money
    def loginFail(money):
        return 0
    return loginPass if username == 'admin' else loginFail
print(login('admin')(100))
print(login('hacker')(100))