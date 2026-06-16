# Local-ETL-Pipeline

## Overview

โปรเจกต์นี้เป็นการสร้าง ELT (Extract, Load, Transform) Pipeline บนเครื่อง Local เพื่อดึงข้อมูลจากไฟล์ CSV ทำการโหลดเข้าสู่ฐานข้อมูล PostgreSQL และแปลงข้อมูลด้วย Python ก่อนนำไปใช้สำหรับการวิเคราะห์ข้อมูล

วัตถุประสงค์ของโปรเจกต์คือเพื่อศึกษากระบวนการ Data Engineering ตั้งแต่การจัดเก็บข้อมูลดิบจนถึงการเตรียมข้อมูลสำหรับ Dashboard และ Reporting

---

## Architecture

CSV Files
↓
Extract (Pandas)
↓
Load (PostgreSQL)
↓
Transform (Python / SQL)

---

## Technologies

* Python
* Pandas
* PostgreSQL
* SQLAlchemy
* Git

---

## Project Structure

project/

├── data/

│   └── ecommerce_sales_data.csv

├── scripts/

│   ├── extract.py

│   ├── load.py

│   └── transform.py

├── main.py

├── requirements.txt

├── README.md


---

## Pipeline Steps

### 1. Extract

อ่านข้อมูลจากไฟล์ CSV ภายในโฟลเดอร์ data/ecommerce_sales_data.csv

### 2. Load

นำข้อมูลเข้าสู่ PostgreSQL ในรูปแบบ Raw Table

### 3. Transform

* ลบข้อมูลที่ Customer ID เป็นช่องว่าง
* ตรวจสอบข้อมูลอื่นๆที่เป็นช่องว่าง
* สร้างคอลัมน์คำนวณเพิ่มเติม

### 4. Output

จัดเก็บข้อมูลที่ผ่านการแปลงแล้วลง Analytics Table สำหรับนำไปใช้งานต่อ

---

## How to Run

1. Clone Repository

git clone <repository-url>

2. Install Dependencies

pip install -r requirements.txt

3. Start PostgreSQL

4. Run Pipeline

python main.py

---

## Future Improvements

* Add Apache Airflow orchestration
* Add Data Quality Checks
* Add Incremental Loading
* Deploy Pipeline to Cloud Environment

---

## Skills Demonstrated

* Data Extraction
* Data Transformation
* Data Loading
* SQL Development
* Database Design
* Python Data Processing
* ETL/ELT Concepts
