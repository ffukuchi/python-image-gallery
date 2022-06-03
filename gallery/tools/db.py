import psycopg2

db_host = "database-1.cccvghq7yvdn.us-east-1.rds.amazonaws.com"
db_name = "image_gallery"
db_user = "image_gallery"

password_file = "/home/ec2-user/.image_gallery_config"

def get_password():
    f = open(password_file, "r")
    result = f.readline()
    f.close()
    return result[:-1]



conn = psycopg2.connect(host=db_host, dbname="image_gallery", user="postgres", password=get_password())

