import csv
import numpy as np

from config.settings import DATA_DIRS


class Analysis :
    def localage(self):
        f = open('C:\\PycharmProjects\\day20_dashboard\\data\\age.csv');
        data = csv.reader(f);
        next(data);

        target = '역삼동'
        tcnt = [];
        mcnt = [];
        wcnt = [];
        for row in data :
            if target in row[0] :
                for i in row[3:104] :
                    try :
                        tcnt.append(int(i));
                    except :
                        tcnt.append(int(i.replace(",","")));
                for j in row[106:207] :
                    mcnt.append(int(j.replace(",","")));
                for k in row[209:310] :
                    wcnt.append(int(k.replace(",","")));
        datas = [{
            'name':'Local Age_Total', 'data':tcnt
        },{
            'name':'Local Age_Man', 'data':mcnt
        },{
            'name':'Local Age_Woman', 'data':wcnt
        }];
        print(datas)
        return datas;

    def wm(self):
        f = open('C:\\PycharmProjects\\day20_dashboard\\data\\ta.csv');
        data = csv.reader(f);
        next(data);

        year = 2020;
        month = 10;

        htemp = [];
        ltemp = [];

        for row in data:
            if year == int(row[0].split('-')[0]) and month == int(row[0].split('-')[1]) :
                ltemp.append(float(row[3]));
                htemp.append(float(row[4]));
        datas = [{
            'name':'일별 최저 기온',
            'data' : ltemp
        },{
            'name':'일별 최고 기온',
            'data':htemp
        }];
        print(datas)
        return datas;

    def subway(self):
        f = open('C:\\PycharmProjects\\day20_dashboard\\data\\subway.csv');
        data = csv.reader(f);
        next(data);

        yu = 0;
        yd = 0;
        nu = 0;
        nd = 0;
        tt = 0;

        for row in data :
            if row[1] == '2호선' and row[3] == '강남' :
                yu = int(row[4].replace(",",""));
                yd = int(row[5].replace(",",""));
                nu = int(row[6].replace(",",""));
                nd = int(row[7].replace(",",""));
                tt = yu + yd + nu + nd;

        datas = [{
            'name': '유임승차', 'y': round(100 * (yu / tt), 2)
        },{
            'name': '유임하차', 'y': round(100 * (yd / tt), 2)
        },{
            'name': '무임승차', 'y': round(100 * (nu / tt), 2)
        },{
            'name': '무임하차', 'y': round(100 * (nd / tt), 2)
        }];
        print(datas)
        return datas;

    def achild(self):
        f = open('/data/age3.csv');
        data = csv.reader(f);
        next(data);
        next(data);

        data = list(data);
        ch_list = [];
        for row in data:
            rdata = int(row[3])+int(row[4])+int(row[5])+int(row[6])+int(row[7])+int(row[8]);
            ch_list.append(rdata);

        datas = [{'name':'number of children', 'data':ch_list}];
        print(datas);
        return datas;

    def apop(self):
        f = open('/data/age4.csv');
        data = csv.reader(f);
        next(data);
        next(data);

        rlist = [];
        data = list(data);
        for row in data :
            rdata = int(row[27]) - int(row[1])
            rlist.append(rdata);

        datas = [{'name':'Rate of Increase', 'data':rlist}];
        print(datas);
        return datas;

    def asim(self,gu):
        f = open('/data/age2.csv');
        data = csv.reader(f);
        next(data);

        data = list(data);

        home = None;
        home2 = [];

        for row in data:
            if gu in row[0]:
                home = np.array(row[3:], dtype=int);
                for h in home :
                    home2.append(int(h) / int(row[2]));

        # 모든 지역의 연령별 비율을 구한다.
        min = 999;
        result_name = '';
        result = None;
        away = None;
        away2 = [];
        for row in data:
            away = np.array(row[3:], dtype=int);
            for a in away :
                away2.append(int(a)/int(row[2]));
            s = 0;
            print(len(home2));
            print(len(away2));
            for i in range(len(home2)) :
                m2 = (int(home2[i]) - int(away2[i]))^2;
                s += m2;

            if s < min and gu not in row[0]:
                min = s;
                result_name = row[0];
                result = away2;

        result = list(result);

        datas = [{
            'name':gu, 'data':home2
        },{
            'name':result_name, 'data':away2
        }]

        print(datas);
        return datas

if __name__ == '__main__' :
    Analysis().asim('신림동');