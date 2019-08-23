from Visitor import Guest, Employee
import sys

class DoorSystem:

    def __init__(self):
        self.__door = Door()
        self.__input_device = InputDevice()
        self.__bell = DoorBell()
        self.__computer = Computer()

    def __operdoor(self):
        self.__door.open()
        self.__door.close()

    def work(self):

        try:
            print("======================您好，欢迎来到X公司======================")
            id_type = self.__input_device.input_info("请选择您的身份信息：\n 1. 访客 \t 2. 员工 \n")

            # 是访客的话
            if int(id_type) == 1:
                res = self.__guest_access()

                if res == Constans.BELL_RING:
                    self.__operdoor()

            # 是员工的话
            if int(id_type) == 2:
                count = 0

                while count < 3:
                    res, t = self.__employee_access()
                    if res == Constans.BELL_RING:
                        self.__operdoor()
                        return
                    else:
                        com = Computer()
                        if com.validate(t, res):
                            print("验证通过")
                            self.__operdoor()
                            break
                        else:
                            if count == 2:
                                print("信息输入错误，对不起，您的机会已经用完，再见！")
                            else:
                                print("您的信息输入有误，请重新输入...")

                    count += 1
        except Exception as e:
            print("您的输入有误")


    # 隐藏私有方法
    def __guest_access(self):
        t = self.__input_device.input_info("请选择: 1.按门铃 \t 2.退出 \n")
        g = Guest()
        if int(t) == Constans.BELL_INPUT:
             return g.press_bell(self.__bell)
        else:
            sys.exit(0)



    # 是员工访问的话
    def __employee_access(self):
        while True:
            t = int(self.__input_device.input_info("请选择: 1.按门铃 \t 2.输密码 \t 3.输指纹 \t 4.退出 \n"))
            e = Employee()
            res = None
            if t == Constans.BELL_INPUT:
                res = e.press_bell(self.__bell)
            elif t == Constans.PASSWORD_INPUT:
                res = e.press_password(self.__input_device)
            elif t == Constans.FINGERPRINTS_INPUT:
                res = e.press_finger(self.__input_device)
            elif t == Constans.EXIT:
                sys.exit(0)
            else:
                print("您输入的选项不存在，请重新输入!")
                continue

            return res, t




class InputDevice:

    def input_info(self, msg:str):
        return input(msg)

    def input_password(self):
        return input("请输入密码:\n")

    def input_fingerprints(self):
        return input("请录入您的指纹:\n")


class Door:

    def open(self):
        print("门已打开，请进入...")

    def close(self):
        print("人已进入，门关闭了...")

class DoorBell:

    def ring(self):
        print("门铃响了")
        return Constans.BELL_RING

class Computer:

    def __init__(self):
        self.__validator = Validator()

    def validate(self,type,value):

        if type == Constans.PASSWORD_INPUT:
            self.__validator = PassWordValidator()

        elif type == Constans.FINGERPRINTS_INPUT:
            self.__validator = FingerPrintsValidator()

        return self.__validator.validate(value)


class Validator:
    def validate(self, args):
        pass

class PassWordValidator(Validator):

    def validate(self, pwd):
        return pwd in Constans.PASSWORD_LIST


class FingerPrintsValidator(Validator):

    def validate(self, fig):
        return fig in Constans.FINGERPRINTS_LIST


class Constans:

    BELL_INPUT = 1

    PASSWORD_INPUT = 2

    FINGERPRINTS_INPUT = 3

    BELL_RING = 5

    EXIT = 4

    ERROR_INPUT = 6

    PASSWORD_LIST = [
        "123456",
        "654321"
    ]

    FINGERPRINTS_LIST = [
        "fg12345",
        "fg13579"
    ]


if __name__ == '__main__':
    ds = DoorSystem()
    ds.work()

