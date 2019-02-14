# Generated by Django 2.1.5 on 2019-02-08 22:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("edu", "0003_auto_20190209_0156"), ("works", "0001_initial")]

    operations = [
        migrations.RenameField(
            model_name="report", old_name="student_id", new_name="student"
        ),
        migrations.RenameField(
            model_name="report", old_name="task_id", new_name="task"
        ),
        migrations.RenameField(
            model_name="task", old_name="subject_id", new_name="subject"
        ),
        migrations.RemoveField(model_name="task", name="group_id"),
        migrations.AddField(
            model_name="task",
            name="group_id",
            field=models.ManyToManyField(related_name="task", to="edu.StudentGroup"),
        ),
    ]
