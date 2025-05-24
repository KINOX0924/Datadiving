# 5월 10일 대체 강의
# 자판기 = 객체 지향으로 설계

# 상품/구매자 클래스
class Goods :
    def __init__(self) :
        self.name      = ""
        self.price     = 0
        self.inventory = 0
        self.payment   = 0
        self.change    = 0
        self.count     = 0
        self.confirm   = False
        # self.count   = 구매 이력을 확인 및 이력 리스트에 들어간 고객 정보를 대조하기 위함
    
    # 고객이 투입한 돈을 입력받는 함수
    def insertMoney(self) :
        self.payment = int(input("금액 투입 : "))
    
    # 고객이 상품을 선택했을 때 상품의 재고를 확인하는 함수
    # 재고가 없을 시 상품 구매 불가 >> 투입한 금액 그대로 다시 반환되어야 함
    def getInventory(self) :
        if self.inventory <= 0 :
            print("\n선택 상품 [품절] 로 구매 불가")
            print("투입된 금액은 반환됩니다.")
            self.chnChange()
            return
        self.calChange()
    
    # 고객이 상품을 선택하고 상품의 재고 , 투입한 금액이 정상적일 경우 잔돈을 계산하는 함수
    def calChange(self) :
        if self.payment < self.price :
            print("\n투입 금액 부족으로 구매 불가")
            print("투입된 금액은 반환됩니다.")
            self.chnChange()
            return
        self.getChange()
    
    # 구매에 성공했을 때 투입액에서 결제액을 제외하는 함수
    def getChange(self) :
        self.change = self.payment - self.price
    
    # 구매에 실패했을 때 투입액과 반환액을 교환하는 함수
    def chnChange(self) :
        self.payment , self.change = self.change , self.payment
    
    # 재고가 0 이거나 , 상품의 가격이 (투입액 + 반환액) 보다 크면 구매를 실패후 결제 확인 변수에 False 대입
    # 아니라면 상품 구매 성공이면 결제 확인 변수에 True
    # 결제 확인 변수를 사용하여 재고를 없앨 지 그대로 놔둘 지 결정
    def printTrade(self) :
        if self.inventory <= 0 or self.price > (self.payment + self.change) :
            print(f"[{self.name}] 상품 구매를 실패하었습니다.")
            self.confirm = False
        else : 
            print(f"[{self.name}] 상품을 구매하였습니다.")
            self.confirm = True
        print(f"상품 금액 : {self.price}" , end = "\t")
        print(f"지불 금액 : {self.payment}" , end = "\t")
        print(f"반환 금액 : {self.change}")
    
    # 구매 이력을 확인하는 것으로 이용자에게는 보여지지 않아야함 / 관리자 클래스가 생기면 거기에서만 사용할 수 있게
    # 현재는 디버깅 및 테스트를 위해 이용자 클래스에서 작동
    # 결제 확인 변수에 따라서 구매를 실패했는지 , 성공했는지만 확인 가능
    def printTradehistory(self) :
        print(f"상품명 : [{self.name}]" , end = "\t")
        print(f"수량 : [1]" , end = "\t")
        if self.confirm == False :
            print("구매 여부 : [실패]")
        else :
            print("구매 여부 : [성공]")



# 자판기 클래스
class Vendingmachine :
    # 세 개의 리스트를 사용 / 같은 인덱스로 상품명 , 가격 , 재고를 한번에 출력 및 선택할 수 있도록 함
    goods_list     = ["" ,"핫 아메리카노" , "아이스 아메리카노" , "핫 카페라떼" , "아이스 카페라떼"]
    price_list     = [0 , 1500 , 2000 , 2500 , 3000]
    inventory_list = [0 , 1 , 0 , 5 , 2]
    count          = 0
    
    def __init__(self) :
        self.history        = []
    # 상품과 금액 , 재고는 상품별로 같은 인덱스를 사용
    # 현재는 관리자 클래스가 별도로 없기에 상품을 추가 , 삭제 , 수정하는 함수가 없음
    # 엑셀 또는 CSV 파일을 사용하여 단숨에 넣는 것이 가능하도록 및 단독 수정도 가능하도록 추가 예정 - 관리자 클래스
    # 단 외부로 꺼내는 것은 아직 안됨
    # 현재는 디버깅을 위해서 초기화값만 넣어둔 상태
    
    # 자판기에서 판매하는 상품 목록을 출력
    # 일단 테스트로 두 개 상품만 출력하고 , 기능 확인 후 리스트로 상품 출력 개수 늘릴 예정
    # 재고가 '0' 이면 품절로 미리 표시 후 혹시라도 재고가 0 이하로 떨어지는 것을 방지하지 위해서 0 으로 초기화
    # 재고가 있다면 가격을 표시하여 구매가 가능함을 알림
    def printGoodslist(self) :
        print("====== 상품 목록 ======")
        for i in range(1,len(self.goods_list)) :
            if  self.inventory_list[i] <= 0 :
                print(f"[{i}] | [{self.goods_list[i]}] | [품절]")
                self.inventory_list[i] = 0
            else :
                print(f"[{i}] | [{self.goods_list[i]}] | 가격 : {self.price_list[i]} 원")
        print("====== 상품 목록 ======")
    
    # 구매할 상품의 번호를 입력 받음
    # 먼저 구매하려고 하는 상품의 번호를 확인하여 자판기에 있는 상품인지를 확인 / 없거나 0 을 누르면 리턴
    def selectGoods(self) :
        select_goods = int(input("구매할 상품 번호 입력 : "))
        
        if select_goods <= 0 or len(self.goods_list) < select_goods :
            print("상품을 잘못 선택하셨습니다.")
            return
        
        # count 를 이용하여 현재 구매 고객의 정보를 가져와서 히스토리와 대조
        # 구매시도를 한 상품명 , 가격 , 재고를 선택한 상품으로 수정 후 계산
        # printTrade() 에서 confirm 변수에 트루/펄스 값을 받는데 해당 변수 값을 사용하여 재고를 조정
        customer_list = self.history[self.count]
        for i , v in enumerate(self.history) :
            if v == customer_list :
                v.name      = self.goods_list[select_goods]
                v.price     = self.price_list[select_goods]
                v.inventory = self.inventory_list[select_goods]
                v.getInventory()
                v.printTrade()
                if v.confirm == True :
                    self.inventory_list[select_goods] -= 1
    
    # 구매 이력을 확인 - 관리자 클래스에서 볼 수 있게 넣을 예정
    def printHistory(self) :
        for customer in self.history :
            customer.printTradehistory()
    
    # 자판기 작동
    # 고객 = 상품 클래스를 생성함
    # 고객이 구매를 할지 , 안 할지 먼저 선택 후에 가장 먼저 금액을 투입 받음
    # 고객 카운트를 고객 객체에 대입
    # 구매 정보를 이력 리스트에 추가
    # 상품 목록 출력
    # 상품 선택 후 구매 성공/실패
    # 고객 카운트 상승
    def onVending(self) :
        customer = Goods()
        customer.insertMoney()
        customer.count = self.count
        self.history.append(customer)
        self.printGoodslist()
        self.selectGoods()
        self.count += 1
           
    # 자판기 메인 메뉴
    def printMenu(self) :
        print("====== 메인 메뉴 ======")
        print("[1] 상품 구매")
        print("[0] 구매 종료")
        print("====== 메인 메뉴 ======")
    
    # 자판기 작동
    def menuStart(self) :
        menu_list = [None , self.onVending , self.printHistory]
        
        while True :
            self.printMenu()
            select = int(input("메뉴 선택 : "))
            
            if select > 0 and select < len(menu_list) :
                menu_list[select]()
            elif select == 0 :
                return False
            else : 
                print("메뉴를 잘못 선택하였습니다.")


# 관리자 클래스 제작 중 - 시간내로 안될 수도 있음
class Admin :
    def __init__(self) :
        pass
    
    # 상품 추가는 자판기 클래스를 생성 후 전역 변수 리스트에 직접 추가
    def addGoods(self) :     
        admin = Vendingmachine()
        admin.goods_list.append(input("상품명 입력 : "))
        admin.price_list.append(int(input("가격 입력 : ")))
        admin.inventory_list.append(int(input("재고 입력 : ")))
        print("상품 추가 완료")
    
    # 자판기 클래스 생성
    # 삭제하고 싶은 상품의 이름을 부분 검색 후 변수에 입력
    # 검색된 항목이 없는 경우 경고문 발생
    # 검색된 경우 삭제하고 싶은 상품의 번호를 선택
    # 인덱스 -> 이름으로 변경 -> 이름을 다시 자판기 클래스 내에서 검색 후 인덱스 확보
    # 확보한 인덱스를 가지고 상품명 , 금액 , 재고 부분 삭제
    def delGoods(self) :
        admin = Vendingmachine()
        name  = input("삭제할 상품 이름 입력 : ")
        goods_name = list(filter(lambda x : name in x , admin.goods_list))

        if len(goods_name) <= 0 :
            print("검색된 상품이 없습니다")
            return
        
        for i , v in enumerate(goods_name) :
            print(f"[{i}] | 상품명 : {v}")
        goods_index = goods_name.index(goods_name[int(input("삭제할 상품의 번호를 입력 : "))])
        goods_name  = goods_name[goods_index]
        
        del_goods_index = admin.goods_list.index(goods_name)
        del admin.goods_list[del_goods_index]
        del admin.price_list[del_goods_index]
        del admin.inventory_list[del_goods_index]
        print(f"{goods_name} 상품이 삭제되었습니다.")
    
    # 상품 정보를 수정하는 함수
    # 구조는 삭제 함수와 동일함
    def modifyGoods(self) :
        admin = Vendingmachine()
        name  = input("수정할 상품 이름 입력 : ")
        goods_name = list(filter(lambda x : name in x , admin.goods_list))

        if len(goods_name) <= 0 :
            print("검색된 상품이 없습니다")
            return
        
        for i , v in enumerate(goods_name) :
            print(f"[{i}] | 상품명 : {v}")
        goods_index = goods_name.index(goods_name[int(input("수정할 상품의 번호를 입력 : "))])
        goods_name  = goods_name[goods_index]
        
        modify_goods_index = admin.goods_list.index(goods_name)
        admin.goods_list[modify_goods_index]        = input("상품명 입력 : ")
        admin.price_list[modify_goods_index]        = (int(input("가격 입력 : ")))
        admin.inventory_list[modify_goods_index]    = (int(input("재고 입력 : ")))
        print(f"{admin.goods_list[modify_goods_index]} 상품이 수정되었습니다.")
    
    # 시간이 안되어서 CSV 받아서 메뉴 한번에 넣는 건 불가 / 집에서 추가 예정
    def loadMenu(self) :
        pass
    
    # 관리자 프로그램 메뉴 출력
    def printAdminmenu(self) :
        print("====== 관리자 메뉴 ======")
        print("[1] 상품 추가")
        print("[2] 상품 삭제")
        print("[3] 상품 수정")
        print("[0] 관리자 프로그램 종료")
        print("====== 관리자 메뉴 ======")
    
    # 자판기 작동
    def menuAdminStart(self) :
        menu_list = [None , self.addGoods , self.delGoods , self.modifyGoods]
        
        while True :
            self.printAdminmenu()
            select = int(input("메뉴 선택 : "))
            
            if select > 0 and select < len(menu_list) :
                menu_list[select]()
            elif select == 0 :
                return False
            else : 
                print("메뉴를 잘못 선택하였습니다.")
        
    
# 실행 구간 ==================================================================== #
def start() :
    if __name__ == "__main__" :
        while True :
            print("[1] 관리자 메뉴 입장")
            print("[2] 자판기 이용")
            print("[0] 프로그램 종료")
            select = input("메뉴 선택 : ")
            if select   == "1" :
                program = Admin()
                program.menuAdminStart()
            elif select == "2" :
                program = Vendingmachine()
                program.menuStart()
            elif select == "0" :
                return False
            else :
                print("메뉴를 잘못 선택하였습니다.")

start()
