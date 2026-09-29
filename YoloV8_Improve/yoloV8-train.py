from ultralytics import YOLO


if __name__ == '__main__':
    final_path = 'train_yaml/improve_all_yolov8n.yaml'
    model = YOLO(final_path)
    model.train(data='./my_data.yaml', workers=8, epochs=200, batch=8, optimizer='SGD', device='0')
