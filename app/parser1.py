import os
import random
import psycopg2
from psycopg2.extras import execute_values
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from slugify import slugify
base_url='https://rozetka.com.ua/headphones/c80027/'
urls=[]
types_ = 'extra'
response = HTMLSession()
for i in range(1,2):
    url = f'https://rozetka.com.ua/headphones/c80027/page={i};21078=tws-2-razdelno,vakuumnie,2726;21079=2731;21806=dlya-telefona/'
    html = response.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    contain = soup.find('rz-grid',class_="ng-star-inserted").find_all('li')
    for j in contain:
        try:
            a = j.find('a')['href']
        except:
            a = None
        urls.append(a)
id=0
count=0
args=[]
slug_check=[]
brands=['oppo','huawei','tecno','vivo','xiaomi','samsung','realme']
corpuses=['алюминий','пластик']
vids=['вкладыши','накладные']
descriptions = ['Все лучшее для пользователя собрано в этой маленькой компактной оболочке вакуумного типа. Наушники стали идеальным средством прослушивания музыки, осуществления голосовых вызовов, гейминга посредством применения мобильных устройств.',
                'Компактный зарядный кейс весом всего 45 граммов сочетает в себе миниатюрный, минималистический дизайн и батарею емкостью 400 mAh. Время работы таких компактных и одновременно мощных наушников составит до 5 часов без подзарядки и до 22 часов вместе с зарядным кейсом.',
                'Активное шумоподавление в наушниках отсекает до 97% посторонних нежелательных звуков в низкочастотном диапазоне, что подтверждено сертификатом UL, выданным независимой лабораторией Underwriters Laboratories, Inc.',
                'выделяется поддержкой современного стандарта подключения Bluetooth 5.2, временем работы до 24 часов (вместе с зарядным кейсом), а также дизайном полувкладышей, вобравшего в себя лучшие особенности наушников двух типов – вкладышей и внутриканальных.',
                'новые беспроводные наушники Huawei, доступные каждому. Модель ориентирована на покупателей, выбирающих устройство с оптимальным соотношением цена-качество, покупают первые TWS-наушники.',
                'выделяется поддержкой современного стандарта подключения Bluetooth 5.2, временем работы до 24 часов (вместе с зарядным кейсом), а также дизайном полувкладышей, вобравшего в себя лучшие особенности наушников двух типов – вкладышей и внутриканальных.',
                'Благодаря светодиодным индикаторам в зарядном устройстве никогда неожиданно не сядет батарейка! И вы всегда будете знать, когда заряд батареи почти исчерпан и пришло время для подзарядки.',
                'Беспроводные наушники нового поколения подключаются при помощи Bluetooth 5.0 и используют технологию TWS для первоклассного 3D стереозвука. Двойной микрофон еще лучше справляется с шумоподавлением. Наушники выполнены в компактном и ультра лёгком корпусе, что позволяет им крепко держаться в ушах даже при занятии спортом. Наушники так же могут использоваться по отдельности как беспроводная гарнитура, когда вы за рулем.',
                'Технология JBL Deep Bass Sound До 6 часов оспроизведения плюс 20 в чехле с возможностью быстрой зарядки Стереозвонки в режиме «hands-free»',
                'Неисчерпаемый источник энергии для любителей музыки. обеспечивают до 24 часов воспроизведения любимых музыки и видео.']
dop_infa=['наушники типа -C EO-IC100','есть 2 режима записи наушника','идёт в комплект чистка для наушников']
for i in urls:
    try:
        id+=1
        if id==81:
            5+'k'
        html = response.get(i).text
        soup = BeautifulSoup(html, 'html.parser')
        name_ = soup.find('h1',class_='product__title').text[11:]
        slug_ = slugify(name_)
        brand_ = brands[random.randint(0,6)]
        if slug_ not in slug_check:
            slug_check.append(slug_)
        else:
            slug_ += f'{id}'
        pricef=soup.find('p',class_="product-price__big").text
        pricef=pricef.replace("₴",'')
        if not len(pricef)<=5:
            1+'5'
        if len(pricef)==5:
            pricef = pricef.replace(pricef[1], '')
        price_ = int(pricef)*308
        photes = soup.find('ul', class_="simple-slider__list ng-star-inserted")
        photo_1_ = photes.find('li').find('img')['src']
        photo_2_ = photes.find('li').find_next('li').find('img')['src']
        weight_ = str(random.randint(30,60))+' г'
        corpus_= corpuses[random.randint(0,1)]
        description_= descriptions[random.randint(0,9)]
        dop_infa_ = dop_infa[random.randint(0,2)]
        vid_=vids[random.randint(0,1)]
        i+='characteristics/'
        html = response.get(i).text
        soup = BeautifulSoup(html, 'html.parser')
        list_towar=soup.find('dl',class_="characteristics-full__list").find_all('div')
        for j in list_towar:
            if j.find('dt',class_="characteristics-full__label").text == 'Тип навушників':
                type_ = j.find('dd').text
            elif j.find('dt',class_="characteristics-full__label").text == 'Тип підключення':
                type_connection_ = j.find('dd').text.replace('Бездротові','Бездротовые')
            elif j.find('dt',class_="characteristics-full__label").text == "Інтерфейс під'єднання":
                enterface_ = j.find('dd').text + ' с микрофоном'
            elif j.find('dt',class_="characteristics-full__label").text == 'Колір':
                color_ = j.find('dd').text
            elif j.find('dt',class_="characteristics-full__label").text == 'Наявність активного шумозаглушення':
                anti_shum_ = 'с активным шумоподавлением'
            elif j.find('dt',class_="characteristics-full__label").text == 'Матеріал амбушур':
                ambushur_ = 'Силекон'
            elif j.find('dt',class_="characteristics-full__label").text == 'Тип випромінювача':
                type_vipe_ = 'Динамический'
            elif j.find('dt',class_="characteristics-full__label").text == "Рік випуску моделі":
                date_create_ = j.find('dd').text
            elif j.find('dt',class_="characteristics-full__label").text == 'Країна-виробник товару':
                country_ = j.find('dd').text
            elif j.find('dt',class_="characteristics-full__label").text == 'Гарантія':
                garantee_ = j.find('dd').text.replace('місяці','мес:')
                garantee_ = garantee_.replace('в','')
            elif j.find('dt',class_="characteristics-full__label").text == "Час роботи, год":
                time_work_ = j.find('dd').text+f' ч с аккамулятором'
        count_ = random.randint(25,50)
        rating_ = 5
    except:
        id -= 1
        count += 1
    else:
        try:
            args.append((id,name_, slug_, brand_,price_,photo_1_,photo_2_,type_,type_connection_,enterface_,color_,anti_shum_,ambushur_,type_vipe_,date_create_,country_,garantee_,time_work_,corpus_,description_,weight_,vid_,dop_infa_,types_,count_,rating_))
        except:
            id-=1
            count+=1
        else:
            print(id)
print(count)
con = psycopg2.connect(
            database=os.environ.get('DB_NAME'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASS'),
            host=os.environ.get('DB_HOST')
        )
cur = con.cursor()
execute_values(cur,"INSERT INTO phones_airpods (id,name, slug, brand,price,photo1,photo2,type,type_connection,enterface,color,anti_shum,ambushur,type_vipe,date_create,country,garantee,time_work,corpus,description,weight,vid,dop_infa,types,count,rating) VALUES %s",args)
con.commit()
con.close()