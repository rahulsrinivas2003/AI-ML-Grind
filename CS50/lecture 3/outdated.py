def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date = input("Date: ").strip()

        # Format 1: MM/DD/YYYY
        if "/" in date:
            try:
                m, d, y = date.split("/")
                m = int(m)
                d = int(d)

                if 1 <= m <= 12 and 1 <= d <= 31:
                    print(f"{y}-{m:02}-{d:02}")
                    break
            except:
                pass

        # Format 2: Month D, YYYY
        elif "," in date:
            try:
                part1, y = date.split(",")
                month_name, d = part1.split()
                d = int(d)

                if month_name in months and 1 <= d <= 31:
                    m = months.index(month_name) + 1
                    print(f"{y.strip()}-{m:02}-{d:02}")
                    break
            except:
                pass


main()
