import pymysql

class DBConnector(object):
	def __init__(self):
		self.db = MySQLdb.connect("localhost", "root", "13866079469", "sao")
		self.db.set_character_set("utf8")

	def insert(self, content, author, title):
		cursor = self.db.cursor()
		sql = "insert into motto (content, author, title) values ('%s' ,'%s', '%s')" % (content, author, title)
		o = True
		try:
			cursor.execute(sql)
			self.db.commit()
		except:
			o = False
		finally:
			cursor.close()
		print(sql, "succeed!!!")
		return o

	def close(self):
		self.db.close()