# -*- encoding: utf-8 -*-
import MySQLdb
from hashlib import md5
from uuid import uuid4
import time

from django.conf import settings
from django.contrib import messages


class DB():
	def __init__(self, host=settings.FORUM_DB_HOST, name=settings.FORUM_DB_NAME,
		user=settings.FORUM_DB_USER, passwd=settings.FORUM_DB_PASS, port=settings.FORUM_DB_PORT):
		self.host = host
		self.name = name
		self.user = user
		self.passwd = passwd
		self.port = port
		self.connection = MySQLdb.connect(host=self.host,
			db=self.name, user=self.user, passwd=self.passwd, port=self.port)
		self.cursor = self.connection.cursor()
		self.connection.set_character_set('utf8')
		self.cursor.execute('SET NAMES utf8;')
		self.cursor.execute('SET CHARACTER SET utf8;')
		self.cursor.execute('SET character_set_connection=utf8;')

	def __del__(self):
		self.connection.close()

	def get_tablename(self, tablename, prefix=settings.FORUM_DB_PREFIX):
		if prefix:
			return "%s%s" % (prefix, tablename)
		else:
			return tablename


def get_last_topics(topics_num=5):
	db = DB()
	cursor = db.cursor
	topics_tablename = db.get_tablename("topics")
	query = """
		SELECT title, posts, starter_name, start_date FROM %s ORDER BY posts DESC LIMIT %s
	""" % (topics_tablename, topics_num)
	cursor.execute(
		"""
			SELECT title, posts, starter_name, start_date FROM """ + topics_tablename + \
			""" ORDER BY posts DESC LIMIT %s""",
		(topics_num, )
	)
	topic_list = cursor.fetchall()
	return topic_list


def generate_forum_passwd(password):
	salt = str(uuid4())[:5]
	hash_passwd = md5(md5(salt).hexdigest()+md5(password ).hexdigest()).hexdigest()
	return (salt, hash_passwd)


def register_forum_user(username, password, ip_address):
	db = DB()
	salt, hash_passwd = generate_forum_passwd(password)
	joined = int(time.time())
	legacy_password = md5(password).hexdigest()
	members_l_display_name = username
	members_l_username = username.lower()
	member_group_id = 3  # "Beginer" group
	members_table_name = str(db.get_tablename(u'members'))
	cursor = db.cursor
	cursor.execute(
		"""
			INSERT INTO """ + members_table_name + """(
				name, members_pass_hash, members_pass_salt, ip_address, joined,
				members_l_display_name, members_l_username, member_group_id
				)
				VALUES
				(%s, %s, %s, %s, %s, %s, %s, %s)
		""", (
			username, hash_passwd, salt, ip_address, joined,
			members_l_display_name,	members_l_username, member_group_id
			)
	)

def forum_login(request, response):
	db = DB()
	cursor = db.cursor
	username = request.user.username
	session_id = request.session.session_key
	ip_address = request.META['REMOTE_ADDR']
	running_time = int(time.time())

	members_tablename = db.get_tablename("members")
	cursor.execute(""" SELECT member_id, members_pass_hash FROM """ + members_tablename + """ WHERE name=%s""", (username, ))
	forumuser = cursor.fetchone()
	if forumuser:
		member_id, members_pass_hash = forumuser
	else:
		messages.warning(request, 'Вы не аутентифицированы на форуме. Обратитесь к администратору')
		return response
	
	sessions_tablename = db.get_tablename("sessions")
	query = """
		INSERT INTO """ + sessions_tablename + """ (id, member_id, ip_address, running_time)
		VALUES (%s, %s, %s, %s)
		ON DUPLICATE KEY UPDATE id=%s
	"""
	query_args = (session_id, member_id, ip_address, running_time, session_id)
	cursor.execute(query, query_args)
	
	response.set_cookie('pass_hash', members_pass_hash)
	response.set_cookie('member_id', member_id)
	response.set_cookie('session_id', session_id)
	cursor.execute("""UPDATE """ + members_tablename + """ SET member_login_key=%s WHERE name=%s""", (session_id, username))
	response.set_cookie('logged_on_forum', True)
	return response

def forum_logout(request, response):
	db = DB()
	cursor = db.cursor
	sessions_tablename = db.get_tablename("sessions")
	cursor.execute("""DELETE IGNORE FROM """ + sessions_tablename + """ WHERE id='%s'""" % (request.session.session_key, ))
	response.set_cookie('logged_on_forum', False)
	response.set_cookie('pass_hash', False)
	response.set_cookie('member_id', 0)
	return response
