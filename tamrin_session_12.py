from datetime import date, time , datetime , timedelta
import jdatetime

lesson_list = [
    "شروع دوشنبه ۱۶ شهریور ۱۴۰۵ - دوشنبه ۱۶:۰۰ تا ۲۰:۰۰",
    "شروع سه شنبه ۱۷ شهریور ۱۴۰۵ - سه شنبه ۱۱:۰۰ تا ۱۲:۰۰"
]

# str : replace, split

#  اگر تاریخ و روز هفته غلط است هشدار دهد

#lesson_list = [
   # {"start_date": date(2026,9,7), "start_time": time(16,0), "end_time": time(20,0)},
  #  {"start_date": date(2026,9,8), "start_time": time(11,0), "end_time": time(14,0)}
#]

#persian_month=["فروردین","اردیبهشت","خرداد","تیر","مرداد","شهریور","مهر","آبان","آذر","دی","بهمن","اسفند"]

def fa_to_en(text):
    fa_digits="۰۱۲۳۴۵۶۷۸۹"
    en_digits="0123456789"
    for f,e in zip(fa_digits, en_digits):
        text= text.replace(f,e)
    return text

def order(word):
   word=fa_to_en(word)
   word=word.replace("\u200c"," ").replace("\t"," ")
   replacement={"یک_شنبه":"یک شنبه",
                 "دو_شنبه":"دو شنبه",
                "سه_شنبه": "سه شنبه",
                 "چهار_شنبه": "چهار شنبه",
                 "پنج_شنبه": "پنچ شنبه",
                "شروع":"",
               "تا":"",
                "-":""}

   for old,new in replacement.items():
       word=word.replace(old,new)

   parts=word.split()
   print(parts)
   mentioned_weekday=parts[0]
   day=int(parts[1])
   month_name=parts[2]
   month_number=jdatetime.datetime.strptime(month_name,"%B").month
  #month_number=persian_month.index(month_name)+1
   year=int(parts[3])
   start_time_hour,start_time_minute=map(int,parts[5].split(":"))
   end_time_hour,end_time_minute=map(int,parts[6].split(":"))

   the_start_time=time(start_time_hour,start_time_minute)
   the_end_time=time(end_time_hour,end_time_minute)


   date_in_persian=jdatetime.date(year,month_number,day)
   the_real_weekday=date_in_persian.weekday()

   if mentioned_weekday != the_real_weekday:
       print(mentioned_weekday ,"مصادف با این تاریخ نیست")

   date_in_english=date_in_persian.togregorian()

   the_start_date=date(date_in_english.year,date_in_english.month,date_in_english.day)

   return {
       "start_date":the_start_date,
       "start_time":the_start_time,
       "end_time":the_end_time,
   }

final_lesson_list=[order(word) for word in lesson_list]

print(final_lesson_list)
