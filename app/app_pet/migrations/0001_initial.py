

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('Telegram', models.CharField(blank=True, max_length=100)),
                ('mail', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('pasport', models.CharField(blank=True, max_length=100)),
                ('snils', models.CharField(blank=True, max_length=100)),
                ('inn', models.CharField(blank=True, max_length=100)),
                ('organization1', models.CharField(blank=True, max_length=100)),
                ('ownership', models.CharField(blank=True, choices=[('M', 'управление'), ('U', 'пользователь')], max_length=100)),
                ('natural_legal', models.CharField(choices=[('n', 'физическое'), ('l', 'юридическое')], max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prefecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('departament', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_pet.departament')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeVaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('prefecture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_pet.prefecture')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('body', models.TextField(blank=True, db_index=True)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='app_pet.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='PetModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_pet', models.CharField(default='', max_length=15, unique=True)),
                ('type_pet', models.CharField(choices=[('d', 'кошка'), ('c', 'собака')], default='d', max_length=1)),
                ('age', models.IntegerField(blank=True)),
                ('weight', models.IntegerField(blank=True)),
                ('nickname', models.CharField(blank=True, default='', max_length=30)),
                ('sex', models.CharField(choices=[('m', 'мужской'), ('f', 'женский')], default='', max_length=30)),
                ('breed_of_dog', models.CharField(blank=True, default='', max_length=30)),
                ('color', models.CharField(blank=True, choices=[('b', 'черный'), ('w', 'белый'), ('b-w', 'черно-белый')], default='', max_length=30)),
                ('fur', models.CharField(blank=True, choices=[('s', 'короткая'), ('l', 'длинная'), ('n', 'обычная')], default='', max_length=30)),
                ('ears', models.CharField(blank=True, choices=[('s', 'стоячие'), ('s-s', 'полустоячие'), ('h', 'висячие')], default='', max_length=30)),
                ('tail', models.CharField(blank=True, choices=[('n', 'обычный'), ('c', 'крючком'), ('s', 'саблевидный')], default='', max_length=30)),
                ('size', models.CharField(blank=True, choices=[('b', 'большой'), ('s', 'маленький'), ('m', 'средний')], default='', max_length=30)),
                ('special_signs', models.CharField(blank=True, default='', max_length=30)),
                ('aviary_number', models.IntegerField(blank=True)),
                ('identification_mark', models.IntegerField(blank=True)),
                ('sterilization_date', models.CharField(blank=True, default='', max_length=30)),
                ('veterinarian', models.CharField(blank=True, default='', max_length=30)),
                ('socialized', models.CharField(blank=True, choices=[('y', 'да'), ('n', 'нет')], default='', max_length=30)),
                ('act_work_order', models.CharField(blank=True, default='', max_length=30)),
                ('data_work_order', models.CharField(blank=True, default='', max_length=30)),
                ('capture_act', models.CharField(blank=True, default='', max_length=30)),
                ('catching_address', models.CharField(blank=True, default='', max_length=30)),
                ('date_admission', models.CharField(blank=True, default='', max_length=30)),
                ('act_admission', models.CharField(blank=True, default='', max_length=30)),
                ('date_leaving', models.CharField(blank=True, default='', max_length=30)),
                ('reason_leaving', models.CharField(blank=True, default='', max_length=30)),
                ('act_leaving', models.CharField(blank=True, default='', max_length=30)),
                ('date_inspection', models.CharField(blank=True, default='', max_length=30)),
                ('anamnesis', models.CharField(blank=True, default='', max_length=30)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('shelter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_pet.shelter')),
                ('typevaccine', models.ManyToManyField(blank=True, null=True, to='app_pet.TypeVaccine')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('batch_number', models.CharField(max_length=64)),
                ('petmodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pet.petmodel')),
                ('typevaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pet.typevaccine')),
            ],
        ),
    ]
