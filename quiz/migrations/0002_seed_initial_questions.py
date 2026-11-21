from django.db import migrations


def seed_questions(apps, schema_editor):
    Question = apps.get_model("quiz", "Question")
    database = schema_editor.connection.alias
    questions = [
        {
            "question": "What language is Django written in?",
            "option1": "C++",
            "option2": "Python",
            "option3": "Javascripts",
            "option4": "Ruby",
            "answer": "Python",
        },
        {
            "question": "Which planet is the biggest in our Galaxy",
            "option1": "Jupiter",
            "option2": "UY Scuti",
            "option3": "Stephenson B-18",
            "option4": "Uranus",
            "answer": "Stephenson B-18",
        },
    ]

    for question in questions:
        Question.objects.using(database).get_or_create(
            question=question["question"],
            defaults=question,
        )


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_questions, migrations.RunPython.noop),
    ]
