contacts = []

def add_contact():
    print("--------- إضافة جهة اتصال جديدة ---------")
    while True:
        name = input("أدخل اسم جهة الاتصال:")
        duplicate = any(name.lower() == contact.split(" - ")[0].lower() for contact in contacts)
        if duplicate:
            print("هذا الاسم موجود مسبقاً، الرجاء استخدام اسم آخر")
        else:
            break
    while True:
        phone = input("أدخل رقم الهاتف: ")
        if not phone.isdigit():
            print("خطأ: رقم الهاتف يجب أن يحتوي على أرقام فقط.")
        else:
            break
    contact=f"{name} - {phone}"
    contacts.append(contact)
    print("تمت الإضافة بنجاح.")

def search_contact():
    print("---------- البحث عن جهة اتصال ----------")
    search_contact_input = input("أدخل الاسم أو رقم الهاتف للبحث: ")
    found_contacts = [contact for contact in contacts if search_contact_input.lower() in contact.lower()]
    if found_contacts:
        print("تم العثور على الجهة:")
        for c in found_contacts:
            print(c)
    else:
        print("لم يتم العثور على الجهة.")

def delete_contact_with_confirm():
    print("------- حذف جهة اتصال مع التأكيد -------")
    delete_input = input("أدخل اسم جهة الاتصال المراد حذفها او الرقم: ").strip().lower()
    matches = [contact for contact in contacts if delete_input == contact.split(" - ")[0].strip().lower() or delete_input == contact.split(" - ")[1].strip()
]

    if matches:
        contact = matches[0]
        print(f"سيتم حذف الجهة التالية: {contact}")
        while True:
            confirmation = input("هل أنت متأكد من الحذف؟ (نعم/لا): ")
            if confirmation == "نعم":
                contacts.remove(contact)
                print("تم حذف جهة الاتصال بنجاح.")
                break
            elif confirmation == "لا":
                print("تم إلغاء عملية الحذف.")
                break
            else:
                print("الرجاء كتابة (نعم) أو (لا) فقط.")
    else:
        print("الاسم أو الرقم غير موجود.")

def show_contacts():
    print("------------ جميع جهات الاتصال ------------")
    if not contacts:
        print(" لا توجد جهات اتصال حالياً.")
    else:
        for i, contact in enumerate(contacts):
            print(f"[{i+1}] {contact}")


def delete_contact_direct():
    print("-------- حذف جهة اتصال بدون تأكيد --------")
    delete_input = input("أدخل اسم جهة الاتصال أو الرقم المراد حذفه: ").strip().lower()

    matches = [contact for contact in contacts if delete_input == contact.split(" - ")[0].strip().lower() or delete_input == contact.split(" - ")[1].strip()
]

    if matches:
        contact = matches[0]
        print(f"تم حذف الجهة التالية: {contact}")
        contacts.remove(contact)
    else:
        print("الاسم أو الرقم غير موجود.")

def exit_program():
    print("تم الخروج من البرنامج ...               ")
    exit()

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

while True:
    choose = input("الرجاء اختيار رقم الخيار (1-6):         ")

    if choose == "1":
        add_contact()
    elif choose == "2":
        search_contact()
    elif choose == "3":
        delete_contact_with_confirm()
    elif choose == "4":
        show_contacts()
    elif choose == "5":
        delete_contact_direct()
    elif choose == "6":
        exit_program()
    else:
        print(" خيار غير صحيح، الرجاء اختيار رقم من 1 إلى 6.")