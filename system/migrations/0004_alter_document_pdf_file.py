# Generated by Django 5.1.1 on 2024-09-07 15:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("system", "0003_alter_document_pdf_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="pdf_file",
            field=models.FileField(upload_to="pdfs/"),
        ),
    ]
