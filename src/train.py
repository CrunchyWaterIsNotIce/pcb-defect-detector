import torch as th
from ultralytics import YOLO

def main():
    # loads pretrained YOLOv11n model, resumed from last training
    model = YOLO('yolo11n.pt')

    # trains model based on data.yaml dataset config
    # gpu acceleration is enabled
    results = model.train(
        data='./datasets/data.yaml',
        epochs=200,
        imgsz=640,
        batch=16,
        patience=25,
        device=0 if th.cuda.is_available() else 'cpu',
        name='yolo11n_pcb_defectsv2',
        project='./weights/runs',
    )

    print(f"Training complete.")

if __name__ == '__main__':
    main()