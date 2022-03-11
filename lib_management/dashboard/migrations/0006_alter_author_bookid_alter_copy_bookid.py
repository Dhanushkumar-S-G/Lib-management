# Generated by Django 4.0.2 on 2022-02-21 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_book_picture_alter_issue_date_returned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bookid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to='dashboard.book'),
        ),
        migrations.AlterField(
            model_name='copy',
            name='bookid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_copies', to='dashboard.book'),
        ),
    ]
