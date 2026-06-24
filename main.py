
def get_validate_input(prompt:str,input_type:str = "str"):
    while True:
        user_input = input(prompt)
        if not user_input:
            print("Dữ liệu không được rỗng")
            continue
        if input_type == "int":
            try:
                value = int(user_input)
                if value < 0 :
                    print("Dữ liệu không được là số âm")
                    continue
                return value
            except ValueError:
                print("Dữ liệu không hợp lệ")
                continue
        return user_input 
    
class CourseRegistration:
    def __init__(self,id,student_name,course_name,tuition_fee,discount,extra_fee):
        self.id = id 
        self.stu_name = student_name
        self.cour_name = course_name 
        self.tui_fee = tuition_fee
        self.discount = discount 
        self.ex_fee = extra_fee
        self.total_fee = 0
        self.fee_type = ""

    def calculate_total_fee(self):
        self.total_fee = (self.tui_fee - self.discount) + self.ex_fee 
    
    def classify_fee(self):
        if self.total_fee < 3000000:
            self.fee_type = "Thấp"
        elif 3000000 <= self.total_fee < 7000000:
            self.fee_type = "Trung Bình"
        elif 7000000 <= self.total_fee < 15000000:
            self.fee_type = "Cao"
        elif self.total_fee >= 15000000:
            self.fee_type = "Rất Cao"

class CourseRegistrationManager:
    def __init__(self):
        self.registrations = []

    def add_registration(self):
        while True:
            self.id = get_validate_input("Nhập mã đăng ký mới: ")
            for regis in self.registrations:
                if self.id.lower() == regis.id.lower():
                    print("Mã đăng ký đã trùng")
                    return
            self.stu_name = get_validate_input("Nhập vào tên học viên: ")
            self.cour_name = get_validate_input("Nhập vào tên khóa học: ")
            self.tui_fee = get_validate_input("Nhập vào học phí gốc: ","int")
            self.discount = get_validate_input("Nhập vào số tiền giảm giá: ","int")
            try : 
                        if self.discount >= self.tui_fee:
                                print("Phí giảm giá quá mức giới hạn")
                                return
            except ValueError:
                        print("Dữ liệu không hợp lệ")
            self.ex_fee = get_validate_input("Nhập vào phụ phí: ","int")

            new_course = CourseRegistration(self.id,self.stu_name,self.cour_name,self.tui_fee,self.discount,self.ex_fee)
            new_course.calculate_total_fee()
            new_course.classify_fee()
            self.registrations.append(new_course)
            print("Thêm đăng ký khóa học thành công!")
            break
    
    def show_all(self):
        if not self.registrations:
            print("Danh sách đăng ký khóa học đang rỗng")
            return
        print(f"{"Mã đăng ký":<15}| {"Họ và tên":<20}| {"Tên khóa học":<15}| {"Học phí gốc":<12}| {"Giảm giá":<12}| {"Phụ phí":<12}| {"Tổng học phí":<15}| {"Phân loại học phí":<15}")
        for regis in self.registrations:
            print(f"{regis.id:<15}| {regis.stu_name:<20}| {regis.cour_name:<15}| {regis.tui_fee:<12}| {regis.discount:<12}| {regis.ex_fee:<12}| {regis.total_fee:<15}| {regis.fee_type:<15}")
    
    def update_registration(self):
        if not self.registrations:
            print("Danh sách đăng ký khóa học đang rỗng")
            return
        self.id = get_validate_input("Nhập vào mã khóa học cần cập nhật: ")
        for regis in self.registrations:
                if self.id.lower() == regis.id.lower():
                    self.tui_fee = get_validate_input("Cập nhật học phí gốc: ","int")
                    self.discount = get_validate_input("Cập nhật phí giảm giá: ","int")
                    try : 
                        if self.discount >= self.tui_fee:
                                print("Phí giảm giá quá mức giới hạn")
                                return
                        return self.discount
                    except ValueError:
                        print("Dữ liệu không hợp lệ")
                    self.ex_fee = get_validate_input("Cập nhật phụ phí: ","int")

                    regis.tui_fee = self.tui_fee
                    regis.discont = self.discount
                    regis.ex_fee = self.ex_fee
                    regis.calculate_total_fee()
                    regis.classify_fee()
                    print("Đã cập nhật thành công")
                    break
        else :
            print("Không tìm thấy khóa học cần cập nhật")

    def delete_registration(self):
        if not self.registrations:
            print("Danh sách đăng ký khóa học đang rỗng")
            return
        self.id = get_validate_input("Nhập vào mã khóa học cần xóa: ")
        for regis in self.registrations:
                if self.id.lower() == regis.id.lower():
                    choice = get_validate_input("Bạn có chắc chắn muốn xóa khóa học này không (Y/N): ").lower()
                    match choice:
                        case "y":
                            self.registrations.remove(regis)
                            print("Xóa đăng ký khóa học thành công")
                            break
                        case "n":
                            print("Đã hủy thao tác xóa")
                            break
                        case _:
                            print("Lựa chọn không hợp lệ")
                            break
        else : 
            print("Không tìm thấy khóa học cần xóa")


    def search_registration(self):
        if not self.registrations:
            print("Danh sách đăng ký khóa học đang rỗng")
            return
        self.name = get_validate_input("Nhập từ khóa tìm kiếm: ")
        found = False
        for regis in self.registrations:
            if self.name.lower() in regis.stu_name.lower() or self.name.lower() in regis.cour_name.lower():
                print(f"Học và tên: {regis.stu_name} - Khóa học: {regis.cour_name}")
                found = True
        if not found:
            print("Không tìm thấy đăng ký khóa học phù hợp")



def main():
    course_manager = CourseRegistrationManager()
    while True:
        print("""
================MENU================
1.Hiển thị danh sách đăng ký khóa học
2.Thêm đăng ký khóa học mới
3.Cập nhật học phí
4.Xóa đăng ký khóa học
5.Tìm kiếm đăng ký
6.Thoát
====================================
""")
        choice = get_validate_input("Nhập lựa chọn của bạn: ")
        match choice:
            case "1":
                course_manager.show_all()
            case "2":
                course_manager.add_registration()
            case "3":
                course_manager.update_registration()
            case "4":
                course_manager.delete_registration()
            case 5: 
                course_manager.search_registration() 
            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý khóa học")
                break
            case _:
                print("Lựa chọn của bạn không hợp lệ")
            



if __name__ == "__main__":
    main()

            