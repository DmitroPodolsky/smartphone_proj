#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import random
import psycopg2
from psycopg2.extras import execute_values
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from slugify import slugify

'''base_url='https://rozetka.com.ua/headphones/c80027/'
#urls=[]
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
urls=['https://rozetka.com.ua/ua/defunc_d4271m/p296932928/', None, 'https://rozetka.com.ua/ua/defunc_d4271m/p296932928/', 'https://rozetka.com.ua/ua/defunc_d4274m/p297022453/', 'https://rozetka.com.ua/ua/defunc_d4276m/p320436982/', 'https://rozetka.com.ua/ua/defunc_d4275m/p320436985/', 'https://rozetka.com.ua/ua/defunc_d4273m/p320432248/', 'https://rozetka.com.ua/ua/defunc_d4272m/p296988478/', 'https://rozetka.com.ua/ua/logitech_985_001182/p366117102/', 'https://rozetka.com.ua/ua/logitech_985_001182/p366117102/', 'https://rozetka.com.ua/ua/logitech_985_001183/p366117165/', 'https://rozetka.com.ua/ua/sony_wfc500d_ce7/p335691736/', None, 'https://rozetka.com.ua/ua/defunc_d4214/p267878356/', None, 'https://rozetka.com.ua/ua/defunc_d4211/p267873376/', 'https://rozetka.com.ua/ua/defunc_d4214/p267878356/', 'https://rozetka.com.ua/ua/defunc_d4216/p267878401/', 'https://rozetka.com.ua/ua/defunc_d4215/p267878386/', 'https://rozetka.com.ua/ua/defunc_d4213/p267878346/', 'https://rozetka.com.ua/ua/defunc_d4212/p267878191/', 'https://rozetka.com.ua/ua/samsung_sm_r510nlvasek/p349736922/', None, 'https://rozetka.com.ua/ua/samsung_sm_r510nlvasek/p349736922/', 'https://rozetka.com.ua/ua/samsung_sm_r510nzwasek/p349743921/', 'https://rozetka.com.ua/ua/samsung_sm_r180nznasek/p238811347/', 'https://rozetka.com.ua/ua/samsung_sm_r180nzkasek/p238792495/', 'https://rozetka.com.ua/ua/samsung_sm_r180nznasek/p238811347/', 'https://rozetka.com.ua/ua/samsung_sm_r180nzwasek/p238811953/', 'https://rozetka.com.ua/ua/apple-pro-with-magsafe-charging-case-2022-2-e-pokolenie/p352490850/', 'https://rozetka.com.ua/ua/huawei_55034952/p350661462/', 'https://rozetka.com.ua/ua/defunc-d4311/p356138040/', None, 'https://rozetka.com.ua/ua/defunc-d4311/p356138040/', 'https://rozetka.com.ua/ua/defunc-d4314/p362376219/', 'https://rozetka.com.ua/ua/defunc-d4316/p362376222/', 'https://rozetka.com.ua/ua/defunc-d4315/p362376231/', 'https://rozetka.com.ua/ua/defunc-d4313/p362376228/', 'https://rozetka.com.ua/ua/defunc-d4312/p356142477/', 'https://rozetka.com.ua/ua/apple-mpny3ty-a/p353550168/', 'https://rozetka.com.ua/ua/huawei_55036650/p363258609/', 'https://rozetka.com.ua/ua/huawei_55036650/p363258609/', 'https://rozetka.com.ua/ua/huawei_55036649/p363258612/', 'https://rozetka.com.ua/ua/huawei_55036651/p363258606/', 'https://rozetka.com.ua/ua/xiaomi_6957141405505/p142831103/', 'https://rozetka.com.ua/ua/jbl_jblwbudsblk/p367813299/', 'https://rozetka.com.ua/ua/jbl_jblwbudsblk/p367813299/', 'https://rozetka.com.ua/ua/jbl_jblwbudswht/p367813302/', 'https://rozetka.com.ua/ua/xiaomi-bhr5489gl/p363180225/', 'https://rozetka.com.ua/ua/beatbox_bbppro1wcb/p301052013/', 'https://rozetka.com.ua/ua/beatbox_bbppro1wcb/p301052013/', 'https://rozetka.com.ua/ua/beatbox_bbppro1wcbr/p349601304/', 'https://rozetka.com.ua/ua/beatbox_bbppro1wcw/p301055198/', 'https://rozetka.com.ua/ua/beatbox_bbppro1wcwr/p349606683/', 'https://rozetka.com.ua/ua/samsung_sm_r177nzwasek/p313512175/', 'https://rozetka.com.ua/ua/samsung_sm_r177nzkasek/p313489399/', 'https://rozetka.com.ua/ua/samsung_sm_r177nlvasek/p313512172/', 'https://rozetka.com.ua/ua/samsung_sm_r177nzgasek/p313512166/', 'https://rozetka.com.ua/ua/samsung_sm_r177nzwasek/p313512175/', 'https://rozetka.com.ua/ua/jbl-jblwflexblk/p367908939/', 'https://rozetka.com.ua/ua/jbl-jblwflexblk/p367908939/', 'https://rozetka.com.ua/ua/jbl-jblwflexwht/p367909464/', 'https://rozetka.com.ua/ua/jbl_jblwbeamblk/p367813344/', 'https://rozetka.com.ua/ua/jbl_jblwbeamblk/p367813344/', 'https://rozetka.com.ua/ua/jbl_jblwbeamwht/p367813347/', 'https://rozetka.com.ua/ua/beatbox_bbpair2wcb/p301066823/', 'https://rozetka.com.ua/ua/beatbox_bbpair2wcb/p301066823/', 'https://rozetka.com.ua/ua/beatbox_bbpair2wcbr/p349606686/', 'https://rozetka.com.ua/ua/beatbox_bbpair2wcw/p301097733/', 'https://rozetka.com.ua/ua/beatbox_bbpair2wcwr/p349606689/', 'https://rozetka.com.ua/ua/anker_a3952gq1_a3952hq1/p337209058/', None, 'https://rozetka.com.ua/ua/anker_a3952ga1/p337209061/', 'https://rozetka.com.ua/ua/anker_a3952gq1_a3952hq1/p337209058/', 'https://rozetka.com.ua/ua/358042887/p358042887/', 'https://rozetka.com.ua/ua/oppo_enco_air_2_w13_ete11_blue/p344376319/', 'https://rozetka.com.ua/ua/sony-wic100b-ce7/p359748258/', 'https://rozetka.com.ua/ua/sony-wic100b-ce7/p359748258/', 'https://rozetka.com.ua/ua/sony-wic100l-ce7/p359748273/', 'https://rozetka.com.ua/ua/sony-wic100w-ce7/p359748267/', 'https://rozetka.com.ua/ua/pixus_alien/p335900782/', 'https://rozetka.com.ua/ua/sennheiser_509180/p345724510/', 'https://rozetka.com.ua/ua/sennheiser_509180/p345724510/', 'https://rozetka.com.ua/ua/sennheiser_700074/p345724537/', 'https://rozetka.com.ua/ua/sennheiser_509181/p345728749/', 'https://rozetka.com.ua/ua/marshall_1005964/p348792777/', 'https://rozetka.com.ua/ua/gelius_2099900822988/p268358846/', 'https://rozetka.com.ua/ua/gelius_2099900822971/p268323221/', 'https://rozetka.com.ua/ua/gelius_2099900822988/p268358846/', 'https://rozetka.com.ua/ua/sony_wf_1000xm4s/p303539973/', 'https://rozetka.com.ua/ua/sony_wf_1000xm4b/p303537893/', 'https://rozetka.com.ua/ua/sony_wf_1000xm4s/p303539973/', 'https://rozetka.com.ua/ua/promate_freepods_3_black/p348277131/', 'https://rozetka.com.ua/ua/promate_freepods_3_black/p348277131/', 'https://rozetka.com.ua/ua/promate_freepods_3_blue/p348278271/', 'https://rozetka.com.ua/ua/promate_freepods_3_white/p348278268/', 'https://rozetka.com.ua/ua/oppo-enco-air2-pro-ete21-white/p354318834/', 'https://rozetka.com.ua/ua/panasonic_rz_b100wge_w/p305911783/', None, 'https://rozetka.com.ua/ua/panasonic_rz_b100wge_k/p305888628/', 'https://rozetka.com.ua/ua/panasonic_rz_b100wge_w/p305911783/', 'https://rozetka.com.ua/ua/anker_a3983h11/p352305267/', 'https://rozetka.com.ua/ua/promate_epic_black/p365481465/', None, 'https://rozetka.com.ua/ua/anker-a3936g11/p361730169/', None, 'https://rozetka.com.ua/ua/proda_prd_bt112wt/p346128400/', 'https://rozetka.com.ua/ua/philips_tat1207bk_00/p350246325/', 'https://rozetka.com.ua/ua/philips_tat1207bk_00/p350246325/', 'https://rozetka.com.ua/ua/philips_tat1207wt_00/p350246361/', 'https://rozetka.com.ua/ua/1more-960737/p362655270/', 'https://rozetka.com.ua/ua/1more-960737/p362655270/', 'https://rozetka.com.ua/ua/1more-960738/p362655663/', 'https://rozetka.com.ua/ua/oppo-enco-x2-ete01-black-oppo/p350853450/', 'https://rozetka.com.ua/ua/oppo-enco-x2-ete01-black-oppo/p350853450/', 'https://rozetka.com.ua/ua/oppo-enco-enco-x2-ete01-white-oppo/p350856918/', 'https://rozetka.com.ua/ua/canyon_cne_cbths3w/p268986696/', None, 'https://rozetka.com.ua/ua/canyon_cne_cbths3b/p268986656/', 'https://rozetka.com.ua/ua/canyon_cne_cbths3w/p268986696/', 'https://rozetka.com.ua/ua/beatbox_bbppro6b/p349384572/', 'https://rozetka.com.ua/ua/beatbox_bbppro6b/p349384572/', 'https://rozetka.com.ua/ua/beatbox_bbppro6bl/p349387062/', 'https://rozetka.com.ua/ua/beatbox_bbppro6o/p349387065/', 'https://rozetka.com.ua/ua/beatbox_bbppro6p/p349387068/', 'https://rozetka.com.ua/ua/beatbox_bbppro6w/p349387071/', 'https://rozetka.com.ua/ua/anker-a3961g91/p361727706/', None, 'https://rozetka.com.ua/ua/xiaomi-t10probk/p326159293/', 'https://rozetka.com.ua/ua/beatbox_bbppromw/p349387122/', 'https://rozetka.com.ua/ua/358042884/p358042884/', 'https://rozetka.com.ua/ua/358042881/p358042881/', 'https://rozetka.com.ua/ua/358042884/p358042884/', 'https://rozetka.com.ua/ua/defunc_d4241/p286060278/', None, 'https://rozetka.com.ua/ua/358042893/p358042893/', 'https://rozetka.com.ua/ua/358042890/p358042890/', 'https://rozetka.com.ua/ua/358042893/p358042893/', 'https://rozetka.com.ua/ua/358042896/p358042896/', 'https://rozetka.com.ua/ua/358042899/p358042899/', 'https://rozetka.com.ua/ua/xiaomi_897741/p362800596/', 'https://rozetka.com.ua/ua/anker-a3961g21/p361727565/', None, 'https://rozetka.com.ua/ua/ergo_bs_740w/p363258618/', 'https://rozetka.com.ua/ua/ergo_bs_740k/p363258615/', 'https://rozetka.com.ua/ua/ergo_bs_740w/p363258618/', 'https://rozetka.com.ua/ua/anker-a3936g21/p361731012/', None, 'https://rozetka.com.ua/ua/pixus_storm/p335900980/', 'https://rozetka.com.ua/ua/sennheiser_509247/p345733168/', 'https://rozetka.com.ua/ua/baseus_ngtw030102/p367382691/', 'https://rozetka.com.ua/ua/x_digital_hbs_110k/p363481464/', None, 'https://rozetka.com.ua/ua/x_digital_hbs_110k/p363481464/', 'https://rozetka.com.ua/ua/x_digital_hbs_110w/p363481467/', 'https://rozetka.com.ua/ua/promate-rippleblack/p346649994/', 'https://rozetka.com.ua/ua/promate-rippleblack/p346649994/', 'https://rozetka.com.ua/ua/promate-rippleblue/p346660971/', 'https://rozetka.com.ua/ua/ergo-bs-900k/p367908777/', 'https://rozetka.com.ua/ua/a4tech_4711421978651/p362398896/', 'https://rozetka.com.ua/ua/jbl_jblt125btwht/p291422343/', 'https://rozetka.com.ua/ua/ergo-bs-730w/p363176613/', 'https://rozetka.com.ua/ua/ergo-bs-730k/p363175821/', 'https://rozetka.com.ua/ua/ergo-bs-730w/p363176613/', 'https://rozetka.com.ua/ua/a4tech_4711421978378/p362398893/', 'https://rozetka.com.ua/ua/a4tech_4711421978446/p362398890/', 'https://rozetka.com.ua/ua/a4tech_4711421978378/p362398893/']
print(1)
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
print(count)'''  # On AWS that doesn't work
args = [(1, 'Sony WF-C500G Coral/Orange (WFC500D.CE7)', 'sony-wf-c500g-coral-orange-wfc500d-ce7', 'oppo', 800492,
         'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png',
         'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png', 'TWS (2 окремо)', 'Бездротовые',
         'Bluetooth с микрофоном', 'Orange', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2021', 'Китай',
         '12 мес:', '10 ч с аккамулятором', 'алюминий',
         'новые беспроводные наушники Huawei, доступные каждому. Модель ориентирована на покупателей, выбирающих устройство с оптимальным соотношением цена-качество, покупают первые TWS-наушники.',
         '54 г', 'накладные', 'есть 2 режима записи наушника', 'extra', 38, 5), (
        2, 'Defunc True Go Slim TWS Blue (D4214)', 'defunc-true-go-slim-tws-blue-d4214', 'huawei', 400092,
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png',
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Blue', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2020', 'Китай',
        '24 мес:', '22 ч с аккамулятором', 'алюминий',
        'Благодаря светодиодным индикаторам в зарядном устройстве никогда неожиданно не сядет батарейка! И вы всегда будете знать, когда заряд батареи почти исчерпан и пришло время для подзарядки.',
        '39 г', 'вкладыши', 'есть 2 режима записи наушника', 'extra', 43, 5), (
        3, 'Defunc True Go Slim TWS Black (D4211)', 'defunc-true-go-slim-tws-black-d4211', 'xiaomi', 400092,
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png',
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2020', 'Китай',
        '24 мес:', '22 ч с аккамулятором', 'алюминий',
        'Активное шумоподавление в наушниках отсекает до 97% посторонних нежелательных звуков в низкочастотном диапазоне, что подтверждено сертификатом UL, выданным независимой лабораторией Underwriters Laboratories, Inc.',
        '30 г', 'вкладыши', 'наушники типа -C EO-IC100', 'extra', 39, 5), (
        4, 'Defunc True Go Slim TWS Blue (D4214)', 'defunc-true-go-slim-tws-blue-d42144', 'huawei', 400092,
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png',
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Blue', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2020', 'Китай',
        '24 мес:', '22 ч с аккамулятором', 'алюминий',
        'выделяется поддержкой современного стандарта подключения Bluetooth 5.2, временем работы до 24 часов (вместе с зарядным кейсом), а также дизайном полувкладышей, вобравшего в себя лучшие особенности наушников двух типов – вкладышей и внутриканальных.',
        '48 г', 'вкладыши', 'наушники типа -C EO-IC100', 'extra', 25, 5), (
        5, 'Defunc True Go Slim TWS Green (D4216)', 'defunc-true-go-slim-tws-green-d4216', 'xiaomi', 400092,
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png',
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Green', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2020', 'Китай',
        '24 мес:', '22 ч с аккамулятором', 'пластик',
        'Неисчерпаемый источник энергии для любителей музыки. обеспечивают до 24 часов воспроизведения любимых музыки и видео.',
        '51 г', 'накладные', 'есть 2 режима записи наушника', 'extra', 28, 5), (
        6, 'Defunc True Go Slim TWS Pink (D4215)', 'defunc-true-go-slim-tws-pink-d4215', 'realme', 400092,
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png',
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Pink', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2020', 'Китай',
        '24 мес:', '22 ч с аккамулятором', 'пластик',
        'новые беспроводные наушники Huawei, доступные каждому. Модель ориентирована на покупателей, выбирающих устройство с оптимальным соотношением цена-качество, покупают первые TWS-наушники.',
        '51 г', 'вкладыши', 'наушники типа -C EO-IC100', 'extra', 29, 5), (
        7, 'Defunc True Go Slim TWS Red (D4213)', 'defunc-true-go-slim-tws-red-d4213', 'tecno', 400092,
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png',
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Red', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2020', 'Китай',
        '24 мес:', '22 ч с аккамулятором', 'алюминий',
        'Технология JBL Deep Bass Sound До 6 часов оспроизведения плюс 20 в чехле с возможностью быстрой зарядки Стереозвонки в режиме «hands-free»',
        '56 г', 'вкладыши', 'наушники типа -C EO-IC100', 'extra', 25, 5), (
        8, 'Defunc True Go Slim TWS White (D4212)', 'defunc-true-go-slim-tws-white-d4212', 'tecno', 384692,
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png',
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'White', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2020', 'Китай',
        '24 мес:', '22 ч с аккамулятором', 'пластик',
        'новые беспроводные наушники Huawei, доступные каждому. Модель ориентирована на покупателей, выбирающих устройство с оптимальным соотношением цена-качество, покупают первые TWS-наушники.',
        '40 г', 'накладные', 'идёт в комплект чистка для наушников', 'extra', 34, 5), (
        9, 'Samsung Galaxy Buds2 Pro Violet (SM-R510NLVASEK)', 'samsung-galaxy-buds2-pro-violet-sm-r510nlvasek', 'vivo',
        1847692, 'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png',
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Violet', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '12 мес:', '8 ч с аккамулятором', 'алюминий',
        'выделяется поддержкой современного стандарта подключения Bluetooth 5.2, временем работы до 24 часов (вместе с зарядным кейсом), а также дизайном полувкладышей, вобравшего в себя лучшие особенности наушников двух типов – вкладышей и внутриканальных.',
        '56 г', 'вкладыши', 'есть 2 режима записи наушника', 'extra', 30, 5), (
        10, 'Samsung Galaxy Buds2 Pro Violet (SM-R510NLVASEK)', 'samsung-galaxy-buds2-pro-violet-sm-r510nlvasek10',
        'oppo', 1847692, 'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png',
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Violet', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '12 мес:', '8 ч с аккамулятором', 'пластик',
        'выделяется поддержкой современного стандарта подключения Bluetooth 5.2, временем работы до 24 часов (вместе с зарядным кейсом), а также дизайном полувкладышей, вобравшего в себя лучшие особенности наушников двух типов – вкладышей и внутриканальных.',
        '56 г', 'накладные', 'есть 2 режима записи наушника', 'extra', 28, 5), (
        11, 'Samsung Galaxy Buds2 Pro White (SM-R510NZWASEK)', 'samsung-galaxy-buds2-pro-white-sm-r510nzwasek', 'vivo',
        1847692, 'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png',
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'White', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '12 мес:', '8 ч с аккамулятором', 'пластик',
        'Неисчерпаемый источник энергии для любителей музыки. обеспечивают до 24 часов воспроизведения любимых музыки и видео.',
        '33 г', 'вкладыши', 'наушники типа -C EO-IC100', 'extra', 27, 5), (
        12, 'Samsung Galaxy Buds Live Bronze (SM-R180NZNASEK)', 'samsung-galaxy-buds-live-bronze-sm-r180nznasek',
        'xiaomi', 1601292, 'https://content1.rozetka.com.ua/goods/images/big/28606651.jpg',
        'https://content1.rozetka.com.ua/goods/images/big/28606633.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Bronze', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2020', 'Китай',
        '12 мес:', '6 ч с аккамулятором', 'алюминий',
        'выделяется поддержкой современного стандарта подключения Bluetooth 5.2, временем работы до 24 часов (вместе с зарядным кейсом), а также дизайном полувкладышей, вобравшего в себя лучшие особенности наушников двух типов – вкладышей и внутриканальных.',
        '55 г', 'накладные', 'наушники типа -C EO-IC100', 'extra', 43, 5), (
        13, 'Samsung Galaxy Buds Live Black (SM-R180NZKASEK)', 'samsung-galaxy-buds-live-black-sm-r180nzkasek', 'vivo',
        1601292, 'https://content.rozetka.com.ua/goods/images/big/28597961.jpg',
        'https://content1.rozetka.com.ua/goods/images/big/28598000.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2020', 'Китай',
        '12 мес:', '6 ч с аккамулятором', 'пластик',
        'Благодаря светодиодным индикаторам в зарядном устройстве никогда неожиданно не сядет батарейка! И вы всегда будете знать, когда заряд батареи почти исчерпан и пришло время для подзарядки.',
        '52 г', 'вкладыши', 'наушники типа -C EO-IC100', 'extra', 39, 5), (
        14, 'Samsung Galaxy Buds Live Bronze (SM-R180NZNASEK)', 'samsung-galaxy-buds-live-bronze-sm-r180nznasek14',
        'samsung', 1601292, 'https://content1.rozetka.com.ua/goods/images/big/28606651.jpg',
        'https://content1.rozetka.com.ua/goods/images/big/28606633.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Bronze', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2020', 'Китай',
        '12 мес:', '6 ч с аккамулятором', 'пластик',
        'Компактный зарядный кейс весом всего 45 граммов сочетает в себе миниатюрный, минималистический дизайн и батарею емкостью 400 mAh. Время работы таких компактных и одновременно мощных наушников составит до 5 часов без подзарядки и до 22 часов вместе с зарядным кейсом.',
        '53 г', 'вкладыши', 'есть 2 режима записи наушника', 'extra', 38, 5), (
        15, 'Samsung Galaxy Buds Live White (SM-R180NZWASEK)', 'samsung-galaxy-buds-live-white-sm-r180nzwasek',
        'samsung', 1385692, 'https://content.rozetka.com.ua/goods/images/big/28607077.jpg',
        'https://content2.rozetka.com.ua/goods/images/big/28607007.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'White', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2020', 'Китай',
        '12 мес:', '6 ч с аккамулятором', 'пластик',
        'Активное шумоподавление в наушниках отсекает до 97% посторонних нежелательных звуков в низкочастотном диапазоне, что подтверждено сертификатом UL, выданным независимой лабораторией Underwriters Laboratories, Inc.',
        '35 г', 'вкладыши', 'идёт в комплект чистка для наушников', 'extra', 29, 5), (
        16, 'Huawei FreeBuds SE White (55034952)', 'huawei-freebuds-se-white-55034952', 'samsung', 584892,
        'https://content.rozetka.com.ua/goods/images/big/281725462.jpg',
        'https://content.rozetka.com.ua/goods/images/big/281725459.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'White', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '12 мес:', '24 ч с аккамулятором', 'пластик',
        'Беспроводные наушники нового поколения подключаются при помощи Bluetooth 5.0 и используют технологию TWS для первоклассного 3D стереозвука. Двойной микрофон еще лучше справляется с шумоподавлением. Наушники выполнены в компактном и ультра лёгком корпусе, что позволяет им крепко держаться в ушах даже при занятии спортом. Наушники так же могут использоваться по отдельности как беспроводная гарнитура, когда вы за рулем.',
        '42 г', 'накладные', 'есть 2 режима записи наушника', 'extra', 46, 5), (
        17, 'Defunc True Talk TWS Black (D4311) ', 'defunc-true-talk-tws-black-d4311', 'samsung', 862092,
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png',
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '24 мес:', '20 ч с аккамулятором', 'пластик',
        'Беспроводные наушники нового поколения подключаются при помощи Bluetooth 5.0 и используют технологию TWS для первоклассного 3D стереозвука. Двойной микрофон еще лучше справляется с шумоподавлением. Наушники выполнены в компактном и ультра лёгком корпусе, что позволяет им крепко держаться в ушах даже при занятии спортом. Наушники так же могут использоваться по отдельности как беспроводная гарнитура, когда вы за рулем.',
        '38 г', 'вкладыши', 'есть 2 режима записи наушника', 'extra', 43, 5), (
        18, 'Defunc True Talk TWS Black (D4311) ', 'defunc-true-talk-tws-black-d431118', 'realme', 862092,
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png',
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '24 мес:', '20 ч с аккамулятором', 'пластик',
        'Неисчерпаемый источник энергии для любителей музыки. обеспечивают до 24 часов воспроизведения любимых музыки и видео.',
        '48 г', 'накладные', 'есть 2 режима записи наушника', 'extra', 50, 5), (
        19, 'Defunc True Talk TWS Blue (D4314)', 'defunc-true-talk-tws-blue-d4314', 'xiaomi', 862092,
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png',
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Blue', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '24 мес:', '20 ч с аккамулятором', 'алюминий',
        'Технология JBL Deep Bass Sound До 6 часов оспроизведения плюс 20 в чехле с возможностью быстрой зарядки Стереозвонки в режиме «hands-free»',
        '51 г', 'накладные', 'идёт в комплект чистка для наушников', 'extra', 44, 5), (
        20, 'Defunc True Talk TWS Green (D4316)', 'defunc-true-talk-tws-green-d4316', 'huawei', 862092,
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png',
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Green', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '24 мес:', '20 ч с аккамулятором', 'пластик',
        'Неисчерпаемый источник энергии для любителей музыки. обеспечивают до 24 часов воспроизведения любимых музыки и видео.',
        '43 г', 'накладные', 'есть 2 режима записи наушника', 'extra', 47, 5), (
        21, 'Defunc True Talk TWS Pink (D4315)', 'defunc-true-talk-tws-pink-d4315', 'tecno', 831292,
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png',
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Pink', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '24 мес:', '20 ч с аккамулятором', 'алюминий',
        'Благодаря светодиодным индикаторам в зарядном устройстве никогда неожиданно не сядет батарейка! И вы всегда будете знать, когда заряд батареи почти исчерпан и пришло время для подзарядки.',
        '47 г', 'вкладыши', 'идёт в комплект чистка для наушников', 'extra', 39, 5), (
        22, 'Defunc True Talk TWS Red (D4313)', 'defunc-true-talk-tws-red-d4313', 'realme', 831292,
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png',
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Red', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '24 мес:', '20 ч с аккамулятором', 'пластик',
        'Благодаря светодиодным индикаторам в зарядном устройстве никогда неожиданно не сядет батарейка! И вы всегда будете знать, когда заряд батареи почти исчерпан и пришло время для подзарядки.',
        '59 г', 'вкладыши', 'есть 2 режима записи наушника', 'extra', 31, 5), (
        23, 'Defunc True Talk TWS White (D4312)', 'defunc-true-talk-tws-white-d4312', 'oppo', 862092,
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png',
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'White', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '24 мес:', '20 ч с аккамулятором', 'пластик',
        'выделяется поддержкой современного стандарта подключения Bluetooth 5.2, временем работы до 24 часов (вместе с зарядным кейсом), а также дизайном полувкладышей, вобравшего в себя лучшие особенности наушников двух типов – вкладышей и внутриканальных.',
        '52 г', 'накладные', 'идёт в комплект чистка для наушников', 'extra', 43, 5), (
        24, 'Apple AirPods with Lightning Charging Case 2022 (3-го покоління) (MPNY3TY/A)',
        'apple-airpods-with-lightning-charging-case-2022-3-go-pokolinnia-mpny3ty-a', 'tecno', 2617692,
        'https://content1.rozetka.com.ua/goods/images/big/285470238.jpg',
        'https://content.rozetka.com.ua/goods/images/big/285470239.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'White', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '12 мес:', '6 ч с аккамулятором', 'пластик',
        'Активное шумоподавление в наушниках отсекает до 97% посторонних нежелательных звуков в низкочастотном диапазоне, что подтверждено сертификатом UL, выданным независимой лабораторией Underwriters Laboratories, Inc.',
        '55 г', 'вкладыши', 'есть 2 режима записи наушника', 'extra', 26, 5), (
        25, 'Huawei FreeBuds 5i Nebula Black (55036650)', 'huawei-freebuds-5i-nebula-black-55036650', 'samsung', 923692,
        'https://content.rozetka.com.ua/goods/images/big/305181256.jpg',
        'https://content.rozetka.com.ua/goods/images/big/305181259.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black-Grey', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022',
        'Китай', '12 мес:', '28 ч с аккамулятором', 'алюминий',
        'Все лучшее для пользователя собрано в этой маленькой компактной оболочке вакуумного типа. Наушники стали идеальным средством прослушивания музыки, осуществления голосовых вызовов, гейминга посредством применения мобильных устройств.',
        '59 г', 'накладные', 'наушники типа -C EO-IC100', 'extra', 50, 5), (
        26, 'Huawei FreeBuds 5i Nebula Black (55036650)', 'huawei-freebuds-5i-nebula-black-5503665026', 'tecno', 923692,
        'https://content.rozetka.com.ua/goods/images/big/305181256.jpg',
        'https://content.rozetka.com.ua/goods/images/big/305181259.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black-Grey', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022',
        'Китай', '12 мес:', '28 ч с аккамулятором', 'пластик',
        'Технология JBL Deep Bass Sound До 6 часов оспроизведения плюс 20 в чехле с возможностью быстрой зарядки Стереозвонки в режиме «hands-free»',
        '51 г', 'накладные', 'есть 2 режима записи наушника', 'extra', 32, 5), (
        27, 'Huawei FreeBuds 5i Isle Blue (55036649)', 'huawei-freebuds-5i-isle-blue-55036649', 'realme', 923692,
        'https://content1.rozetka.com.ua/goods/images/big/305181271.jpg',
        'https://content1.rozetka.com.ua/goods/images/big/305181272.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Blue-Grey', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '12 мес:', '28 ч с аккамулятором', 'алюминий',
        'Все лучшее для пользователя собрано в этой маленькой компактной оболочке вакуумного типа. Наушники стали идеальным средством прослушивания музыки, осуществления голосовых вызовов, гейминга посредством применения мобильных устройств.',
        '51 г', 'вкладыши', 'наушники типа -C EO-IC100', 'extra', 31, 5), (
        28, 'Huawei FreeBuds 5i Ceramic White (55036651)', 'huawei-freebuds-5i-ceramic-white-55036651', 'huawei',
        923692, 'https://content1.rozetka.com.ua/goods/images/big/305181245.jpg',
        'https://content1.rozetka.com.ua/goods/images/big/305181246.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'White-Grey', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022',
        'Китай', '12 мес:', '28 ч с аккамулятором', 'пластик',
        'Компактный зарядный кейс весом всего 45 граммов сочетает в себе миниатюрный, минималистический дизайн и батарею емкостью 400 mAh. Время работы таких компактных и одновременно мощных наушников составит до 5 часов без подзарядки и до 22 часов вместе с зарядным кейсом.',
        '44 г', 'накладные', 'идёт в комплект чистка для наушников', 'extra', 40, 5), (
        29, 'Xiaomi QCY T5 TWS Bluetooth Black (6957141405505/6957141406267)',
        'xiaomi-qcy-t5-tws-bluetooth-black-6957141405505-6957141406267', 'oppo', 184492,
        'https://content.rozetka.com.ua/goods/images/big/175324012.jpg',
        'https://content1.rozetka.com.ua/goods/images/big/175324030.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '12 мес:', '5 ч с аккамулятором', 'алюминий',
        'выделяется поддержкой современного стандарта подключения Bluetooth 5.2, временем работы до 24 часов (вместе с зарядным кейсом), а также дизайном полувкладышей, вобравшего в себя лучшие особенности наушников двух типов – вкладышей и внутриканальных.',
        '54 г', 'накладные', 'есть 2 режима записи наушника', 'extra', 42, 5), (
        30, 'JBL Wave Buds Black (JBLWBUDSBLK)', 'jbl-wave-buds-black-jblwbudsblk', 'huawei', 492492,
        'https://content.rozetka.com.ua/goods/images/big/314398871.jpg',
        'https://content2.rozetka.com.ua/goods/images/big/314398872.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '12 мес:', '32 ч с аккамулятором', 'пластик',
        'новые беспроводные наушники Huawei, доступные каждому. Модель ориентирована на покупателей, выбирающих устройство с оптимальным соотношением цена-качество, покупают первые TWS-наушники.',
        '52 г', 'накладные', 'есть 2 режима записи наушника', 'extra', 37, 5), (
        31, 'JBL Wave Buds Black (JBLWBUDSBLK)', 'jbl-wave-buds-black-jblwbudsblk31', 'oppo', 492492,
        'https://content.rozetka.com.ua/goods/images/big/314398871.jpg',
        'https://content2.rozetka.com.ua/goods/images/big/314398872.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '12 мес:', '32 ч с аккамулятором', 'алюминий',
        'новые беспроводные наушники Huawei, доступные каждому. Модель ориентирована на покупателей, выбирающих устройство с оптимальным соотношением цена-качество, покупают первые TWS-наушники.',
        '51 г', 'вкладыши', 'идёт в комплект чистка для наушников', 'extra', 46, 5), (
        32, 'JBL Wave Buds White (JBLWBUDSWHT)', 'jbl-wave-buds-white-jblwbudswht', 'oppo', 492492,
        'https://content2.rozetka.com.ua/goods/images/big/314398884.jpg',
        'https://content.rozetka.com.ua/goods/images/big/314398885.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'White', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '12 мес:', '32 ч с аккамулятором', 'пластик',
        'Беспроводные наушники нового поколения подключаются при помощи Bluetooth 5.0 и используют технологию TWS для первоклассного 3D стереозвука. Двойной микрофон еще лучше справляется с шумоподавлением. Наушники выполнены в компактном и ультра лёгком корпусе, что позволяет им крепко держаться в ушах даже при занятии спортом. Наушники так же могут использоваться по отдельности как беспроводная гарнитура, когда вы за рулем.',
        '33 г', 'накладные', 'есть 2 режима записи наушника', 'extra', 35, 5), (
        33, 'Xiaomi Redmi Buds 3 Lite Black (BHR5489GL)', 'xiaomi-redmi-buds-3-lite-black-bhr5489gl', 'tecno', 276892,
        'https://content1.rozetka.com.ua/goods/images/big/305005234.jpg',
        'https://content2.rozetka.com.ua/goods/images/big/305005235.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2021', 'Китай',
        '12 мес:', '18 ч с аккамулятором', 'алюминий',
        'Все лучшее для пользователя собрано в этой маленькой компактной оболочке вакуумного типа. Наушники стали идеальным средством прослушивания музыки, осуществления голосовых вызовов, гейминга посредством применения мобильных устройств.',
        '52 г', 'накладные', 'есть 2 режима записи наушника', 'extra', 26, 5), (
        34, 'BeatBox PODS PRO 1 Wireless Charging Black (bbppro1wcb)',
        'beatbox-pods-pro-1-wireless-charging-black-bbppro1wcb', 'oppo', 393932,
        'https://content2.rozetka.com.ua/goods/images/big/182697167.jpg',
        'https://content1.rozetka.com.ua/goods/images/big/182697236.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2021', 'Китай',
        '12 мес:', '4 ч с аккамулятором', 'алюминий',
        'Компактный зарядный кейс весом всего 45 граммов сочетает в себе миниатюрный, минималистический дизайн и батарею емкостью 400 mAh. Время работы таких компактных и одновременно мощных наушников составит до 5 часов без подзарядки и до 22 часов вместе с зарядным кейсом.',
        '46 г', 'вкладыши', 'наушники типа -C EO-IC100', 'extra', 42, 5), (
        35, 'BeatBox PODS PRO 1 Wireless Charging Black (bbppro1wcb)',
        'beatbox-pods-pro-1-wireless-charging-black-bbppro1wcb35', 'vivo', 393932,
        'https://content2.rozetka.com.ua/goods/images/big/182697167.jpg',
        'https://content1.rozetka.com.ua/goods/images/big/182697236.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2021', 'Китай',
        '12 мес:', '4 ч с аккамулятором', 'пластик',
        'Неисчерпаемый источник энергии для любителей музыки. обеспечивают до 24 часов воспроизведения любимых музыки и видео.',
        '39 г', 'вкладыши', 'идёт в комплект чистка для наушников', 'extra', 45, 5), (
        36, 'BeatBox PODS PRO 1 Wireless charging Black-red (bbppro1wcbr)',
        'beatbox-pods-pro-1-wireless-charging-black-red-bbppro1wcbr', 'huawei', 393932,
        'https://content2.rozetka.com.ua/goods/images/big/279987498.jpg',
        'https://content.rozetka.com.ua/goods/images/big/279987512.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black-Red', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2021', 'Китай',
        '6 мес:', '4 ч с аккамулятором', 'алюминий',
        'выделяется поддержкой современного стандарта подключения Bluetooth 5.2, временем работы до 24 часов (вместе с зарядным кейсом), а также дизайном полувкладышей, вобравшего в себя лучшие особенности наушников двух типов – вкладышей и внутриканальных.',
        '45 г', 'вкладыши', 'наушники типа -C EO-IC100', 'extra', 26, 5), (
        37, 'BeatBox PODS PRO 1 Wireless Charging White (bbppro1wcw)',
        'beatbox-pods-pro-1-wireless-charging-white-bbppro1wcw', 'realme', 393932,
        'https://content2.rozetka.com.ua/goods/images/big/182697450.jpg',
        'https://content2.rozetka.com.ua/goods/images/big/182697479.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'White', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2021', 'Китай',
        '12 мес:', '4 ч с аккамулятором', 'алюминий',
        'выделяется поддержкой современного стандарта подключения Bluetooth 5.2, временем работы до 24 часов (вместе с зарядным кейсом), а также дизайном полувкладышей, вобравшего в себя лучшие особенности наушников двух типов – вкладышей и внутриканальных.',
        '59 г', 'вкладыши', 'идёт в комплект чистка для наушников', 'extra', 30, 5), (
        38, 'BeatBox PODS PRO 1 Wireless charging White-red (bbppro1wcwr)',
        'beatbox-pods-pro-1-wireless-charging-white-red-bbppro1wcwr', 'realme', 393932,
        'https://content1.rozetka.com.ua/goods/images/big/279987500.jpg',
        'https://content1.rozetka.com.ua/goods/images/big/279987516.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'White and Red', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2021',
        'Китай', '6 мес:', '4 ч с аккамулятором', 'алюминий',
        'Благодаря светодиодным индикаторам в зарядном устройстве никогда неожиданно не сядет батарейка! И вы всегда будете знать, когда заряд батареи почти исчерпан и пришло время для подзарядки.',
        '51 г', 'накладные', 'идёт в комплект чистка для наушников', 'extra', 47, 5), (
        39, 'Samsung Galaxy Buds2 White (SM-R177NZWASEK)', 'samsung-galaxy-buds2-white-sm-r177nzwasek', 'oppo', 1601292,
        'https://content2.rozetka.com.ua/goods/images/big/202640048.jpg',
        'https://content1.rozetka.com.ua/goods/images/big/202640056.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'White', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2021', 'Китай',
        '12 мес:', '29 ч с аккамулятором', 'алюминий',
        'Активное шумоподавление в наушниках отсекает до 97% посторонних нежелательных звуков в низкочастотном диапазоне, что подтверждено сертификатом UL, выданным независимой лабораторией Underwriters Laboratories, Inc.',
        '59 г', 'накладные', 'наушники типа -C EO-IC100', 'extra', 28, 5), (
        40, 'Samsung Galaxy Buds2 Black (SM-R177NZKASEK)', 'samsung-galaxy-buds2-black-sm-r177nzkasek', 'oppo', 1601292,
        'https://content1.rozetka.com.ua/goods/images/big/202640004.jpg',
        'https://content.rozetka.com.ua/goods/images/big/202640006.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2021', 'Китай',
        '12 мес:', '29 ч с аккамулятором', 'алюминий',
        'Благодаря светодиодным индикаторам в зарядном устройстве никогда неожиданно не сядет батарейка! И вы всегда будете знать, когда заряд батареи почти исчерпан и пришло время для подзарядки.',
        '56 г', 'вкладыши', 'идёт в комплект чистка для наушников', 'extra', 50, 5), (
        41, 'Samsung Galaxy Buds2 Lavender (SM-R177NLVASEK)', 'samsung-galaxy-buds2-lavender-sm-r177nlvasek', 'vivo',
        1601292, 'https://content2.rozetka.com.ua/goods/images/big/202640026.jpg',
        'https://content2.rozetka.com.ua/goods/images/big/202640027.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Lavender', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2021', 'Китай',
        '12 мес:', '29 ч с аккамулятором', 'пластик',
        'Технология JBL Deep Bass Sound До 6 часов оспроизведения плюс 20 в чехле с возможностью быстрой зарядки Стереозвонки в режиме «hands-free»',
        '36 г', 'вкладыши', 'есть 2 режима записи наушника', 'extra', 42, 5), (
        42, 'Samsung Galaxy Buds2 Olive (SM-R177NZGASEK)', 'samsung-galaxy-buds2-olive-sm-r177nzgasek', 'vivo', 1601292,
        'https://content1.rozetka.com.ua/goods/images/big/202640014.jpg',
        'https://content2.rozetka.com.ua/goods/images/big/202640015.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Olive', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2021', 'Китай',
        '12 мес:', '29 ч с аккамулятором', 'пластик',
        'Благодаря светодиодным индикаторам в зарядном устройстве никогда неожиданно не сядет батарейка! И вы всегда будете знать, когда заряд батареи почти исчерпан и пришло время для подзарядки.',
        '34 г', 'накладные', 'наушники типа -C EO-IC100', 'extra', 35, 5), (
        43, 'Samsung Galaxy Buds2 White (SM-R177NZWASEK)', 'samsung-galaxy-buds2-white-sm-r177nzwasek43', 'vivo',
        1601292, 'https://content2.rozetka.com.ua/goods/images/big/202640048.jpg',
        'https://content1.rozetka.com.ua/goods/images/big/202640056.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'White', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2021', 'Китай',
        '12 мес:', '29 ч с аккамулятором', 'алюминий',
        'Беспроводные наушники нового поколения подключаются при помощи Bluetooth 5.0 и используют технологию TWS для первоклассного 3D стереозвука. Двойной микрофон еще лучше справляется с шумоподавлением. Наушники выполнены в компактном и ультра лёгком корпусе, что позволяет им крепко держаться в ушах даже при занятии спортом. Наушники так же могут использоваться по отдельности как беспроводная гарнитура, когда вы за рулем.',
        '32 г', 'вкладыши', 'идёт в комплект чистка для наушников', 'extra', 32, 5), (
        44, 'JBL Wave Flex Black (JBLWFLEXBLK)', 'jbl-wave-flex-black-jblwflexblk', 'realme', 615692,
        'https://content2.rozetka.com.ua/goods/images/big/314509762.jpg',
        'https://content.rozetka.com.ua/goods/images/big/314509763.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '12 мес:', '32 ч с аккамулятором', 'алюминий',
        'Технология JBL Deep Bass Sound До 6 часов оспроизведения плюс 20 в чехле с возможностью быстрой зарядки Стереозвонки в режиме «hands-free»',
        '43 г', 'накладные', 'идёт в комплект чистка для наушников', 'extra', 39, 5), (
        45, 'JBL Wave Flex Black (JBLWFLEXBLK)', 'jbl-wave-flex-black-jblwflexblk45', 'realme', 615692,
        'https://content2.rozetka.com.ua/goods/images/big/314509762.jpg',
        'https://content.rozetka.com.ua/goods/images/big/314509763.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '12 мес:', '32 ч с аккамулятором', 'пластик',
        'новые беспроводные наушники Huawei, доступные каждому. Модель ориентирована на покупателей, выбирающих устройство с оптимальным соотношением цена-качество, покупают первые TWS-наушники.',
        '54 г', 'накладные', 'идёт в комплект чистка для наушников', 'extra', 45, 5), (
        46, 'JBL Wave Flex White (JBLWFLEXWHT)', 'jbl-wave-flex-white-jblwflexwht', 'huawei', 615692,
        'https://content2.rozetka.com.ua/goods/images/big/314509931.jpg',
        'https://content1.rozetka.com.ua/goods/images/big/314509933.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'White', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '12 мес:', '32 ч с аккамулятором', 'алюминий',
        'Компактный зарядный кейс весом всего 45 граммов сочетает в себе миниатюрный, минималистический дизайн и батарею емкостью 400 mAh. Время работы таких компактных и одновременно мощных наушников составит до 5 часов без подзарядки и до 22 часов вместе с зарядным кейсом.',
        '49 г', 'вкладыши', 'есть 2 режима записи наушника', 'extra', 28, 5), (
        47, 'JBL Wave Beam Black (JBLWBEAMBLK)', 'jbl-wave-beam-black-jblwbeamblk', 'xiaomi', 615692,
        'https://content.rozetka.com.ua/goods/images/big/314398738.jpg',
        'https://content1.rozetka.com.ua/goods/images/big/314398739.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '12 мес:', '32 ч с аккамулятором', 'алюминий',
        'Все лучшее для пользователя собрано в этой маленькой компактной оболочке вакуумного типа. Наушники стали идеальным средством прослушивания музыки, осуществления голосовых вызовов, гейминга посредством применения мобильных устройств.',
        '33 г', 'вкладыши', 'есть 2 режима записи наушника', 'extra', 37, 5), (
        48, 'JBL Wave Beam Black (JBLWBEAMBLK)', 'jbl-wave-beam-black-jblwbeamblk48', 'vivo', 615692,
        'https://content.rozetka.com.ua/goods/images/big/314398738.jpg',
        'https://content1.rozetka.com.ua/goods/images/big/314398739.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '12 мес:', '32 ч с аккамулятором', 'алюминий',
        'Компактный зарядный кейс весом всего 45 граммов сочетает в себе миниатюрный, минималистический дизайн и батарею емкостью 400 mAh. Время работы таких компактных и одновременно мощных наушников составит до 5 часов без подзарядки и до 22 часов вместе с зарядным кейсом.',
        '49 г', 'накладные', 'наушники типа -C EO-IC100', 'extra', 43, 5), (
        49, 'JBL Wave Beam White (JBLWBEAMWHT)', 'jbl-wave-beam-white-jblwbeamwht', 'huawei', 615692,
        'https://content.rozetka.com.ua/goods/images/big/314398752.jpg',
        'https://content2.rozetka.com.ua/goods/images/big/314398753.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'White', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '12 мес:', '32 ч с аккамулятором', 'пластик',
        'выделяется поддержкой современного стандарта подключения Bluetooth 5.2, временем работы до 24 часов (вместе с зарядным кейсом), а также дизайном полувкладышей, вобравшего в себя лучшие особенности наушников двух типов – вкладышей и внутриканальных.',
        '60 г', 'накладные', 'есть 2 режима записи наушника', 'extra', 40, 5), (
        50, 'BeatBox PODS AIR 2 Wireless Charging Black (bbpair2wcb)',
        'beatbox-pods-air-2-wireless-charging-black-bbpair2wcb', 'tecno', 338492,
        'https://content1.rozetka.com.ua/goods/images/big/182728728.jpg',
        'https://content.rozetka.com.ua/goods/images/big/182728785.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '12 мес:', '4 ч с аккамулятором', 'алюминий',
        'Активное шумоподавление в наушниках отсекает до 97% посторонних нежелательных звуков в низкочастотном диапазоне, что подтверждено сертификатом UL, выданным независимой лабораторией Underwriters Laboratories, Inc.',
        '53 г', 'накладные', 'есть 2 режима записи наушника', 'extra', 38, 5), (
        51, 'BeatBox PODS AIR 2 Wireless Charging Black (bbpair2wcb)',
        'beatbox-pods-air-2-wireless-charging-black-bbpair2wcb51', 'realme', 338492,
        'https://content1.rozetka.com.ua/goods/images/big/182728728.jpg',
        'https://content.rozetka.com.ua/goods/images/big/182728785.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '12 мес:', '4 ч с аккамулятором', 'алюминий',
        'Активное шумоподавление в наушниках отсекает до 97% посторонних нежелательных звуков в низкочастотном диапазоне, что подтверждено сертификатом UL, выданным независимой лабораторией Underwriters Laboratories, Inc.',
        '30 г', 'накладные', 'наушники типа -C EO-IC100', 'extra', 43, 5), (
        52, 'BeatBox PODS AIR 2 Wireless charging Black-red (bbpair2wcbr)',
        'beatbox-pods-air-2-wireless-charging-black-red-bbpair2wcbr', 'vivo', 338492,
        'https://content1.rozetka.com.ua/goods/images/big/279987503.jpg',
        'https://content.rozetka.com.ua/goods/images/big/279987513.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black-Red', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '6 мес:', '4 ч с аккамулятором', 'пластик',
        'новые беспроводные наушники Huawei, доступные каждому. Модель ориентирована на покупателей, выбирающих устройство с оптимальным соотношением цена-качество, покупают первые TWS-наушники.',
        '58 г', 'вкладыши', 'есть 2 режима записи наушника', 'extra', 25, 5), (
        53, 'BeatBox PODS AIR 2 Wireless Charging White (bbpair2wcw)',
        'beatbox-pods-air-2-wireless-charging-white-bbpair2wcw', 'tecno', 338492,
        'https://content1.rozetka.com.ua/goods/images/big/182727397.jpg',
        'https://content.rozetka.com.ua/goods/images/big/182727420.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'White', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '12 мес:', '4 ч с аккамулятором', 'алюминий',
        'новые беспроводные наушники Huawei, доступные каждому. Модель ориентирована на покупателей, выбирающих устройство с оптимальным соотношением цена-качество, покупают первые TWS-наушники.',
        '58 г', 'вкладыши', 'есть 2 режима записи наушника', 'extra', 38, 5), (
        54, 'BeatBox PODS AIR 2 Wireless charging White-red (bbpair2wcwr)',
        'beatbox-pods-air-2-wireless-charging-white-red-bbpair2wcwr', 'oppo', 338492,
        'https://content.rozetka.com.ua/goods/images/big/279987510.jpg',
        'https://content.rozetka.com.ua/goods/images/big/279987521.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'White and Red', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022',
        'Китай', '6 мес:', '4 ч с аккамулятором', 'алюминий',
        'Технология JBL Deep Bass Sound До 6 часов оспроизведения плюс 20 в чехле с возможностью быстрой зарядки Стереозвонки в режиме «hands-free»',
        '30 г', 'накладные', 'идёт в комплект чистка для наушников', 'extra', 46, 5), (
        55, 'Anker SoundСore Liberty 3 Pro Dusk Purple (A3952GQ1/ A3952HQ1)',
        'anker-soundsore-liberty-3-pro-dusk-purple-a3952gq1-a3952hq1', 'tecno', 1710940,
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png',
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Purple', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2021', 'Китай',
        '18 мес:', '8 ч с аккамулятором', 'алюминий',
        'Технология JBL Deep Bass Sound До 6 часов оспроизведения плюс 20 в чехле с возможностью быстрой зарядки Стереозвонки в режиме «hands-free»',
        '48 г', 'накладные', 'есть 2 режима записи наушника', 'extra', 43, 5), (
        56, 'Anker SoundСore Liberty 3 Pro Fog Gray (A3952GA1)', 'anker-soundsore-liberty-3-pro-fog-gray-a3952ga1',
        'oppo', 2155692, 'https://content1.rozetka.com.ua/goods/images/big/257561490.jpg',
        'https://content1.rozetka.com.ua/goods/images/big/257561493.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Grey', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2021', 'Китай',
        '18 мес:', '8 ч с аккамулятором', 'пластик',
        'Беспроводные наушники нового поколения подключаются при помощи Bluetooth 5.0 и используют технологию TWS для первоклассного 3D стереозвука. Двойной микрофон еще лучше справляется с шумоподавлением. Наушники выполнены в компактном и ультра лёгком корпусе, что позволяет им крепко держаться в ушах даже при занятии спортом. Наушники так же могут использоваться по отдельности как беспроводная гарнитура, когда вы за рулем.',
        '43 г', 'накладные', 'есть 2 режима записи наушника', 'extra', 36, 5), (
        57, 'Anker SoundСore Liberty 3 Pro Dusk Purple (A3952GQ1/ A3952HQ1)',
        'anker-soundsore-liberty-3-pro-dusk-purple-a3952gq1-a3952hq157', 'xiaomi', 1710940,
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png',
        'https://content1.rozetka.com.ua/goods_tags/images_ua/original/316466814.png', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Purple', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2021', 'Китай',
        '18 мес:', '8 ч с аккамулятором', 'алюминий',
        'Благодаря светодиодным индикаторам в зарядном устройстве никогда неожиданно не сядет батарейка! И вы всегда будете знать, когда заряд батареи почти исчерпан и пришло время для подзарядки.',
        '60 г', 'накладные', 'наушники типа -C EO-IC100', 'extra', 44, 5), (
        58, 'Aura 3 White (TWSA3W)', 'aura-3-white-twsa3w', 'samsung', 369292,
        'https://content1.rozetka.com.ua/goods/images/big/294750123.jpg',
        'https://content.rozetka.com.ua/goods/images/big/294750132.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'White', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '3 мес:', '4 ч с аккамулятором', 'алюминий',
        'Все лучшее для пользователя собрано в этой маленькой компактной оболочке вакуумного типа. Наушники стали идеальным средством прослушивания музыки, осуществления голосовых вызовов, гейминга посредством применения мобильных устройств.',
        '36 г', 'вкладыши', 'есть 2 режима записи наушника', 'extra', 29, 5), (
        59, 'OPPO Enco Air 2 (W13) ETE11 Blue', 'oppo-enco-air-2-w13-ete11-blue', 'xiaomi', 769692,
        'https://content.rozetka.com.ua/goods/images/big/270921073.jpg',
        'https://content2.rozetka.com.ua/goods/images/big/270921076.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Blue', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '12 мес:', '4 ч с аккамулятором', 'пластик',
        'выделяется поддержкой современного стандарта подключения Bluetooth 5.2, временем работы до 24 часов (вместе с зарядным кейсом), а также дизайном полувкладышей, вобравшего в себя лучшие особенности наушников двух типов – вкладышей и внутриканальных.',
        '58 г', 'вкладыши', 'наушники типа -C EO-IC100', 'extra', 41, 5), (
        60, 'Sony WI-C100 Black (WIC100B.CE7)', 'sony-wi-c100-black-wic100b-ce7', 'huawei', 307692,
        'https://content1.rozetka.com.ua/goods/images/big/297529368.jpg',
        'https://content1.rozetka.com.ua/goods/images/big/297529389.jpg', 'Вкладки', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', "В'єтнам",
        '12 мес:', '25 ч с аккамулятором', 'алюминий',
        'Компактный зарядный кейс весом всего 45 граммов сочетает в себе миниатюрный, минималистический дизайн и батарею емкостью 400 mAh. Время работы таких компактных и одновременно мощных наушников составит до 5 часов без подзарядки и до 22 часов вместе с зарядным кейсом.',
        '56 г', 'накладные', 'есть 2 режима записи наушника', 'extra', 37, 5), (
        61, 'Sony WI-C100 Black (WIC100B.CE7)', 'sony-wi-c100-black-wic100b-ce761', 'huawei', 307692,
        'https://content1.rozetka.com.ua/goods/images/big/297529368.jpg',
        'https://content1.rozetka.com.ua/goods/images/big/297529389.jpg', 'Вкладки', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', "В'єтнам",
        '12 мес:', '25 ч с аккамулятором', 'алюминий',
        'Все лучшее для пользователя собрано в этой маленькой компактной оболочке вакуумного типа. Наушники стали идеальным средством прослушивания музыки, осуществления голосовых вызовов, гейминга посредством применения мобильных устройств.',
        '48 г', 'вкладыши', 'наушники типа -C EO-IC100', 'extra', 30, 5), (
        62, 'Sony WI-C100 Blue (WIC100L.CE7)', 'sony-wi-c100-blue-wic100l-ce7', 'huawei', 307692,
        'https://content.rozetka.com.ua/goods/images/big/297528069.jpg',
        'https://content.rozetka.com.ua/goods/images/big/297528092.jpg', 'Вкладки', 'Бездротовые',
        'Bluetooth с микрофоном', 'Blue', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', "В'єтнам",
        '12 мес:', '25 ч с аккамулятором', 'пластик',
        'Неисчерпаемый источник энергии для любителей музыки. обеспечивают до 24 часов воспроизведения любимых музыки и видео.',
        '50 г', 'накладные', 'наушники типа -C EO-IC100', 'extra', 31, 5), (
        63, 'Sony WI-C100 White (WIC100W.CE7)', 'sony-wi-c100-white-wic100w-ce7', 'vivo', 307692,
        'https://content1.rozetka.com.ua/goods/images/big/297527686.jpg',
        'https://content1.rozetka.com.ua/goods/images/big/297527687.jpg', 'Вкладки', 'Бездротовые',
        'Bluetooth с микрофоном', 'White', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', "В'єтнам",
        '12 мес:', '25 ч с аккамулятором', 'алюминий',
        'Благодаря светодиодным индикаторам в зарядном устройстве никогда неожиданно не сядет батарейка! И вы всегда будете знать, когда заряд батареи почти исчерпан и пришло время для подзарядки.',
        '49 г', 'накладные', 'идёт в комплект чистка для наушников', 'extra', 49, 5), (
        64, 'Pixus Alien Silver-Black', 'pixus-alien-silver-black', 'realme', 172172,
        'https://content1.rozetka.com.ua/goods/images/big/254142584.jpg',
        'https://content2.rozetka.com.ua/goods/images/big/254142585.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Silver-Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2021',
        'Китай', '12 мес:', '25 ч с аккамулятором', 'пластик',
        'Компактный зарядный кейс весом всего 45 граммов сочетает в себе миниатюрный, минималистический дизайн и батарею емкостью 400 mAh. Время работы таких компактных и одновременно мощных наушников составит до 5 часов без подзарядки и до 22 часов вместе с зарядным кейсом.',
        '31 г', 'накладные', 'идёт в комплект чистка для наушников', 'extra', 35, 5), (
        65, 'Sennheiser Momentum True Wireless 3 Black (509180)', 'sennheiser-momentum-true-wireless-3-black-509180',
        'xiaomi', 3002692, 'https://content.rozetka.com.ua/goods/images/big/273488217.jpg',
        'https://content.rozetka.com.ua/goods/images/preview/273488217.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '24 мес:', '7 ч с аккамулятором', 'алюминий',
        'Компактный зарядный кейс весом всего 45 граммов сочетает в себе миниатюрный, минималистический дизайн и батарею емкостью 400 mAh. Время работы таких компактных и одновременно мощных наушников составит до 5 часов без подзарядки и до 22 часов вместе с зарядным кейсом.',
        '30 г', 'накладные', 'есть 2 режима записи наушника', 'extra', 29, 5), (
        66, 'Sennheiser Momentum True Wireless 3 Black (509180)', 'sennheiser-momentum-true-wireless-3-black-50918066',
        'huawei', 3002692, 'https://content.rozetka.com.ua/goods/images/big/273488217.jpg',
        'https://content.rozetka.com.ua/goods/images/preview/273488217.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '24 мес:', '7 ч с аккамулятором', 'алюминий',
        'Активное шумоподавление в наушниках отсекает до 97% посторонних нежелательных звуков в низкочастотном диапазоне, что подтверждено сертификатом UL, выданным независимой лабораторией Underwriters Laboratories, Inc.',
        '42 г', 'накладные', 'идёт в комплект чистка для наушников', 'extra', 47, 5), (
        67, 'Sennheiser Momentum True Wireless 3 Graphite (700074)',
        'sennheiser-momentum-true-wireless-3-graphite-700074', 'huawei', 3079692,
        'https://content1.rozetka.com.ua/goods/images/big/273488202.jpg',
        'https://content1.rozetka.com.ua/goods/images/big/273488203.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Graphite', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '24 мес:', '7 ч с аккамулятором', 'алюминий',
        'Активное шумоподавление в наушниках отсекает до 97% посторонних нежелательных звуков в низкочастотном диапазоне, что подтверждено сертификатом UL, выданным независимой лабораторией Underwriters Laboratories, Inc.',
        '35 г', 'накладные', 'идёт в комплект чистка для наушников', 'extra', 49, 5), (
        68, 'Sennheiser Momentum True Wireless 3 White (509181)', 'sennheiser-momentum-true-wireless-3-white-509181',
        'samsung', 3002692, 'https://content2.rozetka.com.ua/goods/images/big/273488244.jpg',
        'https://content2.rozetka.com.ua/goods/images/preview/273488244.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'White', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '24 мес:', '7 ч с аккамулятором', 'пластик',
        'выделяется поддержкой современного стандарта подключения Bluetooth 5.2, временем работы до 24 часов (вместе с зарядным кейсом), а также дизайном полувкладышей, вобравшего в себя лучшие особенности наушников двух типов – вкладышей и внутриканальных.',
        '59 г', 'накладные', 'идёт в комплект чистка для наушников', 'extra', 39, 5), (
        69, 'Marshall Headphones Motif ANC Black (1005964)', 'marshall-headphones-motif-anc-black-1005964', 'tecno',
        2771692, 'https://content1.rozetka.com.ua/goods/images/big/278885969.jpg',
        'https://content1.rozetka.com.ua/goods/images/big/278885970.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '24 мес:', '25 ч с аккамулятором', 'пластик',
        'Технология JBL Deep Bass Sound До 6 часов оспроизведения плюс 20 в чехле с возможностью быстрой зарядки Стереозвонки в режиме «hands-free»',
        '30 г', 'накладные', 'наушники типа -C EO-IC100', 'extra', 39, 5), (
        70, 'Gelius Pro Reddots TWS Earbuds GP-TWS010 Pink (2099900822988)',
        'gelius-pro-reddots-tws-earbuds-gp-tws010-pink-2099900822988', 'samsung', 215292,
        'https://content2.rozetka.com.ua/goods/images/big/178102278.jpg',
        'https://content.rozetka.com.ua/goods/images/big/178102254.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Pink', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '12 мес:', '3 ч с аккамулятором', 'пластик',
        'Активное шумоподавление в наушниках отсекает до 97% посторонних нежелательных звуков в низкочастотном диапазоне, что подтверждено сертификатом UL, выданным независимой лабораторией Underwriters Laboratories, Inc.',
        '59 г', 'вкладыши', 'есть 2 режима записи наушника', 'extra', 25, 5), (
        71, 'Gelius Pro Reddots TWS Earbuds GP-TWS010 Black (2099900822971)',
        'gelius-pro-reddots-tws-earbuds-gp-tws010-black-2099900822971', 'oppo', 215292,
        'https://content.rozetka.com.ua/goods/images/big/178102197.jpg',
        'https://content2.rozetka.com.ua/goods/images/big/178102161.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '12 мес:', '3 ч с аккамулятором', 'пластик',
        'Благодаря светодиодным индикаторам в зарядном устройстве никогда неожиданно не сядет батарейка! И вы всегда будете знать, когда заряд батареи почти исчерпан и пришло время для подзарядки.',
        '60 г', 'накладные', 'идёт в комплект чистка для наушников', 'extra', 25, 5), (
        72, 'Gelius Pro Reddots TWS Earbuds GP-TWS010 Pink (2099900822988)',
        'gelius-pro-reddots-tws-earbuds-gp-tws010-pink-209990082298872', 'oppo', 215292,
        'https://content2.rozetka.com.ua/goods/images/big/178102278.jpg',
        'https://content.rozetka.com.ua/goods/images/big/178102254.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Pink', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '12 мес:', '3 ч с аккамулятором', 'пластик',
        'выделяется поддержкой современного стандарта подключения Bluetooth 5.2, временем работы до 24 часов (вместе с зарядным кейсом), а также дизайном полувкладышей, вобравшего в себя лучшие особенности наушников двух типов – вкладышей и внутриканальных.',
        '30 г', 'вкладыши', 'наушники типа -C EO-IC100', 'extra', 31, 5), (
        73, 'Sony WF-1000XM4 Silver (WF1000XM4S.CE7)', 'sony-wf-1000xm4-silver-wf1000xm4s-ce7', 'samsung', 3079692,
        'https://content.rozetka.com.ua/goods/images/big/185478547.jpg',
        'https://content.rozetka.com.ua/goods/images/big/185478546.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Silver', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', "В'єтнам",
        '12 мес:', '3 ч с аккамулятором', 'алюминий',
        'выделяется поддержкой современного стандарта подключения Bluetooth 5.2, временем работы до 24 часов (вместе с зарядным кейсом), а также дизайном полувкладышей, вобравшего в себя лучшие особенности наушников двух типов – вкладышей и внутриканальных.',
        '55 г', 'накладные', 'есть 2 режима записи наушника', 'extra', 36, 5), (
        74, 'Sony WF-1000XM4 Black (WF1000XM4B.CE7)', 'sony-wf-1000xm4-black-wf1000xm4b-ce7', 'oppo', 3079692,
        'https://content1.rozetka.com.ua/goods/images/big/185478738.jpg',
        'https://content.rozetka.com.ua/goods/images/big/185478709.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', "В'єтнам",
        '12 мес:', '3 ч с аккамулятором', 'пластик',
        'Активное шумоподавление в наушниках отсекает до 97% посторонних нежелательных звуков в низкочастотном диапазоне, что подтверждено сертификатом UL, выданным независимой лабораторией Underwriters Laboratories, Inc.',
        '31 г', 'вкладыши', 'есть 2 режима записи наушника', 'extra', 44, 5), (
        75, 'Sony WF-1000XM4 Silver (WF1000XM4S.CE7)', 'sony-wf-1000xm4-silver-wf1000xm4s-ce775', 'tecno', 3079692,
        'https://content.rozetka.com.ua/goods/images/big/185478547.jpg',
        'https://content.rozetka.com.ua/goods/images/big/185478546.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Silver', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', "В'єтнам",
        '12 мес:', '3 ч с аккамулятором', 'алюминий',
        'Все лучшее для пользователя собрано в этой маленькой компактной оболочке вакуумного типа. Наушники стали идеальным средством прослушивания музыки, осуществления голосовых вызовов, гейминга посредством применения мобильных устройств.',
        '59 г', 'накладные', 'есть 2 режима записи наушника', 'extra', 48, 5), (
        76, 'Promate TWS FreePods-3 Black (freepods-3.black)', 'promate-tws-freepods-3-black-freepods-3-black',
        'huawei', 430892, 'https://content1.rozetka.com.ua/goods/images/big/278329029.jpg',
        'https://content.rozetka.com.ua/goods/images/big/278329050.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '24 мес:', '6 ч с аккамулятором', 'пластик',
        'Активное шумоподавление в наушниках отсекает до 97% посторонних нежелательных звуков в низкочастотном диапазоне, что подтверждено сертификатом UL, выданным независимой лабораторией Underwriters Laboratories, Inc.',
        '55 г', 'вкладыши', 'есть 2 режима записи наушника', 'extra', 28, 5), (
        77, 'Promate TWS FreePods-3 Black (freepods-3.black)', 'promate-tws-freepods-3-black-freepods-3-black77',
        'xiaomi', 430892, 'https://content1.rozetka.com.ua/goods/images/big/278329029.jpg',
        'https://content.rozetka.com.ua/goods/images/big/278329050.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Black', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '24 мес:', '6 ч с аккамулятором', 'пластик',
        'выделяется поддержкой современного стандарта подключения Bluetooth 5.2, временем работы до 24 часов (вместе с зарядным кейсом), а также дизайном полувкладышей, вобравшего в себя лучшие особенности наушников двух типов – вкладышей и внутриканальных.',
        '56 г', 'вкладыши', 'наушники типа -C EO-IC100', 'extra', 35, 5), (
        78, 'Promate TWS FreePods-3 Blue (freepods-3.blue)', 'promate-tws-freepods-3-blue-freepods-3-blue', 'huawei',
        430892, 'https://content1.rozetka.com.ua/goods/images/big/278329557.jpg',
        'https://content2.rozetka.com.ua/goods/images/big/278329577.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'Blue', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '24 мес:', '6 ч с аккамулятором', 'алюминий',
        'Благодаря светодиодным индикаторам в зарядном устройстве никогда неожиданно не сядет батарейка! И вы всегда будете знать, когда заряд батареи почти исчерпан и пришло время для подзарядки.',
        '50 г', 'вкладыши', 'идёт в комплект чистка для наушников', 'extra', 41, 5), (
        79, 'Promate TWS FreePods-3 White (freepods-3.white)', 'promate-tws-freepods-3-white-freepods-3-white',
        'xiaomi', 430892, 'https://content2.rozetka.com.ua/goods/images/big/278334904.jpg',
        'https://content2.rozetka.com.ua/goods/images/big/278334905.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'White', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '24 мес:', '6 ч с аккамулятором', 'пластик',
        'выделяется поддержкой современного стандарта подключения Bluetooth 5.2, временем работы до 24 часов (вместе с зарядным кейсом), а также дизайном полувкладышей, вобравшего в себя лучшие особенности наушников двух типов – вкладышей и внутриканальных.',
        '59 г', 'накладные', 'есть 2 режима записи наушника', 'extra', 28, 5), (
        80, 'OPPO Enco Air2 Pro ETE21 White', 'oppo-enco-air2-pro-ete21-white', 'samsung', 769692,
        'https://content2.rozetka.com.ua/goods/images/big/287017604.jpg',
        'https://content.rozetka.com.ua/goods/images/big/287017605.jpg', 'TWS (2 окремо)', 'Бездротовые',
        'Bluetooth с микрофоном', 'White', 'с активным шумоподавлением', 'Силекон', 'Динамический', '2022', 'Китай',
        '12 мес:', '27 ч с аккамулятором', 'алюминий',
        'Благодаря светодиодным индикаторам в зарядном устройстве никогда неожиданно не сядет батарейка! И вы всегда будете знать, когда заряд батареи почти исчерпан и пришло время для подзарядки.',
        '41 г', 'вкладыши', 'идёт в комплект чистка для наушников', 'extra', 50, 5)]
print('ok')
con = psycopg2.connect(
    database=os.environ.get('DB_NAME'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASS'),
    host=os.environ.get('DB_HOST')
)
cur = con.cursor()
execute_values(cur,
               "INSERT INTO phones_airpods (id,name, slug, brand,price,photo1,photo2,type,type_connection,enterface,color,anti_shum,ambushur,type_vipe,date_create,country,garantee,time_work,corpus,description,weight,vid,dop_infa,types,count,rating) VALUES %s",
               args)
con.commit()
con.close()
# proxy:8000
