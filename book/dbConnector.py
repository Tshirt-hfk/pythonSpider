import MySQLdb

class DBConnector(object):
	def __init__(self):
		self.db = MySQLdb.connect("localhost", "root", "13866079469", "sao")
		self.db.set_character_set("utf8")

	def insert(self, url, name, author):
		cursor = self.db.cursor()
		sql = "insert into book (url, name, author) values ('%s' ,'%s', '%s')" % (url, name, author)
		o = True
		try:
			cursor.execute(sql)
			self.db.commit()
		except:
			o = False
		finally:
			cursor.close()
		return o

	def isExisted(self, url):
		cursor = self.db.cursor()
		sql = "select * from book where url='%s'" % url
		o = False
		try:
			cursor.execute(sql)
			list = cursor.fetchall()
			if len(list) >= 1:
				o = True
		except:
			o = True
		finally:
			cursor.close()
		return o

	def close(self):
		self.db.close()