# -----------------------------------Project on Ticket Machine by "Dawit" & "Yonas"---------------------------------
# The program will ask the consumer which of the places they wish to visit, and depending on the
# area they choose, it will assign them a relevant turn number.

# to make emoji we need to import and install emoji library
import emoji as emoji

# to make timer we need to import and install time library
import time

# define the countdown function
def countdown():
    time_sec = 10
    while time_sec > 0:
        minutes, secs = divmod(time_sec, 60)
        hour, minutes = divmod(minutes, 60)
        timeleft = str(hour).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(secs).zfill(2)
        print(timeleft + "\r", end='')
        time.sleep(1)
        time_sec -= 1
        print(timeleft)
    print('\n You are done for today !!')
    print(emoji.emojize('\n\t\t\t\t\tThank you for visiting us '
                        '\n\t\t\t\t\t\t Have a nice day :grinning_face_with_big_eyes::thumbs_up:'))


# define the message display text function
def message_display():
    print("\n\t\t\t\tWELLCOME to 'DY' Pharmacy Drag Store!!!!!!!!!!!!")
    print("\t\t\t\t*********************   *********************")
    print("\t\tCHOOSE SITE FOR: ")
    print("\t\t\t\t\t\tCOSMETIC = 'C'\n"
          "\t\t\t\t\t\tPERFUME =  'P'\n"
          "\t\t\t\t\t\tMEDICINE = 'M'\n")


# Define thank you message function
def thank_you():
    print(emoji.emojize('\n\t\t\t\t\tThank you for visiting us '
                        '\n\t\t\t\t\t\t Have a nice day :grinning_face_with_big_eyes::thumbs_up:'))


# Define cosmetic site ticket generator
def cosmo_site():
    cosmo_queue_num = 1
    cosmo_ticket_num = 0
    while True:
        yield cosmo_queue_num
        cosmo_queue_num, cosmo_ticket_num = cosmo_queue_num + 1, cosmo_ticket_num + 1


# Define medicine site ticket generator
def medicine_site():
    medicine_queue_num = 1
    medicine_ticket_num = 0
    while True:
        yield medicine_queue_num
        medicine_queue_num, medicine_ticket_num = medicine_queue_num + 1, medicine_ticket_num + 1


# Define perfumes site ticket generator
def perfumes_site():
    perfume_queue_num = 1
    perfume_ticket_num = 0
    while True:
        yield perfume_queue_num
        perfume_queue_num, perfume_ticket_num = perfume_queue_num + 1, perfume_ticket_num + 1


cosmo_ticket_number = cosmo_site()
medicines_ticket_number = medicine_site()
perfumes_ticket_number = perfumes_site()
count = 0
timer = 1
exit_point = "Stop"
# using id
idnum_dawit = "987654321"
idnum_yonas = "123456789"
id_list = [idnum_dawit, idnum_yonas]

# while exit_point != "stop" and count < 3:
while count < 3:
    idnum = input("Please Enter Valid Id: ")
    if idnum in id_list:
        message_display()
        customer = input("Please Choose Which Site you went to visit--> ")
        if customer == "c" or customer == "C" or customer == "cosmetic" or customer == "COSMETIC":
            print("\n\t\t\t\t Your Ticket Number is C-", next(cosmo_ticket_number))
            print("\t\t\t\t Please wait and someone will assist you shortly.")
            print("===================================================================================")
        elif customer == "p" or customer == "P" or customer == "perfume" or customer == "PERFUME":
            print("\n\t\t\t\t Your Ticket Number is P-", next(perfumes_ticket_number))
            print("\t\t\t\t Please wait and someone will assist you shortly.")
        elif customer == "m" or customer == "M" or customer == "medicine" or customer == "MEDICINE":
            print("\n\t\t\t\t Your Ticket Number is M-", next(medicines_ticket_number))
            print("\t\t\t\t Please wait and someone will assist you shortly.")
        else:
            print("\t\t\t\t Please choose correct valid site you went to visit--> ")
            continue
        other_site = input("\nDo you went to continue seeing other sites yes/no: ")
        if other_site == "y" or other_site == "Y" or other_site == "Yes" or other_site == "YES":
            continue
        elif other_site == "":
            print("You didn't Enter valid input, Please enter valid value ")
            other_site = input("Do you went to continue seeing other sites y/n")
        else:
            thank_you()
            break
    else:
        count += 1
        continue
else:
    print("\nYou Enter invalid ID so many time , please try other time")
    countdown()
