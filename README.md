> pcb-defect-detector
# VisionPCB

VisionPCB is a web-based application that uses a fine-tuned YOLO model to automatically detect common manufacturing defects on Printed Circuit Boards (PCBs). This project aims to streamline the quality assurance process in electronics manufacturing by providing a fast and accurate inspection tool.

![VisionPCB Demo GIF](assets/demo.gif)

---

## Features

* **Accurate Detection:** Utilizes a YOLOv11n model fine-tuned on a custom dataset for precise results.
* **Multiple Defect Catagories:** Capable of identifying 6 common types of PCB defects:
    * `mouse_bite`
    * `spur`
    * `missing_hole`
    * `short`
    * `open_circuit`
    * `spurious_copper`
* **Web Interface:** A clean and simple user interface built with Flask that allows users to show their camera their PCBs for analysis.

---

## Tech Stack

* **Backend:** Python, Flask, PyTorch, Ultralytics YOLO, OpenCV
* **Frontend:** HTML, CSS

---

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.10+
* Git

### Installation

1.  **Clone repository:**
    ```sh
    git clone [https://github.com/your_username/pcb-defect-detector.git](https://github.com/your_username/pcb-defect-detector.git)
    cd pcb-defect-detector
    ```

2.  **Create and activate virtual environment:**
    ```sh
    # Windows:
    python -m venv .venv
    .\.venv\Scripts\activate

    # macOS/Linux:
    # python3 -m venv .venv
    # source .venv/bin/activate
    ```

3.  **Install required packages:**
    ```sh
    pip install -r requirements.txt
    ```

---

## Usage

To run the Flask application locally, execute the following command from the root directory of the project:

```sh
python app.py
