# # liste =open("cuzdan.oto", "r+")
# # for  i in range (100)  :
# #  if(i==99):
# #     liste\
# #         .write (str(i+1))
# #     continu



# # liste += str(i+1) + ", "


# # finally:
# #     if dosya 
# with open("cuzdan.oto") as dosya :
#     print(dosya.read())
# from datetime import datetime

# # print(datetime.now())
# """ simdi adli bir ofnksiyon tanimladim . . . . """
# simdi = datetime.now
# ne_zaman = datetime()
# print(simdi())









# from datetime import datetime

# # current time and date
# # datetime object
# time = datetime.now()

# # formatting date using strftime
# # format = MM/DD/YY
# print(time.strftime("%m/%d/%y"))

# # format = Month D, Yr
# print(time.strftime("%B %d, %Y"))

# # time formatting
# # HH:MM:SS
# print(time.strftime("%H:%M:%S"))





# from datetime import datetime

# # current time and date
# # datetime object
# time = datetime.now()
# print("Without formatting:", time)

# # formatting date using strftime
# print("Year", time.strftime("%Y"))
# print("Month name", time.strftime("%B"))
# print("Day", time.strftime("%d"))


from datetime import datetime

# current time and date
# datetime object
time = datetime.now()

# formatting date using strftime
# format = MM/DD/YY
print(time.strftime("%m/%d/%y"))

# format = Month D, Yr
print(time.strftime("%B %d, %Y"))

# time formatting
# HH:MM:SS
print(time.strftime("%H:%M:%S"))
