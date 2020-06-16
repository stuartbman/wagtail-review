# Generated by Django 3.0.7 on 2020-06-16 11:58

from django.db import migrations


def populate_new_comment_field(apps, schema_editor):
    ReviewTaskState = apps.get_model('wagtail_review.ReviewTaskState')

    for task_state in ReviewTaskState.objects.only('review_comment'):
        task_state.comment = task_state.review_comment
        task_state.save(update_fields=['comment'])


def populate_old_comment_field(apps, schema_editor):
    ReviewTaskState = apps.get_model('wagtail_review.ReviewTaskState')

    for task_state in ReviewTaskState.objects.only('comment'):
        task_state.review_comment = task_state.comment
        task_state.save(update_fields=['review_comment'])


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0051_taskstate_comment'),
        ('wagtail_review', '0012_rename_comment_to_review_comment'),
    ]

    operations = [
        migrations.RunPython(populate_new_comment_field, populate_old_comment_field),
    ]
