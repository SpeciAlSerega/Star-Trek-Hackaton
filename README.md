# Star Trek
# Pet`s Planet

Открытая база данных  животных, без владельцев или «потеряшек», которых нужно отдать в ближайшие приюты.
Также отработка маршрутных линий до ветеринарных клиник, в которых могут принять израненных или изнеможенных питомцев.
Сайт будет включать в себя интересные факты, новости о мире животных, свайпсистему фотографий и местонахождения зверушек, как в Facebook, включая трекинг, где люди в свободном доступе могут отдать питомцев и любителям животных, которые давно мечтали ими обзавестись.

# Задачи
- Да, поднимаем сайт 
- Прикрепим карты 
- Создадим внутри множество БД для приютов(Если успеем конечно)
- Свайп ленту с новостями

http://w3.insoft.ru/resheniya-i-uslu/municipalitety/ais-uchet-zhivotn/

https://pet911.ru/

Можно умные слова с описаний предметной области подобрать: функционал и прочее

# Установка

```
pip istall django
virtualenv venv --python=python3.8
source venv/bin/activate    
python3 manage.py makemigrations app_pet 
python3 manage.py migrate   
python manage.py runserver 0.0.0.0:8888  
```

## Для загрузки единожды выполняем команду
`python3 manage.py shell` , затем копируем прямо в консоль данный скрипт:


```
from openpyxl import load_workbook
wb = load_workbook('./Data set.xlsx')
sheet = wb.get_sheet_by_name('Лист')
from app_pet.models import *
def aaa(az):
	if (az!=None and az!="Null"):
		return az
	else: 
		return ""
z=0

def intornull(az):
	try:
		m = int(az)
		return m
	except:
		return 0 

for row in range(3,244):
	try:
		a  = PetModel(card_pet=aaa(sheet.cell(row=row, column=2).value), type_pet=aaa(sheet.cell(row=row, column=3).value), age=intornull(sheet.cell(row=row, column=4).value), weight = intornull(sheet.cell(row=row, column=5).value), nickname=aaa(sheet.cell(row=row, column=6).value), sex= aaa(sheet.cell(row=row, column=7).value), breed_of_dog=aaa(sheet.cell(row=row, column=8).value), color=aaa(sheet.cell(row=row, column=9).value), fur=aaa(sheet.cell(row=row, column=10).value), ears=aaa(sheet.cell(row=row, column=11).value), tail = aaa(sheet.cell(row=row, column=12).value), size=aaa(sheet.cell(row=row, column=13).value), special_signs = aaa(sheet.cell(row=row, column=14).value), aviary_number=intornull(sheet.cell(row=row, column=15).value), identification_mark=intornull(sheet.cell(row=row, column=16).value), sterilization_date=aaa(sheet.cell(row=row, column=17).value), veterinarian=aaa(sheet.cell(row=row, column=18).value), socialized=aaa(sheet.cell(row=row, column=19).value), act_work_order=aaa(sheet.cell(row=row, column=20).value), data_work_order=aaa(sheet.cell(row=row, column=21).value), capture_act=aaa(sheet.cell(row=row, column=23).value), catching_address=aaa(sheet.cell(row=row, column=24).value), date_admission = aaa(sheet.cell(row=row, column=28).value), act_admission=aaa(sheet.cell(row=row, column=29).value), date_leaving= aaa(sheet.cell(row=row, column=30).value), reason_leaving = aaa(sheet.cell(row=row, column=31).value), act_leaving= aaa(sheet.cell(row=row, column=32).value), date_inspection = aaa(sheet.cell(row=row, column=45).value), anamnesis = aaa(sheet.cell(row=row, column=46).value))
		a.save()
	except:
		print(z)
	z+=1
	
  ```
