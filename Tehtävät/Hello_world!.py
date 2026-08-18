import time
hello_ascii = """
╔╗─╔╦═══╦╗──╔╗──╔═══╗╔╗
║║─║║╔══╣║──║║──║╔═╗║║║
║╚═╝║╚══╣║──║║──║║─║║║║
║╔═╗║╔══╣║─╔╣║─╔╣║─║║╚╝
║║─║║╚══╣╚═╝║╚═╝║╚═╝║╔╗
╚╝─╚╩═══╩═══╩═══╩═══╝╚╝
"""

bye_ascii ="""
★─▄█▀▀║░▄█▀▄║▄█▀▄║██▀▄║─★
★─██║▀█║██║█║██║█║██║█║─★
★─▀███▀║▀██▀║▀██▀║███▀║─★
★───────────────────────★
★───▐█▀▄─ ▀▄─▄▀ █▀▀──█───★
★───▐█▀▀▄ ──█── █▀▀──▀───★
★───▐█▄▄▀ ──▀── ▀▀▀──▄───★
"""
hello_or_bye = input("")
if hello_or_bye.lower() in ["hello", "bye"]:
    for i in range(1, 100):
        print(f"{i}%")
        time.sleep(0.1)
    if hello_or_bye.lower() == "hello":
        print(hello_ascii)
    elif hello_or_bye.lower() == "bye":
        print(bye_ascii)
else:
    print("Error bitch!")
