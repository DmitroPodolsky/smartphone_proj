import random
import psycopg2
from psycopg2.extras import execute_values
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from slugify import slugify
import os

base_url = 'https://www.mediapark.uz'
urls = []
response = HTMLSession()
for i in range(1, 8):
    url = f'https://www.mediapark.uz/products/category/40?page={i}'
    html = response.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    contain = soup.find_all('div', class_="car-block swiper-slide")
    for j in contain:
        a = j.find('a', class_="product_list_img slide")['href']
        urls.append(base_url + a)
id = 0
count = 0
args = []
slug_check = []
for i in urls:
    try:
        id += 1
        html = response.get(i).text
        soup = BeautifulSoup(html, 'html.parser')
        name_ = soup.find('div', class_="Catalog-information-right-block-left-center-info").find_next('h4').text
        a = soup.find('div', class_="Catalog-information-right-block-right-main").find_next('span').text
        b = a.replace('сум', '')
        price_ = b.replace(' ', '')
        description_ = soup.find('div', id='tab1').find_next('span').find_next('span').text
        photo1_ = base_url + soup.find('div', class_="main").find_next('img', class_='zoom')['src']
        photo2_ = base_url + soup.find('div', class_='slider-nav2-start').find_next('img').find_next('img')['src']
        photo3_ = base_url + \
                  soup.find('div', class_='slider-nav2-start').find_next('img').find_next('img').find_next('img')['src']
        if "https://www.mediapark.uz/themes/mpark/icons/imgs/telegram 1.svg" == photo3_ or "https://www.mediapark.uz/themes/mpark/icons/imgs/telegram 1.svg" == photo2_:
            1 + 'a'
        tr = soup.find('div', class_="table-responsive").find_all('tr')
        for j in tr:
            if j.find('td').text == 'Версия ОС':
                Version_OS_ = j.find('td').find_next('td').text
                if 0 == len(Version_OS_) or 1 == len(Version_OS_):
                    Version_OS_ = 'Hangrom:12'
            if j.find('td').text == 'Корпус':
                corpus_ = j.find('td').find_next('td').text
                if 'алюминий' in corpus_:
                    corpus_ = 'алюминий'
                if 'стекло' in corpus_:
                    corpus_ = 'стекло'
                if 'Пластик' in corpus_:
                    corpus_ = 'пластик'
                if 'классический' in corpus_:
                    corpus_ = 'алюминий'
                if 1 == len(corpus_):
                    corpus_ = 'пластик'
                if 0 == len(corpus_) or 1 == len(corpus_):
                    corpus_ = 'алюминий'
            if j.find('td').text == 'Тип SIM-карты':
                sim_card_ = j.find('td').find_next('td').text
                if 0 == len(sim_card_) or '-' == sim_card_:
                    sim_card_ = '2'
            if j.find('td').text == 'Размеры':
                size_ = j.find('td').find_next('td').text
                if 0 == len(size_) or 1 == len(size_):
                    size_ = 'высота 146.7 мм,ширина 71.5 мм, глубина 7.80 мм'
            if j.find('td').text == 'Вес':
                weight_ = j.find('td').find_next('td').text
                if 0 == len(weight_) or 1 == len(weight_):
                    weight_ = '189 г'
            if j.find('td').text == 'Тип экрана':
                display_type_ = j.find('td').find_next('td').text
                if 0 == len(display_type_) or 1 == len(display_type_):
                    display_type_ = 'Super AMOLED'
            if j.find('td').text == 'Диагональ':
                diagonale_ = j.find('td').find_next('td').text
                if 0 == len(diagonale_) or 1 == len(diagonale_):
                    diagonale_ = '6.5'
            if j.find('td').text == 'Разрешение экрана':
                allow_display_ = j.find('td').find_next('td').text
                if 0 == len(allow_display_) or 1 == len(allow_display_):
                    allow_display_ = '(2400x1080), Full HD'
            if j.find('td').text == 'Фотокамера':
                photo_kamera_ = j.find('td').find_next('td').text
                if 0 == len(photo_kamera_) or 1 == len(photo_kamera_):
                    photo_kamera_ = '16'
            if j.find('td').text == 'Фронтальная камера':
                front_kamera_ = j.find('td').find_next('td').text
                front_kamera_ = front_kamera_.replace(' МП', '')
                if len(front_kamera_) > 2:
                    front_kamera_ = '16'
                if 0 == len(front_kamera_) or '-' == front_kamera_:
                    front_kamera_ = '16'
            if j.find('td').text == 'Выход на наушники':
                audio_ = j.find('td').find_next('td').text
                if 0 == len(audio_) or 1 == len(audio_):
                    audio_ = 'mini jack 3.5 mm'
                audio1_ = 'MP3, AAC, WAV, WMA, FM-радио'
            if j.find('td').text == 'Стандарт':
                standart_ = j.find('td').find_next('td').text
                if 0 == len(standart_) or 1 == len(standart_):
                    standart_ = 'IEEE 802.11 a/b/g/n/ac'
            if j.find('td').text == 'Интерфейсы':
                Interface_ = j.find('td').find_next('td').text
                if 0 == len(Interface_) or 1 == len(Interface_):
                    Interface_ = 'NFC, Bluetooth, Wi-Fi'
            if j.find('td').text == 'Процессор':
                prochessor_ = j.find('td').find_next('td').text
                if 0 == len(prochessor_) or 1 == len(prochessor_):
                    prochessor_ = 'Mali-G68 MC4'
            if j.find('td').text == 'Количество ядер':
                a = [4, 6, 8]
                yadra_ = a[random.randint(0, 2)]
            if j.find('td').text == 'Объем встроенной памяти':
                giga_vstoeno_ = j.find('td').find_next('td').text
                if 0 == len(giga_vstoeno_) or '-' == giga_vstoeno_:
                    giga_vstoeno_ = '64'
                giga_vstoeno_ = giga_vstoeno_.replace(' ГБ', '')
                giga_vstoeno_ = giga_vstoeno_.replace('ГБ', '')
                if ' U<' in giga_vstoeno_:
                    giga_vstoeno_ = giga_vstoeno_.replace(' U<', '')
            if j.find('td').text == 'Объем оперативной памяти':
                giga_operate_ = j.find('td').find_next('td').text
                giga_operate_ = giga_operate_.replace(' ГБ', '')
                if 0 == len(giga_operate_) or '-' == giga_operate_ or 1 == len(giga_operate_):
                    giga_operate_ = '16'
                if ' U<' in giga_operate_:
                    giga_operate_ = giga_operate_.replace(' U<', '')
            if j.find('td').text == 'Слот для карт памяти':
                sloy_card_ = j.find('td').find_next('td').text
                if 0 == len(sloy_card_) or 1 == len(sloy_card_):
                    sloy_card_ = 'есть!'
            if j.find('td').text == 'Аккумулятор':
                accumulator_ = j.find('td').find_next('td').text
                accumulator_ = accumulator_[:4]
                if accumulator_ == 'встр':
                    accumulator_ = '5000'
                if 0 == len(accumulator_) or 1 == len(accumulator_):
                    accumulator_ = '5000'
            if j.find('td').text == 'Дополнительная информация':
                dop_infa_ = j.find('td').find_next('td').text
                if 0 == len(dop_infa_) or 1 == len(dop_infa_):
                    dop_infa_ = 'сканер отпечатка пальца сбоку'
        slug_ = slugify(name_)
        brand_ = slug_.split('-')[1]
        count_ = random.randint(25, 50)
        types_ = 'smartphone'
        rating_ = 5
        if slug_ not in slug_check:
            slug_check.append(slug_)
        else:
            slug_ += f'{id}'
    except:
        id -= 1
        count += 1
    else:
        try:
            args.append((id, name_, price_, photo1_, photo2_, photo3_, description_, Version_OS_, corpus_, sim_card_,
                         size_, weight_, display_type_, diagonale_, allow_display_, photo_kamera_, front_kamera_,
                         audio_, standart_, Interface_, prochessor_, yadra_, giga_vstoeno_, giga_operate_, sloy_card_,
                         accumulator_, dop_infa_, slug_, brand_, audio1_, types_, count_, rating_))
        except:
            id -= 1
            count += 1
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
execute_values(cur,
               "INSERT INTO phones_phones (id, name, price,photo1,photo2,photo3,description,version_os, corpus, sim_card, size, weight, display_type, diagonale, allow_display,photo_kamera, front_kamera, headphone_jack, standart,interface, prochessor,yadra, giga_vstoeno, giga_operate,sloy_card, accumulator, dop_infa,slug,brand,audio,types,count,rating) VALUES %s",
               args)
con.commit()
con.close()
