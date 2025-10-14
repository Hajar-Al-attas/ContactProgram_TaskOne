contacts = []
def add_contact():
    print("--------- إضافة جهة اتصال جديدة ---------")

    while True:
        name = input("أدخل اسم جهة الاتصال: ")
        duplicate = False
        for contact in contacts:
            if contact["name"].lower() == name.lower():
                print("هذا الاسم موجود مسبقاً، الرجاء استخدام اسم آخر")
                duplicate = True
                break
        if not duplicate:
            break

    while True:
        phone = input("أدخل رقم الهاتف: ")
        if not phone.isdigit():
            print("خطأ: رقم الهاتف يجب أن يحتوي على أرقام فقط.")
        else:
            break

    contacts.append({"name": name, "phone": phone})
    print("تمت الإضافة بنجاح.")


def search_contact():
    print("---------- البحث عن جهة اتصال ----------")
    search_contact = input("أدخل الاسم أو رقم الهاتف للبحث: ").strip().lower()
    found = False

    for contact in contacts:
        if search_contact.lower() in contact["name"].lower() or search_contact.lower() in contact["phone"].lower():
            print(f"تم العثور على الجهة:")
            print(f"الاسم: {contact['name']} - رقم الهاتف: {contact['phone']}")
            found = True

    if not found:
        print("لم يتم العثور على الجهة.")



def delete_contact_with_confirm():
    print("------- حذف جهة اتصال مع التأكيد -------")
    delete_phone = input("أدخل اسم جهة الاتصال المراد حذفها او الرقم: ")
    for contact in contacts:
        if contact["name"].lower() == delete_phone.lower() or contact["phone"] == delete_phone:
            print(f"سيتم حذف الجهة التالية:")
            print(f"الاسم: {contact['name']} - رقم الهاتف: {contact['phone']}")
            while True:
                confirmation = input("هل أنت متأكد من الحذف؟ (نعم/لا): ")
                if confirmation == "نعم":
                    contacts.remove(contact)
                    print("تم حذف جهة الاتصال بنجاح.")
                    return
                elif confirmation == "لا":
                    print("تم إلغاء عملية الحذف.")
                    return
                else:
                    print("الرجاء كتابة (نعم) أو (لا) فقط.")


    print("الاسم غير موجود.")


def show_contacts():
    print("------------ جميع جهات الاتصال ------------")
    if not contacts:
        print(" لا توجد جهات اتصال حالياً.")
    else:
        count = 1
        for contact in contacts:
            print(f"[{count}] {contact['name']} - {contact['phone']}")
            count += 1

def delete_contact_direct():
    print("-------- حذف جهة اتصال بدون تأكيد --------")
    delete_input = input("أدخل اسم جهة الاتصال أو الرقم المراد حذفه: ")

    for contact in contacts:
        if contact["name"].lower() == delete_input.lower() or contact["phone"] == delete_input:
            print(f"تم حذف الجهة التالية:")
            print(f"الاسم: {contact['name']} - رقم الهاتف: {contact['phone']}")
            contacts.remove(contact)
            break
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



