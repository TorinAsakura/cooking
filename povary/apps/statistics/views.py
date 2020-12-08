# -*- coding: utf-8 -*-
import pymongo
# from comments.models import Comment


def comments_coll():
	connection = pymongo.Connection()
	statistics_db = connection.statistic
	comments = statistics_db.comments
	return comments

def comment_added(comment):
	comments = comments_coll()
	obj_model = comment.content_type.model_class()
	commented_object = obj_model.objects.get(id=comment.object_id)
	comment_info = {
		"comment_id": comment.id,
		"author": comment.author.username if comment.author else "Anonymous",
		"created": comment.created,
		"ip_addr": comment.ip_addr,
		"content_type": comment.content_type.id,
		"content_type_id": comment.content_type_id,
		"published": comment.published,
		"action": "created",
	}
	object_id = comments.insert(comment_info)
	return object_id

def comment_changed(old_instance, new_instance):
	field_list = old_instance._meta.get_all_field_names()
	# We can't save RelatedManager into mongodb, so just fuck it out
	field_list.remove('answers')
	changed_fields = {}
	for field in field_list:
		old_value = getattr(old_instance, field)
		new_value = getattr(new_instance, field)
		if old_value != new_value:
			changed_fields[field] = {
				"old_value": old_value,
				"new_value": new_value
			}
	if len(changed_fields) < 1:
		return False
	comment_info = {
		"comment_id": new_instance.id,
		"action": "changed",
		"changed_fields": changed_fields
	}
	comments = comments_coll()
	object_id = comments.insert(comment_info)
	return object_id



