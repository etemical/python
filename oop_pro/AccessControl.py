from Visitor import Guest, Employee
import sys

# 在控制台打印红色字体
def getredfont(msg):
    return "\033[31;0m" + msg + "\033[0m"

class DoorSystem:
    """
    初始化门禁系统的各个组件
    """
    def __init__(self):

        self.__door = Door()
        self.__input_device = InputDevice()
        self.__bell = DoorBell()
        self.__computer = Computer()

    def __operdoor(self):
        self.__door.open()
        self.__door.close()

    def work(self):
        while True:
            try:
                print("======================您好，欢迎来到X公司======================")
                id_type = int(self.__input_device.input_info("请选择您的身份信息：\n 1. 访客 \t 2. 员工 \n"))

                # 是访客的话
                if id_type == 1:
                    res = self.__guest_access()

                    if res == Constans.BELL_RING:
                        self.__operdoor()
                        return

                # 是员工的话
                elif id_type == 2:
                    count = 0
                    while count < 3:
                        res, t = self.__employee_access()
                        if res == Constans.BELL_RING:
                            self.__operdoor()
                            return
                        else:
                            com = self.__computer
                            if com.validate(t, res):
                                print("验证通过")
                                self.__operdoor()
                                return
                            else:
                                if count == 2:
                                    print(getredfont("信息输入错误，对不起，您的机会已经用完，再见！"))
                                    return
                                else:
                                    print(getredfont("输入错误，你还剩{}次机会，请重选择...".format(3-(count+1))))

                        count += 1
                else:
                    print(getredfont("您选择的选项不存在,请重新选择..."))

            except ValueError as e:
                print(getredfont("Error,请输入整数类型的选项"))
            except Exception as e :
                print(getredfont(e))

    #  来宾访问
    def __guest_access(self):
        while True:
            t = int(self.__input_device.input_info("请选择: 1.按门铃 \t 2.退出 \n"))
            g = Guest()
            if t == Constans.BELL_INPUT:
                 return g.press_bell(self.__bell)
            elif t == 2:
                sys.exit(0)
            else:
                print(getredfont("你选择的选项不窜在，请重新选择..."))



    # 是员工访问的话
    def __employee_access(self):
        while True:
            t = int(self.__input_device.input_info("请选择: 1.按门铃 \t 2.输密码 \t 3.输指纹 \t 4.退出 \n"))
            e = Employee()
            res = None  # 访问的结果
            if t == Constans.BELL_INPUT:
                res = e.press_bell(self.__bell)
            elif t == Constans.PASSWORD_INPUT:
                res = e.press_password(self.__input_device)
            elif t == Constans.FINGERPRINTS_INPUT:
                res = e.press_finger(self.__input_device)
            elif t == Constans.EXIT:
                sys.exit(0)
            else:
                print(getredfont("您输入的选项不存在，请重新输入!"))
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
    """
     初始化验证器
    """
    def __init__(self):

        self.__validator = Validator()

    """ 验证"""
    def validate(self,type,value):

        if type == Constans.PASSWORD_INPUT:
            self.__validator = PassWordValidator()

        elif type == Constans.FINGERPRINTS_INPUT:
            self.__validator = FingerPrintsValidator()

        return self.__validator(value)



class Validator:

    """
    验证基类
    """
    def __call__(self, *args, **kwargs):
        return self.validate(*args)

    def validate(self, args):
        pass

class PassWordValidator(Validator):
    """
    密码验证
    """
    def validate(self, pwd):
        return pwd in Constans.PASSWORD_LIST


class FingerPrintsValidator(Validator):
    """
    指纹验证
    """
    def validate(self, fig):
        return fig in Constans.FINGERPRINTS_LIST


class Constans:

    # 按门铃
    BELL_INPUT = 1

    #输入密码
    PASSWORD_INPUT = 2

    # 输入指纹
    FINGERPRINTS_INPUT = 3

    # 门铃响了
    BELL_RING = 5

    # 退出系统
    EXIT = 4

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

