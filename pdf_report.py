from datetime import datetime


def generate_report(title, content):

    filename = f"{title}_report.txt"

    try:

        with open(filename, "w") as file:

            file.write("PAK ENERGY & TECH HUB\n")
            file.write("Petroleum Engineering Toolkit\n\n")

            file.write(
                f"Report Date: {datetime.now()}\n\n"
            )

            file.write(content)

        return f"Report created: {filename}"


    except Exception as e:

        return f"Error creating report: {e}"