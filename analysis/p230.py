import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#pd.read_csv() 에서 thousands = ','
from config.settings import DATA_DIRS


class P230 :
    def p248(self,loc):
        f = open(DATA_DIRS[0]+'\\age2.csv');
        data = csv.reader(f);
        next(data);

        data = list(data);

        home = None;
        home2 = None;

        for row in data :
            if loc in row[0] :
                home = np.array(row[3:], dtype=int);
                home2 = home / int(row[2].replace(',', ''));

        # 모든 지역의 연령별 비율을 구한다.
        min = 999;
        result_name = '';
        result = None;
        for row in data :
            away = np.array(row[3:], dtype=int);
            away2 = away / int(row[2].replace(',',''));
            s = np.sum(np.abs(home2 - away2));
            if loc not in row[0] and s < min :
                min = s;
                result_name = row[0];
                result = away2;

        datas = [{
            'name':loc,
            'data':home2.tolist()
        },{
            'name':result_name.split(' ')[1],
            'data':result.tolist()
        }];
        print(datas);
        return datas


    # 1. 전국 영유아(만 0세이상 5세 이하)들이 가장 많이 사는 지역 상위 10개를 히스토그램으로 그리시오
    def p2311(self):
        f = open(DATA_DIRS[0]+'\\age3.csv');
        data = csv.reader(f);
        next(data);
        next(data);
        data = list(data);
        result = [];

        for row in data :
            datas = [];
            baby = np.array(row[3:9],dtype=int);
            babys = int(np.sum(baby));

            datas.append(row[0].split(' ')[1]);
            datas.append(babys);

            result.append(datas);

        print(result);
        return result

    def p231(self):
        f = open('age3.csv');
        data = csv.reader(f);
        next(data);
        next(data);

        max = 0;
        min = 999999;
        loc = '';
        minloc = '';
        maxrate = 0.0;
        minrate = 0.0;
        for row in data :
            rdata = np.array(row[3:9], dtype=int);
            sumdata = np.sum(rdata);
            if sumdata > max :
                maxrate = sumdata / int(row[1]) * 100;
                max = sumdata;
                loc = row[0];
            if sumdata < min :
                minrate = sumdata / int(row[1]) * 100;
                min = sumdata;
                minloc = row[0];

        print(loc, max, maxrate);
        print(minloc, min, minrate);


   # 2. 서울에서 5년간 인구가 가장 많이 늘어난 지역을 구하시오
    def p232(self):
        # 2020
        f = open(DATA_DIRS[0]+'\\age4.csv');
        data = csv.reader(f);
        next(data);
        next(data);
        data = list(data);

        #2015
        f2 = open(DATA_DIRS[0]+'\\age5.csv');
        data2 = csv.reader(f2);
        next(data2);
        data2 = list(data2);

        loc = [];
        rdata = [];

        for row in data :
            for row2 in data2 :
                d = 0;
                if row[0] == row2[0] :
                    d = int(row[27]) - int(row2[1]);
                    loc.append(row[0].split(' ')[1]);
                    rdata.append(d);

        result = {
            'locs':loc,
            'datas':rdata
        };
        print(result);

        return result


if __name__ == '__main__' :
    P230().p232();



