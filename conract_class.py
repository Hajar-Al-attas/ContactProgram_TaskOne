class Contact:
    def __init__(self):
        self.contacts={}
        self.active=True


    def add_contact(self):
        print("--------- إضافة جهة اتصال جديدة ---------")
        while True:
            name = input("أدخل اسم جهة الاتصال: ")
            if name in self.contacts:
                print("هذا الاسم موجود مسبقاً، الرجاء استخدام اسم آخر")
            else:
                break
        while True:
            phone = input("أدخل رقم الهاتف: ")
            if not phone.isdigit():
                print("خطأ: رقم الهاتف يجب أن يحتوي على أرقام فقط.")
            else:
                break
        self.contacts[name] = phone
        print("تمت الإضافة بنجاح.")

    def search_contact(self):
        print("---------- البحث عن جهة اتصال ----------")
        search_contact = input("أدخل الاسم أو رقم الهاتف للبحث: ").strip().lower()
        found_contacts = [    (name, phone) for name, phone in self.contacts.items() if search_contact in name.lower() or search_contact in phone ]
        if found_contacts:
            for name, phone in found_contacts:
                print(f"تم العثور على الجهة: الاسم: {name} - رقم الهاتف: {phone}")
        else:
            print("لم يتم العثور على الجهة.")

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

    def show_contacts(self):
        print("------------ جميع جهات الاتصال ------------")
        if not self.contacts:
            print("لا توجد جهات اتصال حالياً.")
        else:
            for i, (name, phone) in enumerate(self.contacts.items()):
                print(f"[{i+1}] {name} - {phone}")

    def delete_contact_direct(self):
        print("-------- حذف جهة اتصال بدون تأكيد --------")
        name = input("أدخل اسم جهة الاتصال أو الرقم المراد حذفه: ")

        found = [n for n, p in self.contacts.items() if name == n or name == p]

        if found:
            name = found[0]
            print(f"تم حذف الجهة التالية: الاسم: {name} - رقم الهاتف: {self.contacts[name]}")
            del self.contacts[name]
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
        C.add_contact()
    elif choose == "2":
        C.search_contact()
    elif choose == "3":
        C.delete_contact_with_confirm()
    elif choose == "4":
        C.show_contacts()
    elif choose == "5":
        C.delete_contact_direct()
    elif choose == "6":
        C.exit_program()
    else:
        print("خيار غير صحيح، الرجاء اختيار رقم من 1 إلى 6.")
