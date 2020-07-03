from datetime import datetime


def log(message):
    file = open("logging.txt", "a")
    file.write("<!------!>\n")
    file.write(str(datetime.now()))
    file.write("\nСообщение от {0} {1} (id = {2}) \n{3}\n".format(message.from_user.first_name,
            message.from_user.last_name,
                str(message.from_user.id), message.text))
    file.close()

def log_exception(exception):
    output = "[{}] {}: {}".format('EXPECTED', type(exception).__name__, exception)
    file = open("logging.txt","a")
    file.write("<!------!>")
    file.write(output)
    file.close()