import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    work_times = []
    work_hours = []

    try:
        work_times = re.findall(r"^\d.*\b(?= to)|(?<=to\s).*?[a-z]\b", s, re.IGNORECASE)

        if len(work_times) > 2 or len(work_times) < 2:
            raise ValueError

        for wt in work_times:

            if " am" in str(wt).lower():
                wt = str(wt).lower().strip(" am")

                if has_minutes := re.match(r"^(1[0-2]|0?[1-9]):([0-5]?[0-9])$", wt):

                    if int(has_minutes.group(1)) > 12 or int(has_minutes.group(1)) < 1:
                        raise ValueError

                    elif int(has_minutes.group(1)) == 12:
                        work_hours.append(f"00:{has_minutes.group(2)}")

                    elif int(has_minutes.group(1)) <= 9:
                        work_hours.append(
                            f"0{has_minutes.group(1)}:{has_minutes.group(2)}"
                        )

                    else:
                        work_hours.append(
                            f"{has_minutes.group(1)}:{has_minutes.group(2)}"
                        )

                elif has_hours := re.match(r"^(1[0-2]|0?[1-9])", wt):

                    if int(wt) > 12 or int(wt) < 1:
                        raise ValueError

                    elif int(has_hours.group(1)) == 12:
                        work_hours.append(f"00:00")

                    elif int(has_hours.group(1)) <= 9:
                        work_hours.append(f"0{has_hours.group(1)}:00")

                    else:
                        work_hours.append(f"{has_hours.group(1)}:00")

                else:
                    raise ValueError

            if " pm" in str(wt).lower():
                wt = str(wt).lower().strip(" pm")

                if has_minutes := re.match(r"^(1[0-2]|0?[1-9]):([0-5]?[0-9])$", wt):

                    if int(has_minutes.group(1)) > 12 or int(has_minutes.group(1)) < 1:
                        raise ValueError

                    elif int(has_minutes.group(1)) == 12:
                        work_hours.append(f"12:{has_minutes.group(2)}")

                    else:
                        work_hours.append(f"{int(has_minutes.group(1)) + 12}:{has_minutes.group(2)}")

                elif has_hours := re.match(r"^(1[0-2]|0?[1-9])", wt):

                    if int(wt) > 12 or int(wt) < 1:
                        raise ValueError

                    elif int(has_hours.group(1)) == 12:
                        work_hours.append(f"12:00")

                    else:
                        work_hours.append(f"{int(has_hours.group(1)) + 12}:00")

                else:
                    raise ValueError

    except ValueError:
        raise ValueError
    if len(work_hours) == 2:
        return f"{work_hours[0]} to {work_hours[1]}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()