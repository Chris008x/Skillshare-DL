import sys, os
from skillshare import Skillshare, splash


# or by class ID:
# dl.download_course_by_class_id(189505397)

def main():
    dl = Skillshare("PHPSESSID=2963acb7c6e56e7f6e14e20f07aa3e5a")
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


if __name__ == "__main__":
    splash()
    main()
