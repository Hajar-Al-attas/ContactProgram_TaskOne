class Contact:
    def __init__(self):
        self.contacts={}
        self.active=True

    def __setitem__(self,name,phone):
            if name in self.contacts:
                print("هذا الاسم موجود مسبقاً، الرجاء استخدام اسم آخر")
            else:
                if not phone.isdigit():
                    print("خطأ: رقم الهاتف يجب أن يحتوي على أرقام فقط.")
                else:
                    self.contacts[name] = phone
                    print("تمت الإضافة بنجاح.")

    def __contains__(self, search):
        found_contacts = [(name, phone)  for name, phone in self.contacts.items() if search.lower() in name.lower() or search in phone]
        if found_contacts:
            print("---------نتائج البحث----------")
            for name, phone in found_contacts:
                print(f"الاسم: {name} - رقم الهاتف: {phone}")
            return True
        else:
            print("لم يتم العثور على أي جهة مطابقة.")
            return False

    def __str__(self):
        if not self.contacts:
            return "لا توجد جهات اتصال حالياً."
        result = "------------ جميع جهات الاتصال ------------\n"
        for i, (name, phone) in enumerate(self.contacts.items(), start=1):
            result += f"[{i}] {name} - {phone}\n"
        return result.strip()

    def __delitem__(self, key):
        if key in self.contacts:
            print(f"تم حذف الجهة التالية: الاسم: {key} - رقم الهاتف: {self.contacts[key]}")
            del self.contacts[key]
        else:
            print("الاسم أو الرقم غير موجود.")

    def delete_contact_with_confirm(self):
        print("------- حذف جهة اتصال مع التأكيد -------")
        name = input("أدخل اسم جهة الاتصال المراد حذفها او الرقم: ")

        found = [n for n, p in self.contacts.items() if name == n or name == p]

        if found:
            name = found[0]
            print(f"سيتم حذف الجهة التالية: الاسم: {name} - رقم الهاتف: {self.contacts[name]}")
            while True:
                confirmation = input("هل أنت متأكد من الحذف؟ (نعم/لا): ")
                if confirmation == "نعم":
                    del self.contacts[name]
                    print("تم حذف جهة الاتصال بنجاح.")
                    break
                elif confirmation == "لا":
                    print("تم إلغاء عملية الحذف.")
                    break
                else:
                    print("الرجاء كتابة (نعم) أو (لا) فقط.")
        else:
            print("الاسم أو الرقم غير موجود.")

    def exit_program(self):
        print("تم الخروج من البرنامج ...")
        self.active = False
C = Contact()
print("========================================")
print("│       برنامج إدارة جهات الاتصال       │")
print("========================================")
print("┌──────────────────────────────────────┐")
print("│  1. إضافة جهة اتصال جديدة            │")
print("│  2. البحث عن جهة اتصال               │")
print("│  3. حذف جهة اتصال مع التأكيد         │")
print("│  4. عرض جميع جهات الاتصال             │")
print("│  5. حذف جهة اتصال بدون تأكيد         │")
print("│  6. الخروج                           │")
print("└──────────────────────────────────────┘")

while C.active:
    choose = input("الرجاء اختيار رقم الخيار (1-6): ")
    if choose == "1":
        print("--------- إضافة جهة اتصال جديدة ---------")
        while True:
            name = input("أدخل اسم جهة الاتصال: ")
            if name in C.contacts:
                print("هذا الاسم موجود مسبقاً، الرجاء استخدام اسم آخر.")
            else:
                break
        phone = input("أدخل رقم الهاتف: ")
        C[name] = phone
    elif choose == "2":
        search = input("أدخل اسم جهة الاتصال أو الرقم للبحث: ")
        if search in C:
            print("تم العثور على جهة الاتصال.")
        else:
            print("لم يتم العثور على جهة الاتصال.")
    elif choose == "3":
        C.delete_contact_with_confirm()
    elif choose == "4":
        print(C)
    elif choose == "5":
        name = input("أدخل اسم جهة الاتصال المراد حذفها  : ")
        del C[name]
    elif choose == "6":
        C.exit_program()
    else:
        print("خيار غير صحيح، الرجاء اختيار رقم من 1 إلى 6.")
