
def isleap(year):
    if not year % 4:
        if not year % 400:
            return True
        return bool(year % 100)
    return False

def go():
    norm = [31, 28, 31, 30, 31, 30, 31, 31, 30, 30, 31, 31]
    leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 30, 31, 31]
    good_sundays = 0
    day = 1
    month = 0
    year = 1900
    cal = norm
    gen_dname = iter_day()
    gen_mname = iter_month()
    mname = gen_mname.next()
    while year < 2001:
        dname = gen_dname.next()
        print dname, mname, day, year, isleap(year)
        if dname == "Sun" and day == 1:
            #print "Yay!"
            good_sundays += 1
        day += 1
        if day > cal[month]:
            day = 1
            month += 1
            mname = gen_mname.next()
            if month > 11:
                month = 0
                year += 1
                if isleap(year):
                    cal = leap
                else:
                    cal = norm
    print dname, mname, day, year, isleap(year)
    return good_sundays - 1

def iter_day():
    while 1:
        yield "Mon"
        yield "Tue"
        yield "Wed"
        yield "Thu"
        yield "Fri"
        yield "Sat"
        yield "Sun"

def iter_month():
    while 1:
        yield "Jan"
        yield "Feb"
        yield "Mar"
        yield "Apr"
        yield "May"
        yield "Jun"
        yield "Jul"
        yield "Aug"
        yield "Sep"
        yield "Oct"
        yield "Nov"
        yield "Dev"
        
    
