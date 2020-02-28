from requests.auth import HTTPDigestAuth
import avatica

connection = avatica.connect(url="http://localhost:8989", max_retries=3,
                             auth=HTTPDigestAuth('username', 'password'))

cursor = connection.cursor()
cursor.execute("SELECT * FROM orders WHERE retailer_code = 'aitiantian' AND order_no = 'LS1372611101001'")
for row in cursor:
    print(row)


cursor.execute("SELECT * FROM orders WHERE retailer_code = 'aitiantian' AND order_no = 'LS1372611101001'")
for row in cursor:
    print(row)