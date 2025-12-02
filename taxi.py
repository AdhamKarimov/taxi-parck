def kabisa(y):
    if y %400 ==0 :
        return True
    if y%100 !=0 and y%4 == 0:
        return True
    else:
        return False

def yil_kun(y):
    return 366 if kabisa(y) else 365

def kun_sana(k1, oy1, y1):
    kunlar = [31, 28,  31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if kabisa(y1):
        kunlar[1] = 29

    sum_kun = k1
    for i in range(oy1-1):
        sum_kun +=kunlar[i]
    return sum_kun

def sana(k, oy, y, k2, oy2, y2):
    if y == y2:
        kun_sum = kun_sana(k2, oy2, y2) - kun_sana(k, oy, y)
        return kun_sum


    kun1 = yil_kun(y) - kun_sana(k, oy, y)

    orasi = 0

    for y in range(y+1, y2):
        orasi +=yil_kun(y)

    kun2 = kun_sana(k2,oy2,y2)

    return kun1 + orasi + kun2

class User:
    def __init__(self, name, phone, seria, age):
        self.username = name
        self.phone = phone
        self.seria = seria
        self.age = age
        self.password = "0000"
        self.is_active = True
        self.is_admin = False
        self.balance=0

    def edit(self):
        field = input(' 1:username\n 2:phone \n 3:age: \n 4:password \n 5:balance:')
        new_field = input('new : ')
        if field == '1':
            self.username = new_field
        elif field == '2':
            self.phone = new_field
        elif field == '3':
            self.age = new_field
        elif field == '4':
            self.password =new_field
        elif field =="5":
            try:
                self.balance+=float(new_field)
                print(f"yangi balans:{self.balance}so'm")
            except:
                print("not'g'ri summa kiritdingiz")
    def view_balans(self):
        print(f"{self.username} balans: {self.balance}so'm")

u1 = User('user',12345,12345,54)

class Car:
    def __init__(self, model, brand, year, seria, narxi ):
        self.model = model
        self.brand = brand
        self.year = year
        self.seria = seria
        self.narxi=narxi
        self.is_active = True



class Order:
    def __init__(self, user_id, car_id, date_start, date_end):
        self.user_id = user_id
        self.car_id = car_id
        self.date_start = date_start
        self.date_end = date_end
        self.is_active = True
        self.status="kutilmoqda"

    def kun(self):
        k,oy,y=self.date_start
        k2,oy2,y2=self.date_end
        return sana(k,oy,y,k2,oy2,y2)

    def narxi_hisob(self,car):
        return self.kun()*float(car.narxi)

class Notification:
    def __init__(self,user,car,order):
        self.user=user
        self.car=car
        self.order=order
        self.status="kutilmoqda"


class Park:
    def __init__(self, title):
        self.title = title
        self.users = []
        self.cars = []
        self.orders = []
        self.notifications=[]
        self.balnce=0

    def public_cars(self):
        emty=[]
        count = 0
        for item in self.cars:
            if item.is_active:
                count += 1
                print(f'{count}. model: {item.model} brand:{item.brand}')
                emty.append(item)
        return emty
    def add_user(self):
        name =input('username:')
        phone =input('phone:')
        seria =input('seria:')
        age =input('age:')
        u = User(name,phone,seria,age)
        self.users.append(u)
    def view_users(self):
        count = 0
        for item in self.users:
            count+=1
            print(f"{count}. username: {item.username} phone:{item.phone} seria:{item.seria}")
    def add_car(self):
        model = input('modeli:')
        brand = input('brandi:')
        seria = input('seria:')
        year = input('yili:')
        narx=input("kunlik narxi:")
        u = Car(model, brand, year, seria,narx)
        self.cars.append(u)

    def view_cars(self):
        count = 0
        for item in self.cars:
            count += 1
            print(f"{count}. username: {item.model} phone:{item.brand} seria:{item.seria} yilu:{item.year} kunlik narxi:{item.narxi}")

    def login(self):
        name = input("username: ")
        password = input("password: ")
        count=0
        for item in self.users:
            count+=1
            if item.username == name and item.password == password:
                return item, True
            else:
                if count==len(self.users):
                    return 0,False


    def band_qilish(self,user:User):
        for i in self.orders:
            if i.user_id==user.username and i.is_active:
                print("sizga mashina berilgan")
                return
        bosh_mashina=self.public_cars()
        if not bosh_mashina:
            print("hozircha bo'sh mashina yo'q")
            return
        kod=int(input("mashina tartib raqamini kiriting"))
        tanlangan=bosh_mashina[kod-1]
        print("boshlnish sanasi")
        k = int(input("kun:"))
        oy = int(input("oy:"))
        y = int(input("yil:"))

        print("tugash sanasi")
        k2 = int(input("kun:"))
        oy2 = int(input("oy:"))
        y2 = int(input("yil:"))
        order=Order(user.username,tanlangan.seria,(k,oy,y),(k2,oy2,y2))
        self.orders.append(order)
        notification=Notification(user,tanlangan,order)
        self.notifications.append(notification)
        tanlangan.is_active=False
        print("mashina band qilish uchun ariza muvofaqiyatli topshirildi")


    def view_bildirishnoma(self):
        if not self.notifications:
            print("hozurcha hech qanday ariza yo'q")
            return
        print("----bildirishnomalar----")
        count=1
        for item in self.notifications:
            start=item.order.date_start
            end=item.order.date_end
            start_str=f"{start[0]}.{start[1]}.{start[2]}"
            end_str=f"{end[0]}.{end[1]}.{end[2]}"
            print(f"{count}.user:{item.user.username}|car:{item.car.model}|sana:{start_str}dan {end_str}|status:{item.status}")
            print("----------------------------------------------------------------------------")
            count+=1
        kod=int(input("qaysi bildirishnomani batafisil ko'rmoqchisiz(chiqish uchun 0 raqamini kiriting)"))
        if kod==0:
            return
        if kod<1 or kod>len(self.notifications):
            print("bunday bildirishnoma yo'q")
            return
        tanlov=self.notifications[kod-1]
        a=input("tasdiqlash uchun T,rad qilish uchun R kiriting:").upper()
        if a=="T":
            tanlov.status="tasdiqlangan"
            tanlov.order.is_active=True
            print(f"{tanlov.user.username}ning arzasi tasdiqlandi")
        elif a=="R":
            tanlov.status="rad etilgan"
            tanlov.order.is_active=False
            tanlov.car.is_active=True
            print(f"{tanlov.user.username}ning arizasi rad etildi")
        else:
            print("noto'g'ri tanlov")

    def view_my_ariza(self,user:User):
        my_ariza=[i for i in self.notifications if i.user==user]
        if not my_ariza:
            print("sizning arizalaringiz yo'q")
            return
        print("---sizning arizalaringiz---")
        count=1
        for item in my_ariza:
            start = item.order.date_start
            end = item.order.date_end
            start_str = f"{start[0]}.{start[1]}.{start[2]}"
            end_str = f"{end[0]}.{end[1]}.{end[2]}"
            print(
                f"{count}.user:{item.user.username}|car:{item.car.model}|sana:{start_str}dan {end_str}|status:{item.status}")
            print("----------------------------------------------------------------------------")
            count += 1

    def view_my_shartnoma(self,user:User):
        my_ariza=[i for i in self.notifications if i.user==user and i.status=="tasdiqlangan"]
        if not my_ariza:
            print("sizning shartnomangiz yo'q")
            return
        print("---sizning shartnomangiz---")
        count=1
        for item in my_ariza:
            start = item.order.date_start
            end = item.order.date_end
            start_str = f"{start[0]}.{start[1]}.{start[2]}"
            end_str = f"{end[0]}.{end[1]}.{end[2]}"
            print(
                f"{count}.user:{item.user.username}|car:{item.car.model}|sana:{start_str}dan {end_str}|status:{item.status}")
            print("----------------------------------------------------------------------------")
            count += 1

    def search(self,seria):
        for car in self.cars:
            if car.seria==seria:
                return car
        return None



    def car_qaytarish(self,user:User):
        for item in self.orders:
            if item.user_id==user.username and item.is_active:
                car=self.search(item.car_id)
                print(f"siz olgan mashina {car.model} {item.car_id}")
                kunlar = order.kun()
                summa = kunlar * float(car.narxi)
                print(f"mashinani qaytardingiz jami to'lov {summa}so'm")
                if user.balance>=summa:
                    user.balance-=summa
                    self.balnce+=summa
                    item.is_active=False
                    car.is_active=True
                    print(f"qolgan balans:{user.balance}so'm")
                else:
                    print("balansingiz yetmaydi iltimos hisobingizni to'ldiring")
                return
        print("sizda mashina yo'q")





park = Park('park1')
admin = User('admin', 123456, 1234, 12)
admin.is_admin = True
park.users.append(admin)
park.users.append(u1)

def taxi_manager(p:Park,u:User):
    while True:
        kod = input(" 1.edit \n 2.public cars \n 3.band qilish uchun ariza\n 4.arizalarim\n 5.mashinani qaytarish \n 6.shartnomani ko'rish \n 7.balans \n 8. break :")
        if kod=='1':
            u.edit()
        elif kod=='2':
            p.public_cars()
        elif kod=="3":
            p.band_qilish(u)
        elif kod=="4":
            p.view_my_ariza(u)
        elif kod=="5":
            p.car_qaytarish(u)
        elif kod=="6":
            p.view_my_shartnoma(u)
        elif kod=="7":
            print(f"sizning balansingiz{u.balance}so'm")
        elif kod=="8":
            park_manager(park)
        else :
            print("ko'rsatilganlaridan birini tanlang")

def admin_manager(p:Park,u:User):
    while True:
        kod = input(" 1. add user\n 2. add car \n 3. view users \n 4. views cars \n 5. bildirishnoma \n 6.bo'sh mashinalar\n 7.balance \n 8. break\n-> ")
        if kod=='1':
            p.add_user()
        elif kod=='2':
            p.add_car()
        elif kod=='3':
            p.view_users()
        elif kod=='4':
            p.view_cars()
        elif kod=="5":
            p.view_bildirishnoma()
        elif kod=="6":
            p.public_cars()
        elif kod=="7":
            print(f"kompanya {p.title} balansi:{p.balnce}so'm")
        elif kod =="8":
            park_manager(park)
        else:
            print("ko'rsatilganlaridan birini tanlang")

def park_manager(p: Park):
    while True:
        item = p.login()
        if item[1]:
            if item[0].is_admin:
                admin_manager(p,item[0])
            else:
                taxi_manager(p,item[0])
        else:
            print("login yoki parol  xato")

park_manager(park)
