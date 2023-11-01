import datetime
import csv
import os
base_path = "C:\\Users\\araha\\PycharmProjects\\pythonProject\\"
def split(building):
    main_path = "C:\\Users\\araha\\Downloads\\Solar Data "+building
    new_path = "C:\\Users\\araha\\Downloads\\"+building+" Split Data\\"
    initial_date = datetime.datetime(2023, 1, 1)
    for file in os.listdir(main_path):
        path = main_path+"\\"+file
        with open(path) as f_in:
            data = csv.reader(f_in)
            next(data)
            delta = datetime.timedelta(days=1)
            split_data = [rows for rows in data]
            idx = int(len(split_data)/96)
            split_data = [split_data[96*x:96*x+96] for x in range(idx)]
            for row in split_data:
                string = building+"_Analysis_"+initial_date.strftime("%Y_%m_%d")+".csv"
                with open(string,"w", newline="") as f_out:
                    writer = csv.writer(f_out)
                    writer.writerow([";UNIS - "+building+" / Power / Mean values [kW]"])
                    writer.writerows(row)
                    f_out.close()
                    os.rename(base_path+string, new_path+string)
                initial_date = initial_date+delta

