import time as t
from datetime import datetime as dt

plate_times = [
    ["YK52 ABC", "09:35:23", "11:36:24"],
    ["PR15 GHR", "09:37:00", "15:15:01"],
    ["YK52 QRR", "09:42:28", "10:45:00"],
    ["YK52 HGH", "09:57:57", "09:58:21"],
    ["GG72 YUU", "10:01:07", "11:35:19"],
    ["FR08 NBG", "10:13:19", "12:26:28"],
    ["PK11 VVF", "11:27:42", "11:35:24"],
    ["YT55 AFS", "12:02:16", "16:35:24"]
]

for i, p in enumerate(plate_times):
    plate_times[i][1] = dt.strptime(p[1], '%H:%M:%S')
    plate_times[i][2] = dt.strptime(p[2], '%H:%M:%S')

customers = [
    ["AB12 DDD", "Random McRandom", "1 Python Lane, Leeds"],
    ["YT55 AFS", "Larry McHarry", "99 Procedure Road, Manchester"],
    ["YK52 ABC", "Fred Smith", "18 Random Street, Bradford"],
    ["FR08 NBG", "Stephen Rogers", "101 Concatenation Lane, Batley"],
    ["YK52 QRR", "David Beckham", "19 Integer Road, Huddersfield"],
    ["YK52 HGH", "Martin Stevens", "582 Database Street, Leeds"],
    ["GG72 YUU", "Ronald McDonald", "89 String Lane, Wakefield"],
    ["PK11 VVF", "Harry Jameson", "17 Variable Road, Dewsbury"],
    ["PR15 GHR", "John Williams", "52 Boolean Street, London"]
]

MAIL_TEMPLATE = """
{address}

Dear {name},

It has come to our attention that vehicle registration <reg goes here> was parked in our car park for {time} hours. 
There is a £200 fine for all customers that stay longer than 2 hours in our car park. You car arrived at {start} 
and left at {end} and this is a total time of {time} hours. This has resulted in a fine that you must pay in the next 
10 working days. 

Kind Regards,
The Fine Team
"cha-ching"
"""


def main():
    # check for overstayers
    cprint("OVERSTAYERS\n")
    for plate in plate_times:
        d = delta(plate[1], plate[2])
        if d > 2:
            c = lookup(plate[0])
            cprint(f"{c[0]} - {c[1]}: {c[2]}")

            # draft letter
            l_name = c[1].lower().replace(" ", "-") + ".txt"
            with open(l_name, "w") as f:
                f.write(MAIL_TEMPLATE.format(
                    address=c[2],
                    name=c[1],
                    time=round(d, 2),
                    start=plate[1].time(),
                    end=plate[2].time()
                ))


def lookup(plate):
    for c in customers:
        if c[0] == plate:
            return c


def delta(s, e):
    return (e - s).seconds / 3600


last = 0
gap = 0.5


def cprint(msg):
    global last

    for s in msg.split("\n"):
        now = t.time()
        if now - last < gap:
            extra = gap - (now - last)
            t.sleep(extra)
        last = t.time()

        print(s)


if __name__ == "__main__":
    main()
