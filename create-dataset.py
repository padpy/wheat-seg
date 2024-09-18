import glob
import os
import orjson

def main():
    # Create directory
    dirs = ['images', 'images/train', 'images/val', 'images/test', 'labels', 'labels/train', 'labels/val', 'labels/test']
    for dir in dirs:
        os.makedirs(dir, exist_ok=True)
        
    # Get files at location using glob
    files = glob.glob('D:\wheat\dataset\*\*.json')
    for file in files:
        split_type = os.path.basename(os.path.dirname(file))
        json_data = orjson.loads(open(file).read())
        height = json_data['imageHeight']
        width = json_data['imageWidth']
        shapes = json_data['shapes']
        
        with open(f'labels/{split_type}/{os.path.basename(file).replace(".json", ".txt")}', 'w') as f:
            for shape in shapes:
                if shape["shape_type"] != "polygon":
                    continue
                
                if "spike" not in shape["label"]:
                    continue
                
                f.write(f"0 {' '.join([f'{x/width:6f} {y/height:6f}' for x, y in shape['points']])}\n")
            
        
        exit()
        
if __name__ == '__main__':
    main()
