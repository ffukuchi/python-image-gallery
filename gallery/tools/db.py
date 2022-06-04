import psycopg2

db_host = "database-1.cccvghq7yvdn.us-east-1.rds.amazonaws.com"
db_name = "image_gallery"
db_user = "image_gallery"

password_file = "/home/ec2-user/.image_gallery_config"

connection = None
user_input = 0

def get_password():
    f = open(password_file, "r")
    result = f.readline()
    f.close()
    return result[:-1]

def connect():
    global connection
    connection = psycopg2.connect(host=db_host, dbname="image_gallery", user="postgres", password=get_password())

def execute(query, args=None):
    global connection
    cursor = connection.cursor()
    if not args:
        cursor.execute(query)
    else:
        cursor.execute(query, args)
    return cursor



def main():
    connect()
    res = execute('select * from users')
    user_input = 0

    while (user_input != 5):
        print("\n")
        print("1 List users")
        print("2 Add user")
        print("3 Edit user")
        print("4 Delete user")
        print("5 Quit")
        user_input = int(input("Enter command> "))

        if (user_input == 1):
            for row in res:
                print(row)

        if (user_input == 2):

            new_user = input("Username> ")
            new_password = input("Password> ")
            new_fullname = input("Full name> ")

        if (user_input == 3):
            user_to_edit = input("Username to edit> ")
            user_password_to_edit = input("New password (press enter to keep current)>")
            fullnamed_to_edit = input("New full name (press enter to keep current)>")

        if (user_input == 4):
            user_input = input("Enter username to delte> ")
            confirmation = input("Are you sure that you want to delete {user_input}?")

            if (confirmation == 'Yes'):
                res = execute("delete from users where username=%s, password=%s, full name=%s")

        if (user_input == 5):
            print("Good Bye")
            return



        
"""
    for row in res:
        print(row)

    res = execute("update users set password=%s where username='fred'", ('banana',))
    res = execute('select * from users')
    for row in res:
        print(row)
"""

if __name__ == '__main__':
    main()

