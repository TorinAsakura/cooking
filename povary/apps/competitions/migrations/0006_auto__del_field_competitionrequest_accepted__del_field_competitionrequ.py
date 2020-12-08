# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'CompetitionRequest.accepted'
        db.delete_column('competitions_competitionrequest', 'accepted')

        # Deleting field 'CompetitionRequest.recipe'
        db.delete_column('competitions_competitionrequest', 'recipe_id')

        # Adding field 'CompetitionRequest.title'
        db.add_column('competitions_competitionrequest', 'title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'CompetitionRequest.image'
        db.add_column('competitions_competitionrequest', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'CompetitionRequest.description'
        db.add_column('competitions_competitionrequest', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'CompetitionRequest.body'
        db.add_column('competitions_competitionrequest', 'body',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'CompetitionRequest.image1'
        db.add_column('competitions_competitionrequest', 'image1',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CompetitionRequest.image2'
        db.add_column('competitions_competitionrequest', 'image2',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CompetitionRequest.image3'
        db.add_column('competitions_competitionrequest', 'image3',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CompetitionRequest.image4'
        db.add_column('competitions_competitionrequest', 'image4',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CompetitionRequest.image5'
        db.add_column('competitions_competitionrequest', 'image5',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CompetitionRequest.show_till_voting_start'
        db.add_column('competitions_competitionrequest', 'show_till_voting_start',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'CompetitionRequest.show_my_name'
        db.add_column('competitions_competitionrequest', 'show_my_name',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'CompetitionRequest.author'
        db.add_column('competitions_competitionrequest', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'CompetitionRequest.ip_addr'
        db.add_column('competitions_competitionrequest', 'ip_addr',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CompetitionRequest.status'
        db.add_column('competitions_competitionrequest', 'status',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'CompetitionRequest.accepted'
        db.add_column('competitions_competitionrequest', 'accepted',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'CompetitionRequest.recipe'
        raise RuntimeError("Cannot reverse this migration. 'CompetitionRequest.recipe' and its values cannot be restored.")
        # Deleting field 'CompetitionRequest.title'
        db.delete_column('competitions_competitionrequest', 'title')

        # Deleting field 'CompetitionRequest.image'
        db.delete_column('competitions_competitionrequest', 'image')

        # Deleting field 'CompetitionRequest.description'
        db.delete_column('competitions_competitionrequest', 'description')

        # Deleting field 'CompetitionRequest.body'
        db.delete_column('competitions_competitionrequest', 'body')

        # Deleting field 'CompetitionRequest.image1'
        db.delete_column('competitions_competitionrequest', 'image1')

        # Deleting field 'CompetitionRequest.image2'
        db.delete_column('competitions_competitionrequest', 'image2')

        # Deleting field 'CompetitionRequest.image3'
        db.delete_column('competitions_competitionrequest', 'image3')

        # Deleting field 'CompetitionRequest.image4'
        db.delete_column('competitions_competitionrequest', 'image4')

        # Deleting field 'CompetitionRequest.image5'
        db.delete_column('competitions_competitionrequest', 'image5')

        # Deleting field 'CompetitionRequest.show_till_voting_start'
        db.delete_column('competitions_competitionrequest', 'show_till_voting_start')

        # Deleting field 'CompetitionRequest.show_my_name'
        db.delete_column('competitions_competitionrequest', 'show_my_name')

        # Deleting field 'CompetitionRequest.author'
        db.delete_column('competitions_competitionrequest', 'author_id')

        # Deleting field 'CompetitionRequest.ip_addr'
        db.delete_column('competitions_competitionrequest', 'ip_addr')

        # Deleting field 'CompetitionRequest.status'
        db.delete_column('competitions_competitionrequest', 'status')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'competitions.competition': {
            'Meta': {'object_name': 'Competition'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'competitions'", 'to': "orm['auth.User']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'competitions'", 'to': "orm['competitions.CompetitionCategory']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prizes': ('django.db.models.fields.TextField', [], {}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'terms': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'visits_num': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'voting_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'voting_end': ('django.db.models.fields.DateTimeField', [], {}),
            'voting_start': ('django.db.models.fields.DateTimeField', [], {})
        },
        'competitions.competitioncategory': {
            'Meta': {'object_name': 'CompetitionCategory'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'competitions.competitionrequest': {
            'Meta': {'object_name': 'CompetitionRequest'},
            'adding_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'competition': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'competition_requests'", 'to': "orm['competitions.Competition']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image4': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image5': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ip_addr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'place_number': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255'}),
            'show_my_name': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_till_voting_start': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'competitions.competitionvote': {
            'Meta': {'object_name': 'CompetitionVote'},
            'competition_request': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'votes'", 'to': "orm['competitions.CompetitionRequest']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'competition_votes'", 'to': "orm['auth.User']"})
        },
        'competitions.mainpagecompetition': {
            'Meta': {'object_name': 'MainPageCompetition'},
            'competition': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mainpage_competition'", 'to': "orm['competitions.Competition']"}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mainpage_competition'", 'to': "orm['gallery.Gallery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'gallery.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'visits_num': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['competitions']