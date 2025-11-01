import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        students = read_students(input_file)
        write_students(output_file, students)
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")


def read_students(filename):
    students = []
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].split(",")
            students.append({
                "first": first.strip(),
                "last": last.strip(),
                "house": row["house"]
            })
    return students


def write_students(filename, students):
    with open(filename, "w", newline="") as file:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)


if __name__ == "__main__":
    main()