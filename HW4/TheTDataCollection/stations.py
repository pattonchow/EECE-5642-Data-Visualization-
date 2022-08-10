import pandas as pd

def main():
    #file_path = "C:\Users\patto\Desktop\课程\dv5642\HW\HW4\HW4-1\HW4-code\data.html"
    file_name = "data.html"
    table = pd.read_html(file_name)
    print("table count:", len(table))

    data_frame1 = table[0]
    data_frame2 = table[1]

    #print(data_frame1)
    data_frame1.to_csv("stations.csv", index = False)

if __name__ == "__main__":
    main()