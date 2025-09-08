import torch as th
from ultralytics import YOLO

def main():
    # loads pretrained YOLOv11n model, resumed from last training
    model = YOLO('./weights/runs/yolo11n_pcb_defectsv1/weights/last.pt')

    # trains model based on data.yaml dataset config
    # gpu acceleration is enabled
    results = model.train(
        data='./datasets/data.yaml',
        epochs=100,
        imgsz=640,
        batch=16,
        device=0 if th.cuda.is_available() else 'cpu',
        name='yolo11n_pcb_defectsv2',
        project='./weights/runs',
        # exists_ok=True
    )

    print(f"Training complete.")

if __name__ == '__main__':
    main()