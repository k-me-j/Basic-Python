from glob import glob
import json

def modified(path):
    # 파일 경로 리스트로 생성 : ['d:/Kamie/dataset/CAM_FRONT\\000000.json', ... ]
    file_paths = glob(path + "/*.json")
    file_paths = [f for f in file_paths if f.split("\\")[-1].startswith("modified_") == False]

    vehicle = ["Truck", "Car"]

    # json 파일 하나씩 가져오기
    for file in file_paths:
        with open(file) as f:
            json_data = json.load(f)
            i = 0   # json_data["Object"] 요소를 하나씩 가져오기 위한 인덱스
            
            # json_data["Object"] 안의 데이터를 순서대로 하나씩 가져오기
            for _ in range(len(json_data["Object"])):
                per = json_data["Object"][i]

                # level이 0이 아니거나 class가 Dontcare인 데이터는 제거
                if (per['level'] != 0) or (per["class"] == "Dontcare"):
                    json_data["Object"].remove(per)
                    continue  # for문 처음으로 돌아가기. 요소를 삭제했기 때문에 i 증가 안함

                # class가 truck, car인 경우 vehicle로 변경
                if per["class"] in vehicle:
                    per["class"] = "Vehicle"

                i += 1   # 인덱스 증가
                # i를 따로 지정한 이유 : 중간에 remove()를 통해 요소를 삭제하는 경우 list의 length가 줄어들면서 인덱스 에러 발생함


    # 새로운 이름으로 json 파일 저장
    for file in file_paths:
        old = file.split("\\")    # ex) ['d:/Kamie/dataset/CAM_FRONT', '000000.json']
        new_name = old[0] + "/modified_" + old[1]
        with open(new_name, "w") as f:
            json.dump(json_data, f, indent=2)

    print("Done")

if __name__ == "__main__":
    path = "d:/Kamie/dataset/CAM_FRONT/"
    modified(path)

